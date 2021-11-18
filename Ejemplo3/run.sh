#!/bin/bash

docker build -t ejemplo3_img .
docker run -d -p 5001:5001 ejemplo3_img

sleep 10