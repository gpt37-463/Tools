#!/usr/bin/env python3
"""
Demo script - Ví dụ sử dụng Network Monitor
Demonstrates how to use the NetworkMonitor class programmatically
"""

from network_monitor import NetworkMonitor

def demo_basic_usage():
    """Ví dụ sử dụng cơ bản"""
    print("=== VÍ DỤ 1: SỬ DỤNG CƠ BẢN ===\n")
    
    # Tạo instance
    monitor = NetworkMonitor()
    
    # Chạy tất cả các kiểm tra
    results = monitor.run_all_checks()
    
    return results


def demo_individual_checks():
    """Ví dụ chạy từng kiểm tra riêng lẻ"""
    print("\n\n=== VÍ DỤ 2: CHẠY TỪNG KIỂM TRA RIÊNG LẺ ===\n")
    
    monitor = NetworkMonitor()
    
    # Chỉ kiểm tra cấu hình
    print("1. Chỉ kiểm tra cấu hình:")
    config = monitor.check_network_config()
    
    # Chỉ kiểm tra WiFi
    print("\n2. Chỉ kiểm tra WiFi:")
    wifi = monitor.check_wifi_signal()
    
    # Chỉ kiểm tra tốc độ
    print("\n3. Chỉ kiểm tra tốc độ:")
    speed = monitor.test_network_speed()
    
    # Chỉ kiểm tra firewall
    print("\n4. Chỉ kiểm tra firewall:")
    firewall = monitor.check_firewall()
    
    return {
        'config': config,
        'wifi': wifi,
        'speed': speed,
        'firewall': firewall
    }


def demo_custom_report():
    """Ví dụ tạo báo cáo tùy chỉnh"""
    print("\n\n=== VÍ DỤ 3: BÁO CÁO TỪ CHỈNH ===\n")
    
    monitor = NetworkMonitor()
    
    # Chạy các kiểm tra cần thiết
    monitor.check_network_config()
    monitor.check_wifi_signal()
    
    # Tạo báo cáo tùy chỉnh
    print("\n📊 BÁO CÁO TÙY CHỈNH:")
    print("-" * 40)
    
    if 'config' in monitor.results:
        config = monitor.results['config']
        print(f"🖥️  Máy tính: {config.get('hostname', 'N/A')}")
        print(f"🌐 IP: {config.get('ip_address', 'N/A')}")
        print(f"🔌 Internet: {'✓' if config.get('internet_connected') else '✗'}")
    
    if 'wifi' in monitor.results and monitor.results['wifi']:
        wifi = monitor.results['wifi']
        print(f"📡 WiFi: {wifi.get('ssid', 'N/A')}")
        print(f"📶 Tín hiệu: {wifi.get('signal_strength', 'N/A')}%")
    
    print("-" * 40)


if __name__ == "__main__":
    # Chạy các ví dụ
    try:
        # Ví dụ 1: Sử dụng cơ bản
        demo_basic_usage()
        
        # Uncomment để chạy các ví dụ khác:
        # demo_individual_checks()
        # demo_custom_report()
        
    except KeyboardInterrupt:
        print("\n\nĐã dừng demo.")
    except Exception as e:
        print(f"\n\nLỗi trong demo: {e}")
