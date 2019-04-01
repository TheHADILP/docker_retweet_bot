#!/bin/bash

# Build the Docker Image
docker build --rm -t twitter_bot .

# Stop the perhaps already running Docker Container
docker stop twitter_bot

# Remove the old Docker Container
docker container rm twitter_bot

# Docker Run Command to start a new container and mount the directory
docker run -d \
    --name twitter_bot \
    -v "$(pwd)/twitter_bot_data/:/twitter_bot/" \
    --restart=unless-stopped \
    twitter_bot
