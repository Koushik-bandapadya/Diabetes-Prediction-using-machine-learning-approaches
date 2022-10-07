FROM python:3.9

# Create app directory
WORKDIR /app

# Install app dependencies
#COPY requirements.txt ./

RUN pip install "pymongo[srv]" flask numpy sklearn 

# Bundle app source
COPY . .
ENV FLASK_APP=hello.py

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
