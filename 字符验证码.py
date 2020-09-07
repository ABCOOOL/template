from PIL import Image
import pytesseract


def handler(grays, threshold=160):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = grays.point(table, '1')
    return anti


# 图片灰度
gray = Image.open('下载.png').convert('L')
gray.show()

# 图片二值化
image = handler(gray, threshold=195)
image.show()
print(pytesseract.image_to_string(image))