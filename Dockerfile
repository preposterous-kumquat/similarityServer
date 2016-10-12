FROM tiangolo/uwsgi-nginx-flask

RUN pip install -U Flask numpy scipy gensim ez_setup setuptools simserver sqlitedict
ADD . .

RUN curl --data '' http://0.0.0.0:5000/train

EXPOSE 5000

CMD ["python", "server.py"]