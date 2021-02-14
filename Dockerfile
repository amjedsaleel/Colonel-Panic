FROM python:3.8.3-alpine
# Setting work dir
WORKDIR /code 

# We dont want ypc files
ENV PYTHONDONTWRITEBYTECODE 1
# No stdouts from Django
# ENV PYTHONUNBUFFERED 1

# Installing pip and its requirments 
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Copying our project
COPY . /code/

