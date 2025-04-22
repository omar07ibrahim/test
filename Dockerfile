FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /app/media /app/static \
    && chown -R nobody:nogroup /app/media /app/static \
    && chmod -R 755 /app/media /app/static

USER nobody

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "aerocrm_project.wsgi:application"]


