import pygame
import zmq
import time

# 初始化 Pygame
pygame.init()

# 定義顏色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 設定窗口大小
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Autonomous Vehicle Simulation")

# 自走車設定
vehicle_radius = 10
vehicle_position = [100, 100]  # 初始位置

# 設定時鐘
clock = pygame.time.Clock()

# ZMQ 初始化
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")

# 主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 接收 commander 發送的指令
    try:
        message = socket.recv_string(flags=zmq.NOBLOCK)
        command, start, end = message.split()
        # 模擬自走車移動的過程
        start_pos = [int(start.split(',')[0]), int(start.split(',')[1])]
        end_pos = [int(end.split(',')[0]), int(end.split(',')[1])]
        vehicle_position = start_pos  # 這裡可以設計具體移動的過程
    except zmq.Again:
        pass  # 如果沒有消息，則跳過

    # 填充背景色
    screen.fill(WHITE)

    # 畫出路徑（可以根據 layout 的結構設計更多線條或方格）
    pygame.draw.line(screen, BLACK, (100, 100), (700, 700), 5)  # 例子：畫出一條路徑

    # 畫出自走車
    pygame.draw.circle(screen, BLUE, vehicle_position, vehicle_radius)

    # 更新畫面
    pygame.display.flip()

    # 控制每秒幀數
    clock.tick(30)

# 結束 Pygame
pygame.quit()