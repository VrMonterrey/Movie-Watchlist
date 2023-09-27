FROM python:3.11-slim-bullseye
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY . /app/
ENV FLASK_ENV=production
#EXPOSE 5000
#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"] 