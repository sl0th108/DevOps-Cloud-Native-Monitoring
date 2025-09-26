#Python image as base image
FROM python:3.9-buster

#Set the dir in the container
WORKDIR /app

#Copy the requirements file to the directory
COPY requirements.txt .

#Install the required python packages
RUN pip3 install --no-cache-dir -r requirements.txt

#Copy the application to the dir
COPY . .

#Set the enviroment variables for flask
ENV FLASK_RUN_HOST=0.0.0.0

#Expose the port on witch the flask will run
EXPOSE 5000

#Start the flask app when the container is running
CMD ["flask", "run"]
