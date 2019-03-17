FROM python:3.7.2-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
#RUN gunicorn -b :8080 app:APP
CMD ["gunicorn", "app:APP", "-b", "0.0.0.0:8080"]


#ENTRYPOINT ["gunicorn -b :8080 app:APP"]
#ENTRYPOINT ["python", "app.py"]

