FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x scripts/build_cpp.sh && ./scripts/build_cpp.sh

CMD ["python", "bot.py"]
