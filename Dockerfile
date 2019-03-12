FROM python:3
WORKDIR /usr/src/server
ADD ./server/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD ./server/fastText ./fastText
RUN cd fastText && pip install . && cd ..
COPY ./server .
ENTRYPOINT ["python"]
CMD ["app.py"]