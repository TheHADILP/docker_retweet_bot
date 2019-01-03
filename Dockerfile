FROM python:2-alpine

RUN mkdir /twitter_bot

ADD api_setup.py /
ADD retweet.py /

RUN pip install twython

CMD [ "python", "./retweet.py" ]

#ENTRYPOINT [ "python", "./retweet.py" ]
