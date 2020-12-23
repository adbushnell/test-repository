FROM python:3.7.2-slim
RUN mkdir /code
COPY requirements.txt /code/
COPY saved_model /code/
COPY pred_api.py /code/
RUN pip install -r /code/requirements.txt
EXPOSE 5000
CMD ["python","/code/pred_api.py"]

