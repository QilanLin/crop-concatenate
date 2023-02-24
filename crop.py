from PIL import Image


def right_crop(img_path, right_pixels):
    """
    将图片左侧部分裁剪掉，只保留右侧指定个数的像素点

    Args:
    img_path: 要处理的图片的路径
    right_pixels: 保留的右侧像素点数

    Returns:
    None
    """
    # 打开图片
    img = Image.open(img_path)

    # 获取图片的宽度
    img_width = img.width

    # 计算左侧要裁剪掉的像素点数
    left_pixels = img_width - right_pixels

    # 裁剪左侧部分，每行只保留右侧指定个数的像素点
    cropped_img = img.crop((left_pixels, 0, img_width, img.height))
    return cropped_img


def left_crop(img_path, left_pixels):
    """
    将图片右侧部分裁剪掉，只保留左侧指定个数的像素点

    Args:
    img_path: 要处理的图片的路径
    left_pixels: 保留的左侧像素点数

    Returns:
    None
    """
    # 打开图片
    img = Image.open(img_path)

    # 获取图片的宽度
    img_width = img.width

    # 裁剪右侧部分，每行只保留左侧指定个数的像素点
    cropped_img = img.crop((0, 0, left_pixels, img.height))
    return cropped_img


def saving(cropped_img, output_path):
    cropped_img.save(output_path)
    print(f"图片已裁剪并保存为 {output_path}")

x=right_crop('02.png', 1150)
saving(x, '2.png')