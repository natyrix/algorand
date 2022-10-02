FROM python:3.10


# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py migrate
# Copy app code and set working directory
COPY . .
WORKDIR /

# Run
CMD [ "python" , "manage.py", 'runserver']