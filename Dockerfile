From python:3.6

WORKDIR /dapp

COPY requirements.txt /dapp/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /dapp

EXPOSE 8080

CMD python3 manage.py runserver 0.0.0.0:8080