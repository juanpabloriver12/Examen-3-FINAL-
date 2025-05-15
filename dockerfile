FROM python:3.10-slim
 
WORKDIR /app

COPY main.py /app

RUN pip install flask
 
EXPOSE 8005
 
CMD ["python", "main.py"]
