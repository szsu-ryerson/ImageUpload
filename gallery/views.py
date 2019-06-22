import werkzeug.security
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from flask_bootstrap import Bootstrap
from gallery import app, db, models
from gallery.forms import LoginForm, RegistrationForm
from gallery.tools import upload_file_to_s3, list_files_in_s3, delete_file_from_s3
from sightengine.client import SightengineClient

Bootstrap(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

ALLOWED_EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]

@login_manager.user_loader
def user_loader(user_id):
    print ("LOADING USER FOR " + user_id)
    return models.LoginUser.query.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('images'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.LoginUser.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            print ("INVALID")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('images'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("images"))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
@login_required
def process_file():

    if not current_user.is_authenticated:
        flash('Only authenticated users can upload or delete images')
        return redirect(url_for('images'))
        
    if len(list(request.form.keys())) > 0 and request.form["delete"]:
        output = delete_file_from_s3(app.config["S3_BUCKET"], request.form["delete"])
        models.Appimage.query.filter_by(URL=request.form["delete"]).delete()
        db.session.commit()
        return redirect(url_for('images'))

    
    file    = request.files["user_file"]


    if file.filename and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output   	  = upload_file_to_s3(file, app.config["S3_BUCKET"])

        client = SightengineClient('1959849289', 'Wm9a6r2E8SnF7oBfNJUW')
        output2 = client.check('nudity','wad','celebrities','scam').set_url(app.config["S3_LOCATION"]+'/'+file.filename)


        #Get the probability that the face belongs to said celebrity
        celeProb=0
        for face in output2["faces"]:
            celebrities = face.get("celebrity")
    
            for cele in celebrities:
                if(celeProb<cele.get("prob")):
                    celeProb=cele.get("prob")


        #Nudity check: probability that the image does not contain nudity
        #Celebrity check: Probability that the face belongs to said celebrity
        #Weapon check: Probability that the image contains weapons
        #Scammer check: Probability that there is a scammer on the image
        #Offensive check: Probability that the image contains offensive content
        if(float(output2["nudity"]["safe"])<0.5 or celeProb>0.8 or float(output2["weapon"])>0.4 or float(output2["scam"]["prob"])>0.3):
            delete_file_from_s3(app.config["S3_BUCKET"], file.filename)
            flash('Image denied')
            #flash(float(output2["nudity"]["safe"]))
            #flash(celeProb)
            #flash(float(output2["weapon"]))
            #flash(float(output2["scam"]["prob"]))
        else:
            user = models.Appuser.query.filter_by(email=current_user.get_id()).first()
            i = models.Appimage(appuser_id=user.get_id(), URL=file.filename)
            db.session.add(i)
            db.session.commit()

        return redirect(url_for('images'))

    else:
        return redirect(url_for('images'))


@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.LoginUser(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        
        appuser=models.Appuser(email=user.get_id(), username=user.get_id())
        db.session.add(appuser)

        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/images')
def images():
    #images2 = list_files_in_s3(app.config["S3_BUCKET"])
    fileNames=[]
    user = models.Appuser.query.filter_by(email=current_user.get_id()).first()
    allUsers_original = models.Appuser.query.with_entities(models.Appuser.id, models.Appuser.email).all()
    allUsers=[[id, email] for (id ,email) in allUsers_original]


    userEmail = '';
    if(user is not None):
        #images = models.Appimage.query.filter_by(appuser_id = user.get_id()).with_entities(models.Appimage.URL, models.Appimage.appuser_id).all()
        images = db.session.query(models.Appimage).filter_by(appuser_id = user.get_id()).with_entities(models.Appimage.URL, models.Appimage.appuser_id).all()
        fileNames = [[value,id] for (value,id) in images]
        userEmail = user.email
    else:
        images = db.session.query(models.Appimage).with_entities(models.Appimage.URL, models.Appimage.appuser_id).all()
        fileNames = [[value,id] for (value,id) in images]

    return render_template('images.html', fileNames=fileNames, user=userEmail, allUsers=allUsers)



"""
@app.route('/images')
def images():
    #images2 = list_files_in_s3(app.config["S3_BUCKET"])
    fileNames=[]
    user = models.Appuser.query.filter_by(email=current_user.get_id()).first()
    allUsers_original = models.Appuser.query.with_entities(models.Appuser.email).all()
    allUsers=[value for value, in allUsers_original]


    userEmail = '';
    if(user is not None):
        #images = models.Appimage.query.filter_by(appuser_id = user.get_id()).with_entities(models.Appimage.URL, models.Appimage.appuser_id).all()
        images = db.session.query(models.Appuser, models.Appimage).join(models.Appimage).filter_by(appuser_id = user.get_id()).with_entities(models.Appimage.URL, models.Appuser.email).all()
        fileNames = [[value,id] for (value,id) in images]
        userEmail = user.email
    else:
        images = db.session.query(models.Appimage, models.Appuser).join(models.Appuser).with_entities(models.Appimage.URL, models.Appuser.email).all()
        fileNames = [[value,id] for (value,id) in images]
        flash(fileNames)
        

    return render_template('images.html', fileNames=fileNames, user=userEmail, allUsers=allUsers)
"""
