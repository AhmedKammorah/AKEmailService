# AKEmailService 

Email Service




Description of the problem and solution.
Whether the solution focuses on back-end, front-end or if it's full stack.

Reasoning behind your technical choices, including architectural.
Trade-offs you might have made, anything you left out, or what you might do 
differently if you were to spend additional time on the project.



# The Problem

# The Solution
	Backend Service with it's API docs and clients 
## Questions 
* Is there any periority of using the service ?
* What Happen when profider go down?
	* Failover to the other 
		* what happen when old provider come back 
		* what happen when the new provider go down

## High level architecture

![High level architecture](static/AkEmailService-1.png)

![Option 1](static/AkEmailService-4.png)
## Alternative 
![Option 1](static/AkEmailService-2.png)
![Option 2](static/AkEmailService-3.png)
## What Next 

## Components 
1. Email Provider Connectors 
	1. sendgrid connector
	2. sparkposr connector
2. Main Email Service 
3. Health check Service 
4. Rest API Service 
5. RPC Service Server/client
6. some tests
7. API docs
8. Docker/Docker-compose and running scripts


### Email Providers 
	* sendgrid
	* sparkpost

# Getting Started

## steps 
* build docker image 
* Run docker compose 
	* Run Redis container
	* Run Rest API Service 
	* Run RPC Service
	* Run Health check(heartbeat) searvice 
* User Rest API
	* check api docs /apidocs
	* /api/auth to get token
	* /api/email [POST] with JWT token
* Use RPC client


## Init
* clone this repo
* Code Dir Tree
	```
	./
		MainService/    <Your main Flask  code dir> 
		Readme.md
		docker-entrypoint.sh
		..
	```
## Config 
#### Env Variable 
create file ak_variables.env
OR just add my ak_variables.env which i sent 
```
AK_APP_ENV=<pro  or dev>
BASE_HOST=<HOSTIP OR local host>
SENDGRID_API_KEY=<YOUR_API_KEY>
SPARKPOST_API_KEY=<YOUR_API_KEY>
AK_API_JWT_SECRET_KEY=<Choose SECRET Key to used to auth and generate JWT Token>
```
#### Email Providers connectors 
```
	sendgrid:
	    API_KEY: "<YOUR_API_KEY>"
	    STATUS_URL: "http://status.sendgrid.com/api/v2/summary.json"
	    COMPONENT_NAME: "Mail Sending"
	sparkpost:
	    API_KEY: "<YOUR_API_KEY>"
	    STATUS_URL: "https://status.sparkpost.com/api/v2/summary.json"
	    COMPONENT_NAME: "Transmissions API"
```
## Running Pre Requirements
#### Option 1 (Recommended)
	* Docker
	* Docker-compose
#### Option 2
	* Redis server 
		* REDIS_HOST = "ak-redis"
		* REDIS_PORT = 6379
	* Python 3.X
	* pip and python requirements in requirements.txt
		```
			pip install --no-cache-dir -r requirements.txt
		```
	* Run each service separately 

## Build

* Build The images
```
    cd $PWD
	sh build_docker_image.sh 

```
* OR Pull the image from Docker hub 
```
    cd $PWD
	docker pull ahmedkammorah/ak_email_service 

```
## Run
#### Start Container On (Dev Mode) 
```
	sh run_redis.sh
	sh run_ak_dev.sh
```

#### Start Container On (Pro Mode) 
```
	docker-compose up
```
## Deployment
### Services are depoyed on AWS 
* [Main API docs](http://13.58.165.80:5000/apidocs)

## Use The Demo 
### Use Rest API
* Check The API Doc 
	* [Swagger API docs](http://13.58.165.80:5000/apidocs)
* Start Login to get the JWT Token to be able to user the send API Endpoint
	* [Auth Endpoint  /api/auth ](http://13.58.165.80:5000/apidocs/#/AKAuth)
		* username: <Main user name\>
		* password: <Main Password\>
* Test the token on the protected endpoint
	* [Protected test Endpoint /api/protected](http://13.58.165.80:5000/apidocs/#/AKAuth/get_api_protected)
* Use the send Eamil endpoint
	* [Send Email Endpoint /api/email [POST]](http://13.58.165.80:5000/apidocs/#/AKEmailServiceAPI/sendEmail)
### Use RPC client

# Author
* Ahmed Kammroah 
	* [ahmedkammorah](https://github.com/AhmedKammorah) 
	* [resume](https://github.com/AhmedKammorah/my_resume_latex)
	* [LinkedIn](https://www.linkedin.com/in/ahmedkammorah/)
