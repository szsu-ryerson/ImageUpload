# CCPS 530 project

A flask web application that allow different users to upload images and also view images upload by others


## Online Demo
(https://boiling-peak-13795.herokuapp.com/images#)


## Image moderation 
* Sightengine: The SDK that will allow us to automatically moderate our images
* (https://sightengine.com/)


## Getting Started

### Prerequisites

* Amazon S3 storage service: [Tutorial](https://www.lynda.com/Flask-tutorials/Amazon-Simple-Storage-Service-S3-setup/704154/5034692-4.html)

* PostgreSQL database

[Install Heroku CLI](https://www.lynda.com/Flask-tutorials/)
[Create a POstgreSQL database](https://www.lynda.com/Flask-tutorials/Create-PostgreSQL-database/704154/5034691-4.html)


### Configuration
     UPdate the following fields in the file "config.py"

		* SQLALCHEMY_DATABASE_URI
		* S3_BUCKET
		* S3_SECRET
		* S3_KEY
		* S3_LOCATION
		* SECRET_KEY


## Deploy the server application to Heroku


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
