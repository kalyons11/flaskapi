# Set up python
FROM alpine:3.6

# Update packages
RUN apk add --update python py-pip

# Handle pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r src/requirements.txt

# Handle files
COPY flaskapi /src/flaskapi
COPY run.py /src

# Handle env vars
# 

# Run
CMD python src/run.py