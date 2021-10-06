FROM registry.cloud-technology.io/automata/.IO/alpine:latest

ENV NGINX_VERSION="1.19.0"

ENV Y="\\n\\33[33m"
ENV X="\\33[0m\\n"

EXPOSE 80 443

RUN echo -e "${Y} - Installing System Dependencies ${X}" \
    && apk add --no-cache   \
        apache2-utils       \
        libressl3.1-libssl  \
        nano                \
        openssl             \
        php7                \
        php7-fileinfo       \
        php7-fpm            \
        php7-json           \
        php7-mbstring       \
        php7-openssl        \
        php7-session        \
        php7-simplexml      \
        php7-xml            \
        php7-xmlwriter      \
        php7-zlib

RUN echo -e "${Y} - Installing Additional Packages ${X}" \
    && apk add --no-cache   \
        fontconfig          \
        memcached           \
        netcat-openbsd

RUN echo -e "${Y} - Installing NGINX Module Packages ${X}" \
    && apk add --no-cache   \
        linux-headers       \
        openssl-dev         \
        build-base          \
        libxml2             \
        libxslt             \
        perl                \
        pcre-dev            \
        zlib-dev            \
            tzdata

RUN echo -e "${Y} - Compiling NGINX ${X}" \
    && wget "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" \
        --no-verbose \
            --show-progress \
                && tar zxvf "nginx-${NGINX_VERSION}.tar.gz" \
        && cd nginx-${NGINX_VERSION} \
        && ./configure --prefix=/etc/nginx \
            --sbin-path=/usr/sbin/nginx \
            --modules-path=/usr/lib/nginx/modules \
            --conf-path=/etc/nginx/nginx.conf \
            --error-log-path=/var/log/nginx/error.log \
            --pid-path=/var/run/nginx.pid \
            --lock-path=/var/run/nginx.lock \
            --user=nginx \
            --group=nginx \
            --with-select_module \
            --with-poll_module \
            --with-threads \
            --with-file-aio \
            --with-http_ssl_module \
            --with-http_v2_module \
            --with-http_realip_module \
            --with-http_addition_module \
            --with-http_sub_module \
            --with-http_dav_module \
            --with-http_flv_module \
            --with-http_mp4_module \
            --with-http_gunzip_module \
            --with-http_gzip_static_module \
            --with-http_auth_request_module \
            --with-http_random_index_module \
            --with-http_secure_link_module \
            --with-http_degradation_module \
            --with-http_slice_module \
            --with-http_stub_status_module \
            --http-log-path=/var/log/nginx/access.log \
            --http-client-body-temp-path=/var/cache/nginx/client_temp \
            --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
            --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
            --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
            --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
            --with-stream=dynamic \
            --with-stream_ssl_module \
            --with-stream_realip_module \
            --with-stream_ssl_preread_module \
            --with-compat \
            --with-pcre \
            --with-pcre-jit \
            --with-openssl-opt=no-nextprotoneg \
                --with-debug \
        && make && make install

RUN echo -e "${Y} - Creating NGINX Directories ${X}" \
    && mkdir -p /etc/nginx/conf.d \
        /etc/nginx/snippets \
            /etc/nginx/sites-available \
                /etc/nginx/sites-enabled

RUN echo -e "${Y} - Creating NGINX Caches ${X}"     \
    && ln -s /usr/lib/nginx/modules /etc/nginx/modules  \
        && mkdir -p /var/cache/nginx/client_temp        \
            /var/cache/nginx/fastcgi_temp               \
                /var/cache/nginx/proxy_temp             \
                    /var/cache/nginx/scgi_temp          \
                        /var/cache/nginx/uwsgi_temp

RUN echo -e "${Y} - Creating HTML Directories ${X}"     \
    && mkdir -p /var/www/html \
    && mkdir -p /usr/share/nginx/html \
        && cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup

RUN echo -e "${Y} - Creating NGINX Users ${X}" \
    && addgroup -S nginx \
        && adduser -D -S -h \
            /var/cache/nginx \
                -s /sbin/nologin -G nginx nginx \
        && cd .. && rm -r -f ./nginx-${NGINX_VERSION} \
            && rm -rf /var/cache/apk/*

RUN echo -e "${Y} - Creating Fast-CGI Configuration ${X}" \
    && { \
        echo 'fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;'   ; \
	} >> /etc/nginx/fastcgi_params

RUN echo -e "${Y} - Cleaning ${X}" \
    && rm -r -f "/nginx-${NGINX_VERSION}.tar.gz" \
    && rm -r -f "/var/cache/apk/*"

VOLUME [ "/var/cache/nginx", "/config" ]
