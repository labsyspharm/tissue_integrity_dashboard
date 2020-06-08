FROM python:3.8
WORKDIR /home
COPY requirements.txt /home/requirements.txt
RUN pip install -r ./requirements.txt
CMD ["panel", "serve", "code/app.ipynb"]