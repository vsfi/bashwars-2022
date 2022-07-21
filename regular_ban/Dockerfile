FROM alpine

RUN apk add mandoc man-pages coreutils-doc less less-doc

RUN mkdir /home/vsfi
WORKDIR /home/vsfi

COPY fail2ban.log .
COPY text.txt .
COPY Hello.sh .
RUN chmod +x Hello.sh

ENTRYPOINT ["/home/vsfi/Hello.sh"]

CMD /home/vsfi/Hello.sh
