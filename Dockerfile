FROM python:3.12

RUN apt-get update && \
    pip install --upgrade pip

# Install required packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspace
