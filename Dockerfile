FROM python:alpine

RUN mkdir /twitter_bot
RUN mkdir /twitter_bot/data

COPY api_setup.py /twitter_bot
COPY retweet.py /twitter_bot

RUN pip3 install --no-cache-dir twython

RUN addgroup -g 1000 --system twitterbot && adduser --system --shell /bin/false --no-create-home --ingroup twitterbot twitterbot

RUN chown -R twitterbot:twitterbot /twitter_bot

WORKDIR /twitter_bot

USER twitterbot

CMD ["python3","-u","retweet.py"]
