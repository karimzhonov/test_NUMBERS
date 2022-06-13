FROM python:3.9

RUN apt update && apt install postgresql gunicorn -y

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=project.settings

COPY . .

ENV DEBUG=1
ENV SECRET_KEY='django-insecure-+j239v@(8nr61yt5y6==)kykn9)8vb=+=d8@%)@pv6l6g-=$0m'
ENV DATABASE_URL='postgres://amgylpdxwcbsvn:0083b17961ab904d1b43d250d746c5129ca32cad497bcb5bf215cf3b7563150f@ec2-34-246-227-219.eu-west-1.compute.amazonaws.com:5432/d1m2khqsouov6a'
ENV GOOGLE_SHEET_ID='1_qARCaIOTcXhny9NXHHkdAm1-OFjlfDeZGrMoQFRuQM'

RUN pip install -r requirements.txt
RUN python manage.py collectstatic