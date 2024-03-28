FROM nginx:1.25.3

MAINTAINER jinsoo.kim <jjambbongjoa@gmail.com>

# -----------------------------------------------------------------------------
### SERVER COMMON Configuration
# -----------------------------------------------------------------------------
# 서버 언어를 한국어로 설정
ENV LANG="ko_KR.UTF-8"

# 서버 시간대를 서울 시간대로 설정
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
  echo "Asia/Seoul" > /etc/timezone
# -----------------------------------------------------------------------------
### NGINX Configuration
# -----------------------------------------------------------------------------

RUN rm -f /etc/nginx/conf.d/*
RUN mkdir /etc/nginx/sites-enabled/
RUN rm -f /etc/nginx/sites-enabled/default

COPY nginx.conf        /etc/nginx/
COPY common            /etc/nginx/common
COPY sites-available   /etc/nginx/sites-available
COPY sites-enabled/http.conf   /etc/nginx/sites-enabled/http.conf
COPY upstream.conf /etc/nginx/conf.d/

WORKDIR /etc/nginx

CMD ['nginx']
