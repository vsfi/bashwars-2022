FROM alpine

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN apk add python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask
RUN apk add jq jq-doc curl curl-doc

RUN rm /usr/bin/wget
RUN touch /usr/bin/wget
RUN chmod 700 /root
RUN chmod 700 /usr/bin/python3

COPY webapp.py /root/
COPY data.json /root/
COPY banner.txt /home/
COPY hello /home/
RUN chmod +x /home/hello

RUN adduser --disabled-password bbalance

WORKDIR /home/bbalance

ENTRYPOINT ["/home/hello"]

CMD /home/hello
