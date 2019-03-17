#!/bin/bash
docker build . -t jwt-api-test
docker run -p 8080:8080 --env-file env_file jwt-api-test
curl http://127.0.0.1:8080
