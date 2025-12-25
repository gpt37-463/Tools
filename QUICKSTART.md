# Hướng dẫn Nhanh / Quick Start Guide

## Giới thiệu
Công cụ kiểm tra mạng giúp bạn nhanh chóng đánh giá chất lượng kết nối mạng của mình.

## Sử dụng Nhanh

### 1. Kiểm tra đầy đủ (khuyến nghị)
```bash
python3 network_monitor.py
```

Chương trình sẽ tự động:
- ✓ Kiểm tra cấu hình mạng của bạn
- ✓ Đo tín hiệu WiFi (nếu có)
- ✓ Kiểm tra tốc độ mạng
- ✓ Xác định trạng thái tường lửa
- ✓ Tạo báo cáo tổng hợp với điểm số

### 2. Xem ví dụ sử dụng
```bash
python3 demo.py
```

### 3. Chạy kiểm tra tự động
```bash
python3 test_network_monitor.py
```

## Hiểu Kết Quả

### Tín hiệu WiFi
- **A (Xuất sắc)**: 80-100% - Tín hiệu rất mạnh
- **B (Tốt)**: 60-79% - Tín hiệu ổn định
- **C (Trung bình)**: 40-59% - Có thể bị gián đoạn
- **D (Yếu)**: 20-39% - Thường xuyên mất kết nối
- **F (Rất yếu)**: 0-19% - Không đủ để sử dụng

### Tốc độ Mạng (0-100 điểm)
- **90-100**: Xuất sắc (A) - Streaming 4K, gaming mượt mà
- **75-89**: Tốt (B) - Streaming HD, video call tốt
- **60-74**: Trung bình (C) - Duyệt web, email
- **40-59**: Yếu (D) - Chậm, có thể bị lag
- **0-39**: Rất yếu (F) - Cần khắc phục

## Các Trường Hợp Thường Gặp

### Không có quyền kiểm tra tường lửa?
Chạy với quyền administrator:
```bash
# Linux/macOS
sudo python3 network_monitor.py

# Windows (Run PowerShell as Administrator)
python network_monitor.py
```

### Không kiểm tra được WiFi?
- Trên Linux: Cài đặt `wireless-tools` hoặc `network-manager`
  ```bash
  sudo apt-get install wireless-tools
  # hoặc
  sudo apt-get install network-manager
  ```

### Không kiểm tra được tốc độ?
- Kiểm tra kết nối internet
- Tường lửa có thể đang chặn - thử tắt tạm thời

## Tích Hợp Vào Code Của Bạn

```python
from network_monitor import NetworkMonitor

# Tạo instance
monitor = NetworkMonitor()

# Chạy kiểm tra cụ thể
config = monitor.check_network_config()
wifi = monitor.check_wifi_signal()
speed = monitor.test_network_speed()

# Hoặc chạy tất cả
results = monitor.run_all_checks()

# Truy cập kết quả
if 'wifi' in results and results['wifi']:
    print(f"WiFi: {results['wifi']['ssid']}")
    print(f"Signal: {results['wifi']['signal_strength']}%")
```

## Lưu ý Quan Trọng

1. **Internet**: Một số tính năng cần kết nối internet
2. **Quyền truy cập**: Kiểm tra tường lửa cần quyền administrator
3. **WiFi**: Chỉ hoạt động khi máy đang kết nối WiFi
4. **Tốc độ**: Kết quả có thể khác nhau tùy thời điểm

## Khắc Phục Sự Cố

### Lỗi: "Permission denied"
→ Chạy với `sudo` (Linux/Mac) hoặc Administrator (Windows)

### Lỗi: "No module named 'network_monitor'"
→ Đảm bảo bạn đang ở thư mục chứa file `network_monitor.py`

### Lỗi: "Command not found"
→ Cài đặt Python 3: `sudo apt-get install python3`

## Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra log lỗi được hiển thị
2. Đảm bảo Python 3.6+ đã cài đặt
3. Kiểm tra quyền truy cập file
4. Tạo issue trên GitHub

## Tips và Tricks

💡 **Chạy định kỳ**: Tạo cron job để giám sát mạng tự động
```bash
# Chạy mỗi giờ
0 * * * * cd /path/to/Tools && python3 network_monitor.py >> /var/log/network_monitor.log
```

💡 **So sánh kết quả**: Lưu output để so sánh theo thời gian
```bash
python3 network_monitor.py > network_report_$(date +%Y%m%d).txt
```

💡 **Kiểm tra nhanh**: Chỉ chạy một phần
```python
from network_monitor import NetworkMonitor
monitor = NetworkMonitor()
monitor.check_wifi_signal()  # Chỉ kiểm tra WiFi
```
