import random

class Resource:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.money = 1000
        self.slaves = 0
        self.resources = {}

    def buy_resource(self, resource, quantity):
        total_cost = resource.price * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            if resource.name in self.resources:
                self.resources[resource.name] += quantity
            else:
                self.resources[resource.name] = quantity
            print(f"{self.name} đã mua {quantity} {resource.name}(s).")
        else:
            print("Không đủ tiền để mua tài nguyên.")

    def sell_resource(self, resource, quantity):
        if resource.name in self.resources and self.resources[resource.name] >= quantity:
            self.resources[resource.name] -= quantity
            self.money += resource.price * quantity
            print(f"{self.name} đã bán {quantity} {resource.name}(s).")
        else:
            print("Không đủ tài nguyên để bán.")

    def buy_slave(self, quantity):
        cost_per_slave = 200
        total_cost = cost_per_slave * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            self.slaves += quantity
            print(f"{self.name} đã mua {quantity} nô lệ.")
        else:
            print("Không đủ tiền để mua nô lệ.")

    def show_status(self):
        print(f"Tên: {self.name}, Tiền: {self.money}đ, Sức khỏe: {self.health}, Nô lệ: {self.slaves}")
        print("Tài nguyên hiện có:")
        for resource, quantity in self.resources.items():
            print(f"- {resource}: {quantity}")

def main():
    print("Chào mừng đến với trò chơi kinh tế năm 1800!")
    player_name = input("Nhập tên của bạn: ")
    player = Character(player_name)

    resources = [
        Resource("Đường", 10),
        Resource("Bông", 15),
        Resource("Gỗ", 5),
        Resource("Thép", 20)
    ]

    while True:
        print("\n1. Mua tài nguyên")
        print("2. Bán tài nguyên")
        print("3. Mua nô lệ")
        print("4. Xem trạng thái")
        print("5. Thoát")
        choice = input("Chọn một hành động: ")

        if choice == "1":
            print("Chọn tài nguyên để mua:")
            for i, resource in enumerate(resources):
                print(f"{i}. {resource.name} - Giá: {resource.price}đ")
            resource_index = int(input("Nhập số tài nguyên: "))
            quantity = int(input("Nhập số lượng: "))
            if 0 <= resource_index < len(resources):
                player.buy_resource(resources[resource_index], quantity)
            else:
                print("Lựa chọn không hợp lệ.")
        elif choice == "2":
            print("Chọn tài nguyên để bán:")
            for i, resource in enumerate(resources):
                print(f"{i}. {resource.name} - Số lượng: {player.resources.get(resource.name, 0)}")
            resource_index = int(input("Nhập số tài nguyên: "))
            quantity = int(input("Nhập số lượng: "))
            if 0 <= resource_index < len(resources):
                player.sell_resource(resources[resource_index], quantity)
            else:
                print("Lựa chọn không hợp lệ.")
        elif choice == "3":
            quantity = int(input("Nhập số lượng nô lệ muốn mua: "))
            player.buy_slave(quantity)
        elif choice == "4":
            player.show_status()
        elif choice == "5":
            print("Cảm ơn bạn đã chơi!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()