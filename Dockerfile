FROM python:alpine

RUN mkdir /twitter_bot

COPY api_setup.py /
COPY retweet.py /

RUN pip3 install --no-cache-dir twython

CMD ["python3","-u","retweet.py"]
