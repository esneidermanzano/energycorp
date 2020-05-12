FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .
COPY ./src .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
	&& pip3 install --no-cache-dir --force-reinstall cffi \
	&& pip3 install --no-cache-dir cairocffi \
	&& pip3 install -r requirements.txt \
	&& apk del .build-deps


RUN adduser -D myuser
USER myuser

#If you wanna test with compose, enable the follow lines

#EXPOSE 8000

#ENTRYPOINT ["python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]
