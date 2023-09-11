FROM python:3.10.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

RUN python3 manage.py loaddata users.yaml  || true

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
