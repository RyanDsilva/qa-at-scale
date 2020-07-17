FROM deepset/haystack-cpu:latest

WORKDIR /home/user

COPY . /home/user/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "main:app" "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]