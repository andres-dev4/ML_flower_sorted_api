
FROM python:3.10.5-slim-buster


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5001


CMD ["tail", "-f" ,"/dev/null"]
