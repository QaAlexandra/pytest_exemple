FROM python:3.8-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./src /code/src
COPY ./tests /code/tests

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "50700"]
