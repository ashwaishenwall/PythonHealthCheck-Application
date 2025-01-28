#!/bin/bash

# Pull the latest Nginx Docker image
docker pull nginx:latest
docker run -d -p 80:80 --name nginx-server nginx:latest
