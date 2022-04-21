FROM amazon/aws-lambda-python:latest

LABEL maintainer="Wesley Cheek"
# Installs python, removes cache file to make things smaller
RUN yum update -y && \
    yum install -y python3 python3-dev python3-pip gcc && \
    rm -Rf /var/cache/yum
# Moves requirements.txt file into the container
COPY requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt

# Points to the handler function of your lambda function
CMD ["example_docker_lambda.handler"]