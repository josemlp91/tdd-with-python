#
#  Dockerfile para proyectos Django
#

# Base image.
FROM python:3.6

# Create code folder.
RUN mkdir /src

# Set working dir.
WORKDIR /src

# Add python requirements file.
ADD requirements.txt /src/

# Install required programs.
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y \
    gettext \
    vim

RUN apt-get install -y unzip


# Add source code.
ADD . /src/

# Run script file.
CMD ./run.sh