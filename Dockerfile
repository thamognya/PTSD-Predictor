ARG BASE_IMAGE=ubuntu:latest
FROM $BASE_IMAGE

RUN mkdir /ptsd-detector
COPY ./scripts/start.sh /ptsd-detector/start.sh
RUN apt-get update && apt-get install -y \
    python \
    pip \
    git \
    && git --version

ENTRYPOINT ["/ptsd-detector/start.sh"]