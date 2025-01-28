#!/bin/bash

# Start an Nginx container
docker run -d -p 80:80 --name nginx-server nginx:latest

