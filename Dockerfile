FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY migrations migrations
COPY run.py src/app/_init_.py src/app/budget_categories.py src/app/main.py src/app/notion_trans.py src/app/transactions.py ./

EXPOSE 8000
CMD waitress-serve --listen=0.0.0.0:8000 --call "run:create_app"
