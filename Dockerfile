# FROM python:3.6-slim-stretch
# FROM nvcr.io/nvidia/pytorch:19.01-py3
FROM nvcr.io/nvidia/pytorch:20.10-py3
LABEL maintainer="liam.chen@bronci.com.tw"

ENV DEBIAN_FRONTEND=noninteractive
# VOLUME ["asr_denoiser"]
RUN mkdir /asr_denoiser
COPY . /asr_denoiser
WORKDIR /asr_denoiser
RUN apt-get update -q -y \
    && apt-get upgrade -q -y \
    # && apt-get install sox -q -y \
    # && apt-get install libsox-fmt-mp3 -q -y \
    && pip install -r requirements.txt \
    && apt-get install libsndfile1 -q -y
    # && apt-get install libportaudio2 -q -y \
    # && apt-get install ffmpeg -q -y