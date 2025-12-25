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

## Cấu trúc dự án / Project Structure

```
Tools/
├── network_monitor.py      # Main program - Chương trình chính
├── demo.py                 # Usage examples - Ví dụ sử dụng
├── test_network_monitor.py # Test suite - Bộ test
├── requirements.txt        # Dependencies (none required)
├── README.md              # Documentation
└── .gitignore            # Git ignore file
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

### Chạy demo với các ví dụ:

```bash
python3 demo.py
```

### Chạy tests:

```bash
python3 test_network_monitor.py
```

## Ví dụ kết quả / Example Output

```
