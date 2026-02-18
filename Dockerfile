# استخدام نسخة حديثة ومدعومة في 2026
FROM python:3.9-slim-bookworm

# دمج التحديث والتحميل في أمر واحد لتقليل حجم الطبقات (Layers)
# وتنظيف الكاش فوراً بعد التثبيت
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git curl ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# تحديث pip (النسخة slim يجي معاها pip جاهز)
RUN pip install --no-cache-dir -U pip

WORKDIR /app
COPY . /app

# تثبيت المتطلبات مع منع تخزين الكاش لتوفير المساحة
RUN pip install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "VCPlayBot"]
