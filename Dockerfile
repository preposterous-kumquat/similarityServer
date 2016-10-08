FROM python:2.7.12

RUN pip install -U Flask numpy scipy gensim ez_setup setuptools simserver sqlitedict
ADD . .

EXPOSE 5000

CMD ["python", "server.py"]