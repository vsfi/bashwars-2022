from python:3.10 as stage

WORKDIR /data

COPY . /data
RUN mkdir -p files
RUN python generate.py

FROM alpine

WORKDIR /home
RUN apk add mandoc man-pages coreutils-doc less less-doc
COPY --from=stage /data/files .
COPY banner.txt .
COPY banner.sh .
RUN chmod +x banner.sh

ENTRYPOINT ["/home/banner.sh"]

CMD /home/banner.sh
