
import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width, screen_height = 1000, 2000
screen = pygame.display.set_mode((screen_width, screen_height))

# Thiết lập tốc độ FPS
clock = pygame.time.Clock()
fps = 260  # Thay đổi giá trị này để điều chỉnh FPS

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Cập nhật màn hình
    screen.fill((1, 0, 1))  # Màu nền
    pygame.display.flip()

    # Thiết lập FPS
    clock.tick(fps)  # Điều chỉnh FPS
print("160fps")