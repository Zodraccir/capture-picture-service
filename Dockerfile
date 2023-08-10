FROM --platform=linux/amd64 ubuntu:22.04 AS builder

RUN apt-get update -y && \
    apt-get install -y python3.10 python3-pip

RUN pip install --upgrade pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgl1  -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /services/requirements.txt

WORKDIR /services

RUN pip install -r requirements.txt

COPY . /services

ENTRYPOINT [ "python3" ]

CMD [ "service.py" ]