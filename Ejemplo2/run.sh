#!/bin/bash

docker build -t ejemplo2_img .
docker run -d -p 5000:5000 ejemplo2_img