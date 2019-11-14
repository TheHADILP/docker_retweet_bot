#!/bin/bash

# Build the Docker Image
docker build --no-cache --rm --pull -t twitter_bot .

# Stop the perhaps already running Docker Container
docker stop twitter_bot

# Remove the old Docker Container
docker container rm twitter_bot

# Docker Run Command to start a new container and mount the directory
docker run -d \
    --name twitter_bot \
    -v "$(pwd)/data/:/twitter_bot/data/" \
    --restart=unless-stopped \
    twitter_bot
