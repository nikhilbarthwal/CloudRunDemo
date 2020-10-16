FROM python:3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apk add libreoffice build-base msttcorefonts-installer fontconfig && update-ms-fonts && fc-cache -f

RUN pip install Flask gunicorn requests
COPY . $APP_HOME

# prevent libreoffice from querying ::1 (ipv6 ::1 is rejected until istio 1.1)
RUN mkdir -p /etc/cups && echo "ServerName 127.0.0.1" > /etc/cups/client.conf

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
