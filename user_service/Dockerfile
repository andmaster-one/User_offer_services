# pull official base image
FROM python

# set work directory
WORKDIR /code/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install --no-cache-dir -r req.txt

# copy project
COPY . .
