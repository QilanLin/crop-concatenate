from PIL import Image

BACKGROUND_COLOR = (255, 255, 255)
NUM_ROWS_TO_OVERLAP = 40
# 加载图片
img1 = Image.open('1.png')
img2 = Image.open('2.png')
# 获取img2大小
width, height = img1.size
# 获取img1像素数据
pixels = img1.load()
rows_pixels = []
for y in range(img1.height - NUM_ROWS_TO_OVERLAP, img1.height):
    single_row_pixels = [pixels[x, y] for x in range(img1.width)]
    rows_pixels.append(single_row_pixels)
    # print('rows_pixels:', rows_pixels)
# 获取img2像素数据
pixels2 = img2.load()
# 获取img2的宽度和高度
width, height = img2.size
overlap_height = 0
# 读取img2像素, 计算重叠高度
for c in range(0, img2.height - NUM_ROWS_TO_OVERLAP):
    rows_pixels2 = []
    for y in range(c, c + NUM_ROWS_TO_OVERLAP):
        single_row_pixels = [pixels2[x, y] for x in range(img2.width)]
        rows_pixels2.append(single_row_pixels)
        # print('rows_pixels2:', rows_pixels2)
    if rows_pixels2 == rows_pixels:
        overlap_height = c + NUM_ROWS_TO_OVERLAP
        break

# 计算新图片的大小
print('overlap_height=',overlap_height)
new_width = width
new_height = height + img2.height - overlap_height

# 创建新图片
new_img = Image.new('RGB', (new_width, new_height), BACKGROUND_COLOR)

# 将img1复制到新图片的上部
new_img.paste(img1.crop((0, 0, img1.width, img1.height - overlap_height)), (0, 0))

# 将img2复制到新图片的下部
new_img.paste(img2.crop((0, overlap_height, img2.width, img2.height)), (0, img1.height - overlap_height))

# 保存新图片
new_img.save('output.png')
