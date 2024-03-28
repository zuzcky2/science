FROM continuumio/miniconda3:24.1.2-0
#continuumio/miniconda3-alpine
MAINTAINER Jinsoo Kim <jjambbongjoa@gmail.com>

USER root
# -----------------------------------------------------------------------------
### SERVER COMMON Configuration
# -----------------------------------------------------------------------------
# 서버 언어를 한국어로 설정
ENV LANG="ko_KR.UTF-8"

# 서버 시간대를 서울 시간대로 설정
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
  echo "Asia/Seoul" > /etc/timezone
# -----------------------------------------------------------------------------
### Anaconda Configuration
# -----------------------------------------------------------------------------

# 필요한 패키지를 설치합니다.
RUN conda install -c conda-forge jupyter jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user

RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry in the new environment
RUN python -m pip install poetry

RUN poetry config warnings.export false

COPY nbconfig /root/.jupyter/nbconfig
ADD ../jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
