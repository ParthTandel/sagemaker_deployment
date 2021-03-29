# this is a very simple Docker file
# task in this file
# 1) Pull ubuntu18.04 base image.
# 2) Install required packages like python, python-pip and other certificates.
# 3) After installing python3 create a symb link to python.
# 4) Copy requirements.txt file from the project.
# 5) Install python related library using the requirement.txt file.
# 6) copy your code to the /opt/program/ directory of the container.
# 7) Set python path to /opt/program/ where the files from the estimator will be copied to
# 8) Set the working directory.
# thats it. I know this looks like a lot but once you get a hang of it, it is very simple.
# also this file is driectly from the amazon shell code with some small changes.

# Build an image that can do training and inference in SageMaker
# This is a Python 3 image that uses the nginx, gunicorn, flask stack
# for serving inferences in a stable way.

FROM ubuntu:18.04


# install python, pip and other required tools
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3-pip \
         python3-setuptools \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# create symblink for python and pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

# Here we get all python packages.
COPY requirement.txt .
RUN pip --no-cache-dir install -r requirement.txt

RUN python -c "import nltk;nltk.download('stopwords')"


# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY estimator /opt/program
WORKDIR /opt/program