FROM python:3
WORKDIR /usr/src/server
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]