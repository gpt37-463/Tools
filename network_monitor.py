#!/usr/bin/env python3
"""
Network Monitoring Tool
Kiểm tra kết nối mạng nội bộ, tốc độ, tín hiệu WiFi, cấu hình và tường lửa
"""

import subprocess
import platform
import socket
import time
import re
import sys
from datetime import datetime


class NetworkMonitor:
    def __init__(self):
        self.os_type = platform.system()
        self.results = {}
        
    def check_network_config(self):
        """Kiểm tra cấu hình mạng"""
        print("\n=== KIỂM TRA CẤU HÌNH MẠNG ===")
        config = {}
        
        try:
            # Lấy hostname
            config['hostname'] = socket.gethostname()
            print(f"Hostname: {config['hostname']}")
            
            # Lấy địa chỉ IP
            config['ip_address'] = socket.gethostbyname(config['hostname'])
            print(f"Địa chỉ IP: {config['ip_address']}")
            
            # Kiểm tra kết nối internet
            config['internet_connected'] = self.check_internet_connection()
            print(f"Kết nối Internet: {'Có' if config['internet_connected'] else 'Không'}")
            
            # Lấy thông tin chi tiết về interface
            config['interfaces'] = self.get_network_interfaces()
            
            self.results['config'] = config
            return config
            
        except Exception as e:
            print(f"Lỗi khi kiểm tra cấu hình: {e}")
            return None
    
    def check_internet_connection(self):
        """Kiểm tra kết nối internet"""
        try:
            # Thử kết nối đến Google DNS
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
    
    def get_network_interfaces(self):
        """Lấy thông tin về các interface mạng"""
        interfaces = []
        
        try:
            if self.os_type == "Windows":
                result = subprocess.run(['ipconfig', '/all'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                print(f"\nThông tin Interface:")
                print(output[:500] + "..." if len(output) > 500 else output)
                
            elif self.os_type == "Linux":
                result = subprocess.run(['ip', 'addr'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                print(f"\nThông tin Interface:")
                print(output[:500] + "..." if len(output) > 500 else output)
                
            elif self.os_type == "Darwin":  # macOS
                result = subprocess.run(['ifconfig'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                print(f"\nThông tin Interface:")
                print(output[:500] + "..." if len(output) > 500 else output)
                
        except Exception as e:
            print(f"Không thể lấy thông tin interface: {e}")
        
        return interfaces
    
    def check_wifi_signal(self):
        """Kiểm tra tín hiệu WiFi"""
        print("\n=== KIỂM TRA TÍN HIỆU WIFI ===")
        wifi_info = {}
        
        try:
            if self.os_type == "Windows":
                result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                
                # Tìm SSID
                ssid_match = re.search(r'SSID\s+:\s+(.+)', output)
                if ssid_match:
                    wifi_info['ssid'] = ssid_match.group(1).strip()
                    print(f"SSID: {wifi_info['ssid']}")
                
                # Tìm signal strength
                signal_match = re.search(r'Signal\s+:\s+(\d+)%', output)
                if signal_match:
                    wifi_info['signal_strength'] = int(signal_match.group(1))
                    print(f"Cường độ tín hiệu: {wifi_info['signal_strength']}%")
                    wifi_info['signal_grade'] = self.grade_signal(wifi_info['signal_strength'])
                    print(f"Đánh giá tín hiệu: {wifi_info['signal_grade']}")
                
            elif self.os_type == "Linux":
                # Sử dụng iwconfig hoặc nmcli
                try:
                    result = subprocess.run(['iwconfig'], 
                                          capture_output=True, text=True, timeout=10)
                    output = result.stdout
                    
                    # Tìm SSID
                    ssid_match = re.search(r'ESSID:"(.+)"', output)
                    if ssid_match:
                        wifi_info['ssid'] = ssid_match.group(1)
                        print(f"SSID: {wifi_info['ssid']}")
                    
                    # Tìm signal quality
                    signal_match = re.search(r'Link Quality=(\d+)/(\d+)', output)
                    if signal_match:
                        quality = int(signal_match.group(1))
                        max_quality = int(signal_match.group(2))
                        wifi_info['signal_strength'] = int((quality / max_quality) * 100)
                        print(f"Cường độ tín hiệu: {wifi_info['signal_strength']}%")
                        wifi_info['signal_grade'] = self.grade_signal(wifi_info['signal_strength'])
                        print(f"Đánh giá tín hiệu: {wifi_info['signal_grade']}")
                        
                except FileNotFoundError:
                    print("Lệnh iwconfig không có sẵn. Thử nmcli...")
                    result = subprocess.run(['nmcli', 'device', 'wifi'], 
                                          capture_output=True, text=True, timeout=10)
                    print(result.stdout)
                    
            elif self.os_type == "Darwin":  # macOS
                result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                
                # Tìm SSID
                ssid_match = re.search(r'SSID:\s+(.+)', output)
                if ssid_match:
                    wifi_info['ssid'] = ssid_match.group(1).strip()
                    print(f"SSID: {wifi_info['ssid']}")
                
                # Tìm RSSI (signal strength)
                rssi_match = re.search(r'agrCtlRSSI:\s+(-?\d+)', output)
                if rssi_match:
                    rssi = int(rssi_match.group(1))
                    # Chuyển đổi RSSI sang phần trăm (thang đo thường từ -90 đến -30)
                    wifi_info['signal_strength'] = max(0, min(100, (rssi + 90) * (100 / 60)))
                    print(f"Cường độ tín hiệu: {wifi_info['signal_strength']:.0f}%")
                    wifi_info['signal_grade'] = self.grade_signal(wifi_info['signal_strength'])
                    print(f"Đánh giá tín hiệu: {wifi_info['signal_grade']}")
            
            if not wifi_info:
                print("Không tìm thấy kết nối WiFi hoặc không có quyền truy cập")
                
        except Exception as e:
            print(f"Lỗi khi kiểm tra WiFi: {e}")
        
        self.results['wifi'] = wifi_info
        return wifi_info
    
    def grade_signal(self, signal_strength):
        """Đánh giá chất lượng tín hiệu"""
        if signal_strength >= 80:
            return "Xuất sắc (A)"
        elif signal_strength >= 60:
            return "Tốt (B)"
        elif signal_strength >= 40:
            return "Trung bình (C)"
        elif signal_strength >= 20:
            return "Yếu (D)"
        else:
            return "Rất yếu (F)"
    
    def test_network_speed(self):
        """Kiểm tra tốc độ mạng"""
        print("\n=== KIỂM TRA TỐC ĐỘ MẠNG ===")
        speed_info = {}
        
        # Kiểm tra độ trễ (latency) bằng ping
        speed_info['latency'] = self.test_latency()
        
        # Kiểm tra tốc độ download đơn giản
        speed_info['download_test'] = self.simple_download_test()
        
        # Đánh giá tốc độ
        speed_info['speed_grade'] = self.grade_network_speed(
            speed_info['latency'], 
            speed_info['download_test']
        )
        
        print(f"\nĐánh giá tốc độ mạng: {speed_info['speed_grade']}")
        
        self.results['speed'] = speed_info
        return speed_info
    
    def test_latency(self):
        """Kiểm tra độ trễ mạng"""
        print("\nKiểm tra độ trễ (ping)...")
        
        try:
            if self.os_type == "Windows":
                result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                
                # Tìm average time
                avg_match = re.search(r'Average = (\d+)ms', output)
                if avg_match:
                    latency = int(avg_match.group(1))
                    print(f"Độ trễ trung bình: {latency}ms")
                    return latency
                    
            else:  # Linux/macOS
                result = subprocess.run(['ping', '-c', '4', '8.8.8.8'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                
                # Tìm average time
                avg_match = re.search(r'avg[^0-9]*([0-9.]+)', output)
                if avg_match:
                    latency = float(avg_match.group(1))
                    print(f"Độ trễ trung bình: {latency:.1f}ms")
                    return latency
                    
        except Exception as e:
            print(f"Không thể kiểm tra độ trễ: {e}")
        
        return None
    
    def simple_download_test(self):
        """Kiểm tra tốc độ download đơn giản"""
        print("\nKiểm tra tốc độ download...")
        
        try:
            import urllib.request
            
            # Download một file nhỏ để test
            test_url = "http://speedtest.ftp.otenet.gr/files/test1Mb.db"
            
            start_time = time.time()
            response = urllib.request.urlopen(test_url, timeout=15)
            data = response.read()
            end_time = time.time()
            
            # Tính toán tốc độ (Mbps)
            file_size_mb = len(data) / (1024 * 1024)
            duration = end_time - start_time
            speed_mbps = (file_size_mb * 8) / duration
            
            print(f"Tốc độ download: {speed_mbps:.2f} Mbps")
            return speed_mbps
            
        except Exception as e:
            print(f"Không thể kiểm tra tốc độ download: {e}")
            print("(Có thể do không có kết nối internet hoặc firewall chặn)")
        
        return None
    
    def grade_network_speed(self, latency, download_speed):
        """Đánh giá tốc độ mạng tổng thể"""
        score = 0
        
        # Đánh giá latency (40 điểm)
        if latency:
            if latency < 20:
                score += 40
            elif latency < 50:
                score += 30
            elif latency < 100:
                score += 20
            else:
                score += 10
        else:
            score += 20  # Điểm trung bình nếu không test được
        
        # Đánh giá download speed (60 điểm)
        if download_speed:
            if download_speed > 50:
                score += 60
            elif download_speed > 20:
                score += 45
            elif download_speed > 10:
                score += 30
            elif download_speed > 5:
                score += 20
            else:
                score += 10
        else:
            score += 30  # Điểm trung bình nếu không test được
        
        # Chuyển điểm thành grade
        if score >= 90:
            return f"Xuất sắc (A) - {score}/100 điểm"
        elif score >= 75:
            return f"Tốt (B) - {score}/100 điểm"
        elif score >= 60:
            return f"Trung bình (C) - {score}/100 điểm"
        elif score >= 40:
            return f"Yếu (D) - {score}/100 điểm"
        else:
            return f"Rất yếu (F) - {score}/100 điểm"
    
    def check_firewall(self):
        """Kiểm tra trạng thái tường lửa"""
        print("\n=== KIỂM TRA TƯỜNG LỬA ===")
        firewall_info = {}
        
        try:
            if self.os_type == "Windows":
                result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                
                # Kiểm tra trạng thái firewall
                if "State" in output or "ON" in output:
                    firewall_info['enabled'] = "ON" in output
                    firewall_info['status'] = output
                    print(f"Tường lửa: {'BẬT' if firewall_info['enabled'] else 'TẮT'}")
                    print(f"\nChi tiết:")
                    print(output[:300] + "..." if len(output) > 300 else output)
                
            elif self.os_type == "Linux":
                # Kiểm tra ufw
                try:
                    result = subprocess.run(['ufw', 'status'], 
                                          capture_output=True, text=True, timeout=10)
                    output = result.stdout
                    firewall_info['type'] = 'ufw'
                    firewall_info['enabled'] = 'active' in output.lower()
                    print(f"Tường lửa (ufw): {'BẬT' if firewall_info['enabled'] else 'TẮT'}")
                    print(output)
                except FileNotFoundError:
                    # Kiểm tra iptables
                    result = subprocess.run(['iptables', '-L'], 
                                          capture_output=True, text=True, timeout=10)
                    output = result.stdout
                    firewall_info['type'] = 'iptables'
                    firewall_info['rules_count'] = len(output.split('\n'))
                    print(f"Tường lửa (iptables): Có {firewall_info['rules_count']} quy tắc")
                    print(output[:300] + "..." if len(output) > 300 else output)
                
            elif self.os_type == "Darwin":  # macOS
                result = subprocess.run(['/usr/libexec/ApplicationFirewall/socketfilterfw', '--getglobalstate'], 
                                      capture_output=True, text=True, timeout=10)
                output = result.stdout
                firewall_info['enabled'] = 'enabled' in output.lower()
                print(f"Tường lửa: {'BẬT' if firewall_info['enabled'] else 'TẮT'}")
                print(output)
                
        except PermissionError:
            print("Không có quyền kiểm tra tường lửa. Cần chạy với quyền administrator/sudo.")
            firewall_info['error'] = 'Permission denied'
        except Exception as e:
            print(f"Lỗi khi kiểm tra tường lửa: {e}")
            firewall_info['error'] = str(e)
        
        self.results['firewall'] = firewall_info
        return firewall_info
    
    def generate_report(self):
        """Tạo báo cáo tổng hợp"""
        print("\n" + "="*60)
        print("BÁO CÁO TỔNG HỢP KIỂM TRA MẠNG")
        print("="*60)
        print(f"Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Hệ điều hành: {self.os_type}")
        print("="*60)
        
        # Tóm tắt kết quả
        if 'config' in self.results:
            print(f"\n✓ Cấu hình mạng: {self.results['config'].get('ip_address', 'N/A')}")
            print(f"  Internet: {'Có kết nối' if self.results['config'].get('internet_connected') else 'Không kết nối'}")
        
        if 'wifi' in self.results and self.results['wifi']:
            print(f"\n✓ WiFi SSID: {self.results['wifi'].get('ssid', 'N/A')}")
            print(f"  Tín hiệu: {self.results['wifi'].get('signal_grade', 'N/A')}")
        
        if 'speed' in self.results:
            print(f"\n✓ Tốc độ mạng: {self.results['speed'].get('speed_grade', 'N/A')}")
        
        if 'firewall' in self.results:
            fw = self.results['firewall']
            if 'error' in fw:
                print(f"\n✓ Tường lửa: Không thể kiểm tra ({fw['error']})")
            elif 'enabled' in fw:
                print(f"\n✓ Tường lửa: {'BẬT' if fw['enabled'] else 'TẮT'}")
        
        print("\n" + "="*60)
    
    def run_all_checks(self):
        """Chạy tất cả các kiểm tra"""
        print("Bắt đầu kiểm tra mạng...")
        print("="*60)
        
        self.check_network_config()
        self.check_wifi_signal()
        self.test_network_speed()
        self.check_firewall()
        self.generate_report()
        
        return self.results


def main():
    """Hàm chính"""
    print("=" * 60)
    print("CHƯƠNG TRÌNH KIỂM TRA MẠNG")
    print("Network Monitoring Tool")
    print("=" * 60)
    
    monitor = NetworkMonitor()
    results = monitor.run_all_checks()
    
    print("\n✓ Hoàn thành kiểm tra!")
    return results


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nĐã dừng chương trình.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nLỗi: {e}")
        sys.exit(1)
