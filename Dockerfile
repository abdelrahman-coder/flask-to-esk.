FROM python:stretch

RUN mkdir app
WORKDIR app
#Copy files
COPY requirements.txt .
COPY main.py .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["gunicorn"  , "-b", ":8080", "main:APP"]
#CMD ["gunicorn", "main:APP","-b", ":8080"]

#CMD ["gunicorn", "app:APP", "-b", "0.0.0.0:8080"]