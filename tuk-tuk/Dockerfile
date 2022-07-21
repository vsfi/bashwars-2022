FROM alpine

RUN apk add mandoc man-pages coreutils-doc less less-doc \
    python3 curl curl-doc nginx
RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install flask

RUN chmod 700 /root && chmod 700 /usr/bin/python3

COPY webapp.py /root/
COPY entrypoint /bin/entrypoint
COPY banner /bin/banner
COPY nginx.conf /etc/nginx/http.d/default.conf

RUN chmod +x /bin/entrypoint /bin/banner && chmod 600 /etc/nginx/http.d/default.conf

RUN adduser --disabled-password police

WORKDIR /home/police

ENTRYPOINT ["/bin/entrypoint"]