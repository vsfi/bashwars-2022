FROM alpine

RUN apk add nginx curl vim  mandoc man-pages coreutils-doc less less-doc curl-doc

COPY nginx.conf /etc/nginx/http.d/default.conf
COPY banner /bin/banner
COPY entrypoint /bin/entrypoint
COPY add_hosts /add_hosts
COPY logs /var/logs

RUN chmod +x /bin/entrypoint /bin/banner /add_hosts && chmod 600 /etc/nginx/http.d/default.conf
RUN adduser --disabled-password billy

COPY domains /home/billy/domains

WORKDIR /home/billy
ENTRYPOINT ["/bin/entrypoint"]