# 1. Chọn image base Python 3.11
FROM python:3.11-slim

# 2. Thiết lập working directory
WORKDIR /app

# 3. Cài các thư viện trực tiếp
RUN pip install --no-cache-dir \
    flask \
    flask-cors \
    pillow \
    numpy \
    tensorflow-cpu==2.12.0 \
    f

# 4. Copy toàn bộ source code vào container
COPY . .

# 5. Expose port Flask sử dụng
EXPOSE 5000

# 6. Chạy app
CMD ["python", "app.py"]
