FROM nginx

ARG UID
ARG GID

ENV UID=${UID}
ENV GID=${GID}

# MacOS staff group's gid is 20, so is the dialout group in alpine linux. We're not using it, let's just remove it.
RUN delgroup dialout

#COPY ./server/nginx.conf /etc/nginx/nginx.conf
COPY ./server/nginx.conf /etc/nginx/conf.d/


RUN mkdir -p /var/www/html