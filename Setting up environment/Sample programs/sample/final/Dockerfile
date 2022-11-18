FROM python:3.6.5-alpine
WORKDIR /app
ADD . /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
