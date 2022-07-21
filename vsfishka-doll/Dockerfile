FROM alpine

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN apk add vim vim-doc
COPY vimrc /etc/vim/vimrc
RUN adduser -D uganda
COPY access.1.log.gz /home/uganda/access.1.log.gz
RUN chown -R root:root /home
RUN chmod -R 755 /home
RUN chmod -R 400 /tmp
USER uganda
CMD trap : INT ; yes "You shall not pass VSFI wall!!" || echo -e "\n\nWoohoo, you've done it!" ; read -p "Press any key for the next task" ; vim ; echo -e "\n\nHooray!" ; cd ; read -p "Press any key for the next task" ; echo -e "\n\nШтош, бороться с yes научились, из вима вышли, пришло время для настоящего классического таска Bashwars на божественные однострочники:\n\nВ вашей домашней директории лежит логфайл веб-сервера. Выведите топ-5 популярных URL с количеством обращений к ним." ; sh
