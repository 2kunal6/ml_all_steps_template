FROM python:3.10

COPY . /app/
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run"]

CMD ["python", "src/api_service.py"]
