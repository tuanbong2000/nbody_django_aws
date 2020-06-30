# Base Image
#FROM linuxmintd/mint19-amd64:latest
From python:3.8
# create and set working directory
RUN mkdir /nbody_django
WORKDIR /nbody_django

# Add current directory code to working directory
ADD . /nbody_django/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888
# ENV DEBUG=1
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential g++\ 
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        ffmpeg\
        vim\
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv
# install nbody_sh1.c
RUN g++ -o nbody_sh1 nbody_sh1.C

# Install project dependencies
RUN pipenv install --skip-lock --system --dev
#RUN pip install -r requirements.txt

EXPOSE 8000
CMD gunicorn nbody_django.wsgi:application --bind 0.0.0.0:$PORT
#CMD python manage.py runserver --noreload --nothreading 127.0.0.1:$PORT