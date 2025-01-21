import tkinter as tk
from tkinter import simpledialog
import pyautogui
import time
from PIL import ImageGrab

def get_color_at_center(box_size):
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    box_left = center_x - box_size // 2
    box_top = center_y - box_size // 2
    box_right = center_x + box_size // 2
    box_bottom = center_y + box_size // 2

    img = ImageGrab.grab(bbox=(box_left, box_top, box_right, box_bottom))
    pixels = img.load()
    
    # 获取中心像素的颜色
    color = pixels[box_size // 2, box_size // 2]
    return color

def check_color(target_color):
    box_size = 9
    while True:
        current_color = get_color_at_center(box_size)
        if current_color == target_color:
            pyautogui.click()
        time.sleep(0.1)

def start_detection():
    color_code = simpledialog.askstring("输入颜色", "请输入颜色代码（例如：255,0,0）：")
    if color_code:
        target_color = tuple(map(int, color_code.split(',')))
        check_color(target_color)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    start_detection()