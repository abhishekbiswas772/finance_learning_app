FROM python:3.9-alpine AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache \
    postgresql-libs

FROM base AS build
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps
COPY . /app/
FROM base AS release
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /app/ /app/
WORKDIR /app
EXPOSE 80
CMD ["python", "-m", "flask", "db", "init"]
CMD ["python", "-m", "flask", "db", "migrate"]
CMD ["python", "-m", "flask", "db", "upgrade"]
CMD ["python", "app.py"]