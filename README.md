# CCPS 530 project

A flask web application that allow different users to upload images and also view images upload by others. The images uploaded will be moderated by Sightengine and stored in Amazon S3.


## Online Demo
https://boiling-peak-13795.herokuapp.com/images#


## Image moderation 
* [Sightengine](https://sightengine.com/): The SDK that will allow us to automatically moderate our images
* Models used: Nudity detection, Celebrities, Scammers, Weapons

## Plugins
* [Image gallery](https://github.com/mohamednasr/MAgallery)
* [Show password](http://bootstrap-show-password.wenzhixin.net.cn/home/)

## Getting Started

### Prerequisites

* Amazon S3 storage service: [Set up a S3 bucket](https://www.lynda.com/Flask-tutorials/Amazon-Simple-Storage-Service-S3-setup/704154/5034692-4.html)

* PostgreSQL database [Install Heroku CLI](https://www.lynda.com/Flask-tutorials/) /  [Create a POstgreSQL database](https://www.lynda.com/Flask-tutorials/Create-PostgreSQL-database/704154/5034691-4.html)


### Configuration
Clone the [repo](https://github.com/szsu-ryerson/ImageUpload)

*Update the following fields in the file "config.py"

* SQLALCHEMY_DATABASE_URI
* S3_BUCKET
* S3_SECRET
* S3_KEY
* S3_LOCATION
* SECRET_KEY


## Deploy the application to Heroku
In the terminal, go into the directory for this project and use the following commands:

Create a git repository
```
git init
```

Creat a new application in Heroku
```
heroku create
```

Add the files to the repository
```
git add -A
```
Commit the files
```
git commit -a -m "Initial application setup"
```

Push the file to Heroku
```
git push heroku master
```
