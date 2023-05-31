## THIẾT KẾ XE TỰ HÀNH SỬ DỤNG RASPBERRY PI 3 MODEL B+ ĐỂ DÒ LINE, NHẬN DIỆN BIỂN BÁO VÀ PHÁT HIỆN VẬT CẢN

### Phần cứng

- 1 Raspberry Pi 3 Model B+
- 1 Camera Raspberry Pi V1 OV5647 5M
- 1 Cảm biến siêu âm HC-SR04
- 1 Module điều khiển L298N
- 3 Pin ncr18650a (3.7V / 4.2V6800mAh) (Không nên dùng pin 2A nguồn yếu xe chạy yếu)
- 4 Động cơ DC giảm tốc
- 1 Khung xe, 4 bánh xe, 1 Gá đỡ Camera
- 1 Pin sạc dự phòng cấp nguồn cho Rasp (Đầu ra tối thiểu 2V)
- 1 Thẻ nhớ SSD 32 GB (Để cài đặt hệ điều hành cho Rasp)
- Dây nối, ốc và các phụ tùng cần thiết

[![SampleModel](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FSampleModel.jpg?alt=media&token=3b75c1f7-c74c-4bf0-baf0-03f14039e586&_gl=1*ba0qs4*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUwOTQ4NC43LjEuMTY4NTUwOTU3Ny4wLjAuMA.. "SampleModel")](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FSampleModel.jpg?alt=media&token=3b75c1f7-c74c-4bf0-baf0-03f14039e586&_gl=1*ba0qs4*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUwOTQ4NC43LjEuMTY4NTUwOTU3Ny4wLjAuMA.. "SampleModel")

[![SampleModel](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FSampleModel2.jpg?alt=media&token=4fb50cf2-63cb-4146-b9bc-a5513eb42c14&_gl=1*1kpj09i*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUwOTQ4NC43LjEuMTY4NTUwOTY2My4wLjAuMA.. "SampleModel")](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FSampleModel2.jpg?alt=media&token=4fb50cf2-63cb-4146-b9bc-a5513eb42c14&_gl=1*1kpj09i*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUwOTQ4NC43LjEuMTY4NTUwOTY2My4wLjAuMA.. "SampleModel")

### Phần mềm

#### Cài đặt các phần mềm cần thiết

