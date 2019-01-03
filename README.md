# Retweet-Bot for Twitter with Docker and Twython
This is the Docker version of my Twitter Bot: https://twitter.com/TLoveBotti

## Installation
Clone repository:
```git clone https://github.com/TheHADILP/docker_retweet_bot.git```

```
# Build the Docker Image
docker build -t twitter_bot .

# Stop the perhaps already running Docker Container
docker stop twitter_bot

# Remove the old Docker Container
docker container rm twitter_bot

# Docker Run Command to start a new container and mount the directory
docker run -d \
    --name twitter_bot \
    -v "/home/ubuntu/twitter_bot/:/twitter_bot/" \
    --restart=unless-stopped \
    twitter_bot
```

## Twitter creds
Now you can set up the API access for your Twitter account on https://developer.twitter.com/en/apps

Enter your API keys in the twitter-creds file:  
Put each item on a separate line and remove all quotes.
```
"Consumer Key"
"Consumer Secret"
"Access Token"
"Access Token Secret"
```
Run the following command to prevent your API credentials being accidentally pushed to git:  
```git update-index --skip-worktree twitter-creds```

## Blacklist
All retweeted Tweet-IDs are saved in the retweet_blacklist file.
This ensures that no duplicate posts are tweeted.
