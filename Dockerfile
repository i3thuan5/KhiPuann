FROM python:3.8-bullseye

WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt

ENV DJANGO_SETTINGS_MODULE=autuan.settings-tsiunnsuann
COPY khipuann/ .

EXPOSE 8000
CMD python manage.py collectstatic --noinput --clear && gunicorn \
  -b 0.0.0.0:8000 \
  --workers 2 --threads 4 \
  --log-level debug \
  khipuann.wsgi
