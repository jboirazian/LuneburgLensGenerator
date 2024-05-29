FROM pymesh/pymesh:py3.7-slim
RUN pip install click
WORKDIR /app
COPY Luneburg.py ./Luneburg.py
ADD modules /
CMD ["python3","-u","Luneburg.py"]