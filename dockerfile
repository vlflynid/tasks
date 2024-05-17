FROM python:3.12

COPY requirements.txt requirements.txt

RUN apt update -y
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

WORKDIR /app

COPY .. /app/

EXPOSE 5000

ENTRYPOINT [ "python", "main.py" ]
