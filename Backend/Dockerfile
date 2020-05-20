FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .
COPY ./src .

RUN pip install -r requirements.txt
RUN useradd -s /bin/bash myuser
USER myuser

RUN sudo apt-get install ttf-mscorefonts-installer 
RUN sudo fc-cache


#If you wanna test with compose, enable the follow lines

#EXPOSE 8000

#ENTRYPOINT ["python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]
