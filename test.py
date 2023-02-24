from PIL import Image
import numpy as np

# 创建两张图像
img1 = np.zeros((200, 1500, 3), dtype=np.uint8)
img2 = np.zeros((200, 1500, 3), dtype=np.uint8)

# 在第一张图像上绘制绿色矩形
for i in range(160, 200):
    for j in range(0, 1500):
        img1[i, j] = [0, 255, 0]

# 在第一张图像上绘制一些图案
for i in range(50, 100):
    for j in range(100, 400):
        img1[i, j] = [255, 0, 0]
    for j in range(650, 950):
        img1[i, j] = [0, 255, 255]
    for j in range(1200, 1500):
        img1[i, j] = [255, 255, 0]

# 在第二张图像上绘制绿色矩形
for i in range(20, 60):
    for j in range(0, 1500):
        img2[i, j] = [0, 255, 0]

# 在第二张图像上绘制一些图案
for i in range(100, 150):
    for j in range(100, 400):
        img2[i, j] = [0, 0, 255]
    for j in range(650, 950):
        img2[i, j] = [255, 0, 255]
    for j in range(1200, 1500):
        img2[i, j] = [0, 255, 0]

# 将两张图像保存为文件
Image.fromarray(img1).save('1.png')
Image.fromarray(img2).save('2.png')
