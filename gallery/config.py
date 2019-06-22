import os

class Config(object):
	SQLALCHEMY_DATABASE_URI="postgres://rcezaasgarfdnn:0ded998f6a193b89f391621e9fe1fc51b3d3c7a3db8b06b885f391af60166a6a@ec2-54-163-230-199.compute-1.amazonaws.com:5432/d2pvkehpsl7umo"
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	S3_BUCKET="ccps530"
	S3_SECRET="mr+O9KeC+zcT5mQEbDFhZcghj/ijCmCxWrnwG6x+"
	S3_KEY="AKIAVQNMIRYRPSUIL7FH"
	S3_LOCATION='https://ccps530.s3.ca-central-1.amazonaws.com'
	ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif'])
	SECRET_KEY="SPFTIjokdkfjekls=esitd"

	