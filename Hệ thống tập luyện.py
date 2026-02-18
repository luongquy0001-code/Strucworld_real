import time
import random
import json
import os

USD_TO_VND = 26155.18
USER_DATA_FILE = "user_data.json"

class User:
    def __init__(self, username):
        self.username = username
        self.balance_vnd = 0
        self.balance_usd = 0
        self.inventory = []
        self.effort_multiplier = 1  # Mức độ chăm chỉ trong tập luyện
        self.load_user_data()  # Tải dữ liệu người dùng khi khởi tạo

    def load_user_data(self):
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                if data.get("username") == self.username:
                    self.balance_vnd = data.get("balance_vnd", 0)
                    self.inventory = data.get("inventory", [])
                    self.effort_multiplier = data.get("effort_multiplier", 1)

    def save_user_data(self):
        data = {
            "username": self.username,
            "balance_vnd": self.balance_vnd,
            "inventory": self.inventory,
            "effort_multiplier": self.effort_multiplier
        }
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file)

    def workout(self, duration):
        reward_vnd = (duration // 30) * 10000 * self.effort_multiplier  # 10.000 VND cho mỗi 30 phút
        self.balance_vnd += reward_vnd
        self.balance_usd = self.balance_vnd / USD_TO_VND
        print(f"{self.username} completed a workout and earned {reward_vnd} VND!")
        self.save_user_data()  # Lưu dữ liệu sau khi tập luyện

    def purchase_item(self, item, cost_usd):
        cost_vnd = cost_usd * USD_TO_VND
        if self.balance_vnd >= cost_vnd:
            self.balance_vnd -= cost_vnd
            self.inventory.append(item)
            print(f"{self.username} purchased {item} for {cost_usd} USD.")
            self.save_user_data()  # Lưu dữ liệu sau khi mua hàng
        else:
            print(f"{self.username} does not have enough VND to purchase {item}. Needs {cost_vnd:.2f} VND.")

    def show_inventory(self):
        print(f"{self.username}'s Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

    def show_balance(self):
        print(f"{self.username}'s Balance: {self.balance_vnd:.2f} VND, {self.balance_usd:.2f} USD")

    def start_workout_timer(self, duration):
        print(f"Starting workout for {duration} minutes...")
        for remaining in range(duration * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end='\r')  # Cập nhật đồng hồ đếm ngược trên cùng một dòng
            time.sleep(1)
        print("\nWorkout session finished!")

    def auto_start_workout(self, duration):
        self.start_workout_timer(duration)
        self.workout(duration)

# Cửa hàng với các mặt hàng hữu ích
shop_items = {
    "Luxury Gym Equipment": 40000,  # 40.000 USD
    "Premium Workout Clothes": 20000,  # 20.000 USD
    "Personal Trainer Session": 10000,  # 10.000 USD
    "Energy Drink": 5,  # Cung cấp hiệu ứng tăng tốc độ kiếm tiền
}

# Sử dụng lớp User
username = input("Enter your username: ")
user1 = User(username)

# Tự động bắt đầu bài tập 30 phút
user1.auto_start_workout(30)

# Hiển thị số dư
user1.show_balance()

# Người dùng cố gắng mua một món đồ trong cửa hàng
item_to_purchase = "Luxury Gym Equipment"
user1.purchase_item(item_to_purchase, shop_items[item_to_purchase])

# Hiển thị kho đồ
user1.show_inventory()