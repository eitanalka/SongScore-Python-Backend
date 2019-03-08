FROM python:3
WORKDIR /usr/src/server
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN cd fastText && pip install . && cd ..
ENTRYPOINT ["python"]
CMD ["classify_lyrics.py"]