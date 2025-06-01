# Animal Classifier

## 1. Thành viên
- Đặng Đức Duy – 23020347
## 2. Mô tả dự án
Hệ thống nhận diện loài động vật từ hình ảnh trong thời gian thực.  
- Người dùng upload ảnh động vật lên trang web (Frontend).  
- Backend (Flask + MobileNetV2) nhận ảnh, xử lý và trả về top-3 nhãn (label + score) dưới dạng JSON.  
- Frontend hiển thị kết quả ngay sau khi nhận phản hồi.
### 2.1. Các thành phần của dự án

Frontend: HTML, CSS, JavaScript thuần, được triển khai trên server Nginx.

Backend: Python (Flask), MobileNetV2 (TensorFlow), PIL để xử lý ảnh.

Docker và Docker Compose: Đóng gói và triển khai toàn bộ hệ thống dưới dạng các container riêng biệt (frontend, backend và database MySQL).

Database: MySQL dùng để lưu trữ kết quả nhận diện (tùy chọn, chưa kết nối trong bản demo này).

## 3. Mục tiêu thực hiện

Tìm hiểu và triển khai mô hình AI để nhận diện hình ảnh.

Tạo một ứng dụng đầy đủ với giao diện dễ dùng.

Triển khai ứng dụng bằng Docker, Docker Compose và lưu trữ image lên Docker Hub.

## 4. Liên kết Docker Hub

Backend: dduy071/animal-backend

Frontend: dduy071/animal-frontend

## 5. Cấu trúc thư mục dự án

animal-classifier/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md

## 6. Hướng dẫn chạy dự án

### 6.1. Yêu cầu trước khi chạy

Máy tính cài đặt Docker và Docker Compose.

### 6.2. Chạy dự án

Bước 1: Clone dự án từ GitHub

git clone https://github.com/dduy071/animal-classifier.git
cd animal-classifier

Bước 2: Khởi động hệ thống

docker-compose up --build -d

Bước 3: Kiểm tra các container đang chạy

docker-compose ps

Bước 4: Truy cập ứng dụng

Truy cập địa chỉ http://localhost:3000.

Chọn file ảnh động vật và nhấn nút Classify để nhận kết quả.

Bước 5: Kiểm thử Backend riêng biệt (tùy chọn)

curl -F "image=@đường_dẫn_đến_ảnh.jpg" http://localhost:5000/classify

### 6.3. Dừng và xóa các container

docker-compose down

## 7. Một số lỗi thường gặp và cách khắc phục

Frontend không kết nối được Backend:

Kiểm tra cấu hình CORS trong Backend.

Đảm bảo URL gọi API là http://localhost:5000/classify.

Backend thiếu thư viện:

Đảm bảo đã cài các thư viện: flask, flask-cors, pillow, tensorflow-cpu.

Cổng bị chiếm dụng:

Thay đổi cổng trong docker-compose.yml nếu cổng mặc định đã bị chiếm.

## 8. Tổng kết

Hệ thống hoàn chỉnh với đầy đủ các thành phần frontend, backend, Docker hóa và triển khai dễ dàng thông qua Docker Compose.

Đảm bảo giáo viên hoặc người dùng khác chỉ cần chạy lệnh:

docker-compose up -d

là có thể sử dụng và kiểm thử hệ thống nhanh chóng.

## 9. Đánh giá tổng quan

Ưu điểm:

Giao diện đơn giản, dễ sử dụng.

Triển khai dễ dàng, gọn nhẹ nhờ Docker.

Kết quả nhận diện nhanh và chính xác.

Hạn chế:

Hiện tại chưa kết nối database MySQL để lưu trữ log.

Cần thêm các tính năng mở rộng khác như đăng nhập, quản lý lịch sử nhận diện...


