FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install cv2
CMD python app.py