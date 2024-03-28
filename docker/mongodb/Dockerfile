FROM mongo:7.0.4

MAINTAINER jinsoo.kim <jjambbongjoa@gmail.com>

# -----------------------------------------------------------------------------
### SERVER COMMON Configuration
# -----------------------------------------------------------------------------
# 서버 언어를 한국어로 설정
ENV LANG="ko_KR.UTF-8"

# 서버 시간대를 서울로 변경
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
  echo "Asia/Seoul" > /etc/timezone
# -----------------------------------------------------------------------------
ADD mongod.conf /etc/mongod.conf

CMD ["mongod", "-f", "/etc/mongod.conf"]