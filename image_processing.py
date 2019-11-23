import cv2


def cal_value(gray):
    n = 0
    total = 0
    print(len(gray))

    for row in gray:
        for cell in row:
            n = n + 1
            total = total + cell
            print(n, total)

    result = {
        "total": total,
        "avarage_value": total / n,
        "pixel_quantity": n
    }

    return result


def parse_img(file):
    print(file)
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cal_value(gray)
