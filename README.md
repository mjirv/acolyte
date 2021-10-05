# Acolyte
_Self-service data analytics powered by GPT-3_

![Screenshot](screenshot.PNG)

## About
Acolyte is self-service business analytics. Users can ask questions like "how many customers do we have?" or "who placed the most orders last week?" in plain English and get the right answer from their data warehouse.

## Deployment
There are two separate applications to deploy (the api and client). The easiest way to deploy is on Heroku via the following steps:
1. Create a new API Heroku app and a new Client heroku app.
2. In the API app (via the Heroku command line or the Heroku web UI):
    1. add the `heroku/python` buildpack.
    2. Add a `DATABASE_URL` environment variable with the full URI to your database (i.e. `postgres://USER:PASSWORD@HOSTNAME:PORT/DATABASE`) 
    3. Add an `OPENAI_API_KEY` environment variable with your OpenAI API key.
3. In the Client app (via the Heroku command line or the Heroku web UI):
    1. Add the `heroku/nodejs` buildpack and the `https://github.com/heroku/heroku-buildpack-static` buildpack.
    2. Add a `VUE_APP_API_ENDPOINT` with the url to your API (e.g. `https://acolyte-api.herokuapp.com/api`)
4. In this directory, via the Heroku command line, run the following:
```bash
heroku git:remote --remote heroku-client -a YOUR_CLIENT_HEROKU_APP_NAME
heroku git:remote --remote heroku-server -a YOUR_API_HEROKU_APP_NAME
git subtree push --prefix client heroku-client master
git subtree push --prefix api heroku-server master
```