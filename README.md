# Network Monitoring Tool / Công cụ Kiểm tra Mạng

Chương trình kiểm tra các kết nối mạng nội bộ, tốc độ truyền, tín hiệu WiFi, cấu hình và tường lửa.

## Tính năng / Features

✓ **Kiểm tra cấu hình mạng** - Network configuration check
- Hiển thị hostname và địa chỉ IP
- Kiểm tra kết nối internet
- Liệt kê các interface mạng

✓ **Kiểm tra tín hiệu WiFi** - WiFi signal monitoring
- Hiển thị SSID đang kết nối
- Đo cường độ tín hiệu WiFi
- Chấm điểm chất lượng tín hiệu (A-F)

✓ **Kiểm tra tốc độ mạng** - Network speed testing
- Đo độ trễ (ping/latency)
- Kiểm tra tốc độ download
- Chấm điểm tốc độ mạng tổng thể (0-100)

✓ **Kiểm tra tường lửa** - Firewall status
- Phát hiện và hiển thị trạng thái tường lửa
- Hỗ trợ Windows, Linux, macOS

## Yêu cầu hệ thống / Requirements

- Python 3.6 trở lên
- Hệ điều hành: Windows, Linux, hoặc macOS
- Quyền administrator/sudo để kiểm tra tường lửa (tùy chọn)

## Cài đặt / Installation

```bash
# Clone repository
git clone https://github.com/gpt37-463/Tools.git
cd Tools

# Không cần cài đặt thêm dependencies - chỉ cần Python 3
```

## Sử dụng / Usage

### Chạy chương trình cơ bản:

```bash
python3 network_monitor.py
```

### Chạy với quyền administrator (để kiểm tra tường lửa):

**Windows (PowerShell as Administrator):**
```powershell
python network_monitor.py
```

**Linux/macOS:**
```bash
sudo python3 network_monitor.py
```

## Ví dụ kết quả / Example Output

```
============================================================
CHƯƠNG TRÌNH KIỂM TRA MẠNG
Network Monitoring Tool
============================================================
Bắt đầu kiểm tra mạng...
============================================================

=== KIỂM TRA CẤU HÌNH MẠNG ===
Hostname: my-computer
Địa chỉ IP: 192.168.1.100
Kết nối Internet: Có

=== KIỂM TRA TÍN HIỆU WIFI ===
SSID: MyWiFiNetwork
Cường độ tín hiệu: 85%
Đánh giá tín hiệu: Xuất sắc (A)

=== KIỂM TRA TỐC ĐỘ MẠNG ===
Kiểm tra độ trễ (ping)...
Độ trễ trung bình: 15ms

Kiểm tra tốc độ download...
Tốc độ download: 45.2 Mbps

Đánh giá tốc độ mạng: Tốt (B) - 85/100 điểm

=== KIỂM TRA TƯỜNG LỬA ===
Tường lửa: BẬT

============================================================
BÁO CÁO TỔNG HỢP KIỂM TRA MẠNG
============================================================
```

## Hệ thống chấm điểm / Grading System

### Tín hiệu WiFi / WiFi Signal:
- **A (Xuất sắc)**: 80-100%
- **B (Tốt)**: 60-79%
- **C (Trung bình)**: 40-59%
- **D (Yếu)**: 20-39%
- **F (Rất yếu)**: 0-19%

### Tốc độ mạng / Network Speed (0-100 điểm):
- **Độ trễ (40 điểm):**
  - < 20ms: 40 điểm
  - < 50ms: 30 điểm
  - < 100ms: 20 điểm
  - ≥ 100ms: 10 điểm

- **Tốc độ download (60 điểm):**
  - > 50 Mbps: 60 điểm
  - > 20 Mbps: 45 điểm
  - > 10 Mbps: 30 điểm
  - > 5 Mbps: 20 điểm
  - ≤ 5 Mbps: 10 điểm

## Lưu ý / Notes

- Một số tính năng yêu cầu quyền administrator/sudo
- Kiểm tra tốc độ mạng cần kết nối internet
- Trên Linux, có thể cần cài đặt `iwconfig` hoặc `nmcli` để kiểm tra WiFi
- Kết quả có thể khác nhau tùy thuộc vào môi trường mạng

## License

MIT License

## Đóng góp / Contributing

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo pull request hoặc issue.
