#!/bin/bash

# Update and install Docker
apt-get update
apt-get install -y docker.io
systemctl enable docker
systemctl start docker

