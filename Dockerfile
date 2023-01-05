FROM python:3.10-slim-buster
COPY requirements.txt requirements.txt
WORKDIR /src

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cryptography
CMD [ "python", "main.py"]
