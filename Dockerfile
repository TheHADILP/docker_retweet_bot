FROM python:alpine

RUN mkdir /twitter_bot

COPY api_setup.py /
COPY retweet.py /

RUN pip3 install --no-cache-dir twython

RUN addgroup --system twitterbot && adduser --system --shell /bin/false --no-create-home --ingroup twitterbot twitterbot

USER twitterbot

CMD ["python3","-u","retweet.py"]
