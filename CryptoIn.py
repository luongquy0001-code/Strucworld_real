import random
import time

# Khởi tạo danh sách tài sản
assets = {}

# Hàm thêm tài sản
def add_asset(name):
    if name not in assets:
        assets[name] = {'quantity': 0, 'price': 100}  # Giá khởi tạo là 100
        print(f"Tài sản '{name}' đã được thêm.")
    else:
        print(f"Tài sản '{name}' đã tồn tại.")

# Hàm mua tài sản
def buy_asset(name, quantity, price):
    if name in assets:
        assets[name]['quantity'] += quantity
        assets[name]['price'] = price  # Cập nhật giá mua
        print(f"Đã mua {quantity} của '{name}' với giá {price:.2f}.")
    else:
        print(f"Tài sản '{name}' không tồn tại.")

# Hàm bán tài sản
def sell_asset(name, quantity):
    if name in assets:
        if assets[name]['quantity'] >= quantity:
            assets[name]['quantity'] -= quantity
            print(f"Đã bán {quantity} của '{name}'.")
        else:
            print(f"Số lượng không đủ để bán {quantity} của '{name}'.")
    else:
        print(f"Tài sản '{name}' không tồn tại.")

# Hàm cập nhật giá ngẫu nhiên với thao túng từ cá voi
def update_prices():
    for name in assets:
        # Tạo biến động ngẫu nhiên cho giá
        change = random.uniform(-0.05, 0.05)  # Biến động từ -5% đến +5%
        
        # Giả định cá voi thao túng giá
        if random.random() < 0.1:  # 10% khả năng cá voi thao túng
            change += random.uniform(-0.1, 0.1)  # Thao túng mạnh hơn

        assets[name]['price'] *= (1 + change)

# Hàm thống kê tài sản
def print_statistics():
    print("\nThống kê tài sản:")
    print(f"{'Tài sản':<20} {'Số lượng':<10} {'Giá':<10}")
    print("-" * 40)
    for name, info in assets.items():
        print(f"{name:<20} {info['quantity']:<10} {info['price']:.2f}")

# Hàm vẽ biểu đồ đơn giản
def draw_chart():
    print("\nBiểu đồ tài sản:")
    for name, info in assets.items():
        print(f"{name}: {'*' * int(info['quantity'])}")

# Chương trình chính
while True:
    update_prices()  # Cập nhật giá trước mỗi hành động
    action = input("\nNhập hành động (add, buy, sell, stats, chart, exit): ").strip().lower()
    
    if action == 'add':
        asset_name = input("Nhập tên tài sản: ")
        add_asset(asset_name)
    elif action == 'buy':
        asset_name = input("Nhập tên tài sản: ")
        quantity = int(input("Nhập số lượng: "))
        price = float(input("Nhập giá: "))
        buy_asset(asset_name, quantity, price)
    elif action == 'sell':
        asset_name = input("Nhập tên tài sản: ")
        quantity = int(input("Nhập số lượng: "))
        sell_asset(asset_name, quantity)
    elif action == 'stats':
        print_statistics()
    elif action == 'chart':
        draw_chart()
    elif action == 'exit':
        print("Thoát chương trình.")
        break
    else:
        print("Hành động không hợp lệ. Vui lòng thử lại.")
    
    time.sleep(1)  # Tạm dừng một giây trước khi tiếp tục