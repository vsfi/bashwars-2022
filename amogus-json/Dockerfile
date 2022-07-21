FROM alpine 

RUN apk add --no-cache jq jq-doc mandoc man-pages coreutils-doc && mkdir -p /home/vsfi

ADD jsons/* /home/vsfi
ADD hello /bin/hello

RUN chmod +x /bin/hello
ENTRYPOINT ["/bin/hello"]

WORKDIR /home/vsfi

