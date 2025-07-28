FROM python:3.9-slim

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD [ "fastapi", "run", "src/main.py", "--port", "8000" ]