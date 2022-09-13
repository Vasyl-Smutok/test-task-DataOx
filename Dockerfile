FROM python:3.10.4-slim-buster

LABEL maintainer="vasyl.smutok@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "db_manager.py"]
CMD ["python", "parse.py"]