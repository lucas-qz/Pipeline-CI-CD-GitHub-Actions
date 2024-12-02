FROM python

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
 
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
