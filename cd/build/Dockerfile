FROM python:3.14.4-slim-trixie

COPY ./v1.4.tar.gz /tmp/v1.4.tar.gz

RUN mkdir /root_dir && \
    tar -xzf /tmp/v1.4.tar.gz -C /root_dir --strip-components=1 && \
    rm /tmp/v1.4.tar.gz

RUN python -m venv /root_dir/venv && \
    /root_dir/venv/bin/pip install -r /root_dir/app/requirements.txt

WORKDIR /root_dir

EXPOSE 8000

CMD [ "venv/bin/python", "main.py"]

## ici un healthcheck (curl ou autre)

