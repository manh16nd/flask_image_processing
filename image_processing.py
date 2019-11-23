import cv2
import numpy as np 


def cal_value(gray):
    matrix = np.matrix(gray)
    total = matrix.sum()
    n = matrix.shape[0] * matrix.shape[1]
    average_value = total / n
    
    result = {
        "total": total,
        "average_value": average_value,
        "pixel_quantity": n
    }

    return result


def parse_img(file):
    print(file)
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return cal_value(gray)
