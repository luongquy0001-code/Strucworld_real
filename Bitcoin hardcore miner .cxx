#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <iomanip>

class Miner {
public:
    Miner() : bitcoin(0.0), miningTime(5) {}

    void mine() {
        std::cout << "Đang khai thác BTC... ";
        for (int i = 0; i < miningTime; ++i) {
            std::cout << (i % 2 == 0 ? '0' : '1'); // Hiển thị 0 và 1
            std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // Độ trễ 1 giây
        }
        std::cout << std::endl;

        // Giả lập khả năng khai thác thành công với độ khó cực cao
        if (rand() % 10000 < 1) { // 0.01% khả năng thành công
            bitcoin += 0.001; // Tăng số Bitcoin theo hashrate
            std::cout << "Đã khai thác 0.001 BTC! Tổng BTC: " << std::fixed << std::setprecision(3) << bitcoin << std::endl;
        } else {
            std::cout << "Khai thác không thành công! Thử lại." << std::endl;
        }

        // Giả lập lỗi ngớ ngẩn
        if (rand() % 100 < 99) { // 99% khả năng gặp lỗi
            std::cout << "Lỗi: Không thể kết nối với mạng! Thử lại sau." << std::endl;
        }
    }

    double getBitcoin() const {
        return bitcoin;
    }

private:
    double bitcoin;  // Số Bitcoin đã khai thác
    int miningTime;  // Thời gian khai thác
};

void displayMovingCoin() {
    int width = 20;
    int height = 10;
    int coinX = rand() % width;
    int coinY = rand() % height;

    // Hiển thị đồng tiền vàng di chuyển lung tung
    for (int i = 0; i < 10; ++i) {
        std::system("clear"); // Xóa màn hình (trên Linux/Mac)
        // std::system("cls"); // Sử dụng cho Windows
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                if (x == coinX && y == coinY) {
                    std::cout << "💰"; // Hiển thị đồng tiền vàng
                } else {
                    std::cout << "×";
                }
            }
            std::cout << std::endl;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(500)); // Độ trễ 500ms
        coinX = rand() % width; // Cập nhật vị trí đồng tiền
        coinY = rand() % height; // Cập nhật vị trí đồng tiền

        // Giả lập va chạm với bẫy
        if (rand() % 100 < 10) { // 10% khả năng va chạm
            std::cout << "Đồng tiền đã va chạm với bẫy và bị hỏng!" << std::endl;
            return; // Kết thúc hàm nếu đồng tiền bị hỏng
        }
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0))); // Khởi tạo seed cho random
    Miner miner;
    char action;

    std::cout << "Chào mừng đến với trò chơi mô phỏng đào Bitcoin!" << std::endl;

    while (true) {
        std::cout << "Nhấn 'm' để khai thác BTC, 'q' để thoát: ";
        std::cin >> action;

        if (action == 'm') {
            displayMovingCoin(); // Hiển thị đồng tiền vàng di chuyển
            miner.mine();
        } else if (action == 'q') {
            std::cout << "Tổng BTC đã khai thác: " << std::fixed << std::setprecision(3) << miner.getBitcoin() << std::endl;
            break;
        } else {
            std::cout << "Hành động không hợp lệ!" << std::endl;
        }
    }

    return 0;
}