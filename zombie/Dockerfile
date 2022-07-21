# FROM ubuntu:18.04

# # RUN 
# RUN apt update
# RUN apt install -y psmisc
# RUN apt install -y gcc musl-dev
FROM alpine

# RUN 
RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN apk add gcc musl-dev

WORKDIR /data
COPY child.c .
RUN gcc child.c -o child 
COPY *.sh .
COPY *.txt .
RUN chmod +x *.sh

ENTRYPOINT ["/data/runner.sh"]

CMD /data/runner.sh


# FROM alpine

# # RUN 
# RUN apk add mandoc man-pages coreutils-doc less less-doc
# RUN apk add gcc musl-dev
