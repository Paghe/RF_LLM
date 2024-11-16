FROM python

RUN apt-get update && apt-get install -y libsndfile1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
COPY start.sh /app/

RUN pip install --no-cache-dir -r requirements.txt
COPY  . /app

CMD ["./start.sh"]
