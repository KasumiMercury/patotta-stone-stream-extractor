FROM python:3.12

RUN apt-get update && \
    pip install --upgrade pip && \
    apt-get install -y bash

# Install required packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspace

EXPOSE 8080
