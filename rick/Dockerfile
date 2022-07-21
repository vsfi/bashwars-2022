from python:3.10 as stage

RUN pip install ffmpeg-python leet
RUN apt update -y
RUN apt install -y ffmpeg
COPY . /data/
WORKDIR /data
RUN mkdir -p audio
RUN python generate.py

from alpine:latest

RUN apk update
RUN apk add ffmpeg
WORKDIR /data
COPY banner.sh .
COPY task .
RUN chmod +x banner.sh
COPY --from=stage /data/audio/ .
CMD /data/banner.sh
