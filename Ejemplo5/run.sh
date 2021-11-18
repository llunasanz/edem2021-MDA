#!/bin/bash

docker pull 
docker build -t ejemplo5_img .
docker run -p 5002:5002 jupyter/minimal-notebook 


sleep 10