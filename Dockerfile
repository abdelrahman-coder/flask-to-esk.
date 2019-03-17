FROM python:3.7.2-slim

RUN mkdir app
WORKDIR app
#Copy files
COPY requirements.txt .
COPY main.py .
RUN ls
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["gunicorn", "main:APP","-b", ":8080"]



#CMD ["gunicorn", "app:APP", "-b", "0.0.0.0:8080"]