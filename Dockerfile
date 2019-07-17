FROM python:alpine

RUN mkdir /twitter_bot

COPY api_setup.py /
COPY retweet.py /

RUN pip install --no-cache-dir twython

CMD ["python","-u","retweet.py"]
