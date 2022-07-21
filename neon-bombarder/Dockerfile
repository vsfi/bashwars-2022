from python:3.10 as stage

RUN pip install Pillow numpy piexif
COPY . /data/
WORKDIR /data
RUN mkdir -p images
RUN python generate.py


FROM alpine
RUN apk update
RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN apk add exiftool
RUN mkdir -p /home/vsfi

COPY --from=stage /data/images/ /home/vsfi
ADD hello /bin/hello

RUN chmod +x /bin/hello

ENTRYPOINT ["/bin/hello"]
WORKDIR /home/vsfi
