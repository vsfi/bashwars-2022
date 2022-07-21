FROM alpine

WORKDIR /data
# RUN apk add mandoc man-pages coreutils-doc less less-doc tar
# COPY --from=stage /data/time.tar.gz .
COPY frames/*.frame frames/
COPY banner.txt .
COPY *.sh .
RUN chmod +x *.sh

RUN adduser -D hunter

WORKDIR /home/hunter

ENTRYPOINT ["/data/banner.sh"]

CMD /data/banner.sh
