FROM alpine

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password michele
WORKDIR /michele
COPY ./_start.sh .
COPY hello .
COPY banner.txt .
RUN chmod +x hello _start.sh
RUN sh _start.sh
RUN rm _start.sh

ENTRYPOINT ["/michele/hello"]
CMD /michele/hello