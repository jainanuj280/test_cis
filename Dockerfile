# base image to be used
FROM python

# create root directory for our project in the container
#RUN mkdir /code

# Set the working directory to the created dir
WORKDIR /code

# add the requiremnets file to the working dir
COPY requirements.txt /code/

#instal the requirements (install before adding rest of code to avoid rerunning this at every code change-built in layers)
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /music_service
COPY . /code/

#set environments to be used
#set environments to be used
ENV AUTHOR="Anuj"

EXPOSE 8000

#run the service docker app
CMD python manage.py runserver 0.0.0.0:8000