- Cài đặt [Raspberry Pi Imager](https://www.raspberrypi.com/software/ "Raspberry Pi Imager")
- Cài đặt [Putty](https://www.putty.org/ "Putty")
- Cài đặt [VNCServer](https://www.realvnc.com/en/connect/download/vnc/ "VNCServer")

#### Cài đặt hệ điều hành cho Rasp

- [Video hướng dẫn](https://www.youtube.com/watch?v=WP0E5Y_nSiM "Video hướng dẫn")

#### Kết nối Rasp qua Laptop với cap Lan

- [Video hướng dẫn](https://www.youtube.com/watch?v=F5OYpPUJiOw "Video hướng dẫn")

#### Kết nối Rasp với Laptop thông qua SSH

- [Video hướng dẫn](https://www.youtube.com/watch?v=wQlwwMq9JXg) (Đảm bảo Rasp và Laptop kết nối cùng một mạng - đây là mạng được setup trong phần Cài đặt hệ điều hành cho Rasp)
- Lưu ý: Sau khi kết nối Rasp qua SSH, gõ lệnh vào putty `vncserver` nó sẽ hiện đúng địa chỉ IP để kết nối với VNCServer

#### Cài đặt các thư viện cần thiết

- OpenCV [Video hướng dẫn](https://www.youtube.com/watch?v=a5lx4dsRfDA "Video hướng dẫn")
- Numpy [Link hướng dẫn](https://phoenixnap.com/kb/install-numpy "Link hướng dẫn")
- Gpiozero [Link hướng dẫn](https://gpiozero.readthedocs.io/en/stable/installing.html "Link hướng dẫn")
- imutils [Link hướng dẫn](https://bobbyhadz.com/blog/python-install-imutils "Link hướng dẫn") (Thư viện hỗ trợ phần Nhận diện biển báo)

#### Hướng dẫn kết nối

- Kết nối Motor với L298N [Link hướng dẫn](https://www.youtube.com/watch?v=bNOlimnWZJE "Link hướng dẫn")
- Kết nối L298N với Rasp [Link hướng dẫn](https://pivietnam.com.vn/huong-dan-cach-dieu-khien-xe-mo-hinh-co-ban-voi-raspberry-pi-pivietnam-com-vn.html?fbclid=IwAR1dyVeLWXpDEAMOchu3Vsk2CwuBvKuCqeAA3Fb_qjjATlPzjIdaFi1m8Y8 "Link hướng dẫn")
  (Mặc định khi mua L298N thì chân ENA và ENB sẽ kết nối với chân nguồn 5V, ta cần gỡ phần nắp kết nối để kết nối chân ENA và ENB với Rasp)
- Kết nối Camera với Rasp [Link hướng dẫn](https://www.youtube.com/watch?v=xA9rzq5_GFM&t=209s&fbclid=IwAR0qvDJrHIOT8dHwlxFJVVh2PR3Dd33ANXNesstNkvv7m0rcZgd3-21GB4U "Link hướng dẫn") (Lưu ý trước khi gắn hoặc tháo camera khỏi Rasp đảm bảo Rasp tắt nguồn)
- Kết nối Sensor với Rasp:
  - Bước 1: Kết nối VCC của HC-SR04 với chân 5V của Raspberry Pi.
  - Bước 2: Kết nối GND của HC-SR04 với chân GND của Raspberry Pi.
  - Bước 3: Kết nối chân Trig của HC-SR04 với một chân GPIO của Raspberry Pi (ví dụ: chân 11 - GPIO17).
  - Bước 4: Kết nối chân Echo của HC-SR04 với một chân GPIO khác của Raspberry Pi (ví dụ: chân 8 - GPIO18).

#### Hướng dẫn chạy

- Test thử motor bằng file **MotorTest.py** (Nếu motor chạy ngược chiều kiểm tra chân phần khai báo, nếu motor không chạy thì có thể motor bị cháy hoặc L298N bị cháy phần cổng kết nối với motor. Ta thử kết nối hai dây nguồn vào pin nếu motor vẫn chạy thì có thể không bị cháy mà là L298N bị cháy, nếu motor chạy yếu thì có thể do nguồn pin, pin có thể hết hoặc bị chết pin :>>)
- Test camera, có trong video hướng dẫn kết nối camera với Rasp
- Test cảm biến, ta chạy file sensor.py, thử test khoảng cách từ cảm biến tới vật cản bằng cách in thông số khoảng cách ra (Thường thì vật cản để càng xa thì thông số in ra càng lớn nếu thông số không theo đúng kết quả mong đợi, kiểm tra lại chân kết nối sensor với Rasp)
- Đối với Nhận diện line: Ta chạy file **LineDetection.py**, các thông số xung điều chỉnh cho phù hợp với mức nguồn hiện tại (Nếu điều chỉnh phù hợp xe chạy không bị giật).
  - Biến contour_area để xác định độ lớn vùng đen để có thể dừng động cơ, ta nên in giá trị biến này để test khi nào nên dừng nó có thể phụ thuộc vào độ cao của camera và độ lớn của vùng đen
  - Ghi nhận giá trị cx phù hợp để có thể cua phải, cua trái (Khi giá trị không phù hợp xe có thể không cua phải, cua trái được)
- Đối với Nhận diện line kết với vật cản: Ta chạy file **LineDectection_Sensor.py**. Khi xe gặp vật cản thì sẽ dừng.
- Đối với Nhận diện biển báo: Ta chạy file **SignRecognition.py**. Hình ảnh biến báo test ở thư mục **ImageForSignRecognition**

#### Hình ảnh demo

- Có thể xem video demo tại thư mục **VideoForDemo**
- Nhận diện line
  [![](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FDemo1.jpg?alt=media&token=2868ab37-4900-46ff-9c4a-465bdd130e45&_gl=1*f2gxj3*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUxMzc3My44LjEuMTY4NTUxMzk1OC4wLjAuMA..)](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FDemo1.jpg?alt=media&token=2868ab37-4900-46ff-9c4a-465bdd130e45&_gl=1*f2gxj3*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUxMzc3My44LjEuMTY4NTUxMzk1OC4wLjAuMA..)
- Nhận diện biển báo
  [![](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FDemo2.jpg?alt=media&token=dc00dc69-9c94-4e52-9422-279cd73e1428&_gl=1*qq3k0s*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUxMzc3My44LjEuMTY4NTUxNDEzOS4wLjAuMA..)](https://firebasestorage.googleapis.com/v0/b/can-app-image.appspot.com/o/files%2FDemo2.jpg?alt=media&token=dc00dc69-9c94-4e52-9422-279cd73e1428&_gl=1*qq3k0s*_ga*MTM3MTk0MTM3NC4xNjgyNTI0MzUw*_ga_CW55HF8NVT*MTY4NTUxMzc3My44LjEuMTY4NTUxNDEzOS4wLjAuMA..)
