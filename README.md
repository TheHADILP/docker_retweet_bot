# Retweet-Bot for Twitter with Docker and Twython
This is the Docker version of my Twitter Bot: https://twitter.com/TLoveBotti

## Installation
Clone the repository
```git clone https://github.com/TheHADILP/docker_retweet_bot.git```

and run the [docker_build_and_run.sh](https://github.com/TheHADILP/docker_retweet_bot/blob/master/docker_build_and_run.sh) script for easy and hassle-free setup or find the commands here:

```
# Build the Docker Image
docker build --no-cache --rm --pull -t twitter_bot .

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
```

## Persistent Data Directory

The ```twitter_bot_data``` directory gets mounted to the Docker Container and contains all the persistent files explained below:

### twitter-creds
You can set up the API access for your Twitter account on https://developer.twitter.com/en/apps

Enter your API credentials in this file:  
Put each item on a separate line and remove all quotes.
```
"Consumer Key"
"Consumer Secret"
"Access Token"
"Access Token Secret"
```
Run the following command to prevent your API credentials being accidentally pushed to git:  
```git update-index --skip-worktree twitter_bot_data/twitter-creds```

### retweet-blacklist
All retweeted Tweet-IDs are saved in this file.  
This ensures that no duplicate posts are tweeted.

### users
A list of Twitter user that you want to iterate through (one user per line).  
The file is prepopulated with some names, modify as you like.  
Changes take immediate effect, so no need to restart anything.

### buzzwords
A list of words that the filtered Tweets are checked against (one word per line).  
At least one of those words needs to be included in a Tweet's text in order to get retweeted.  
The file is prepopulated with some example words, modify as you like.  
Changes take immediate effect, so no need to restart anything. (Surprise, huh)
