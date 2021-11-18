FROM python:3.9.7

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ejemplo_notebook_descargado.ipynb ejemplo_notebook_descargado.ipynb

EXPOSE 5002

CMD ["python","ejemplo_notebook_descargado.ipynb"]