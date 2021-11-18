FROM python:3.9.7

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py

EXPOSE 5001

CMD ["python","main.py"]