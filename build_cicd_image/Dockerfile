ARG CICD_IMAGE_TAG=3.14.4-slim-trixie
ARG GECKODRIVER_VERSION=v0.36.0-linux64

FROM python:${CICD_IMAGE_TAG}

COPY geckodriver-${GECKODRIVER_VERSION}.tar.gz /tmp/
RUN tar -xzf /tmp/geckodriver-${GECKODRIVER_VERSION}.tar.gz -C /usr/local/bin/ && \
    rm /tmp/geckodriver-${GECKODRIVER_VERSION}.tar.gz && \
    chmod +x /usr/local/bin/geckodriver