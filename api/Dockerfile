FROM python:3.8.12-buster
LABEL maintainer="Tanaka Kazuki"
LABEL discription = "December hackson backend api"

WORKDIR /app
RUN pip install flask psycopg2-binary waitress Flask-Login

COPY ./main.py /app
COPY ./dbaccess.py /app

CMD ["python","main.py"]