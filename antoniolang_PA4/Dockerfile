FROM python:latest
WORKDIR /home/tonycs/CS446_PA4/antoniolang_PA4
COPY pythonCode2.py pythonCode2.py
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python", "./pythonCode2.py"]