# Deploying a Flask API

This was fourth project for the Udacity course Full Stacke developer [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

The Goal of the project was to containerize and deploy a Flask API to a Kubernetes cluster using Docker, AWS EKS, CodePipeline, and CodeBuild.

The Flask app consists of a simple API with three endpoints:

- `GET '/'`: This is a simple health check, which returns the response 'Healthy'. 
- `POST '/auth'`: This takes a email and password as json arguments and returns a JWT based on a custom secret.
- `GET '/contents'`: This requires a valid JWT, and returns the un-encrpyted contents of that token. 

The app relies on a secret set as the environment variable `JWT_SECRET` to produce a JWT. The built-in Flask server is adequate for local development, but not production, so you will be using the production-ready [Gunicorn](https://gunicorn.org/) server when deploying the app.
The AWS endpoint of this project is : ` a513859296ba111eaa0da0e8387c1a80-1573041465.us-west-2.elb.amazonaws.com`


## Test endpoints:
```
export TOKEN=`curl -d '{"email":"<EMAIL>","password":"<PASSWORD>"}' -H "Content-Type: application/json" -X GET  a513859296ba111eaa0da0e8387c1a80-1573041465.us-west-2.elb.amazonaws.com/auth  | jq -r '.token'`
curl --request GET 'a513859296ba111eaa0da0e8387c1a80-1573041465.us-west-2.elb.amazonaws.com/contents' -H "Authorization: Bearer ${TOKEN}" | jq 

```

