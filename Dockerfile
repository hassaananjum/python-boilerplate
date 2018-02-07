FROM python:3
EXPOSE 4000
ADD . ~
WORKDIR ~
RUN pip install -r Requirements.txt
CMD [ "python", "main.py" ]