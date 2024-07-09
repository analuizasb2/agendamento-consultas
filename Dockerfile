FROM python:3.13-rc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python init_db.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]