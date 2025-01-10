# import math

version = "v1.0.0"

pi = 3.141592

def triangle_area(base, height):
    """
    삼각형의 넓이를 계산합니다.
    :param base: 밑변 길이
    :param height: 높이
    :return: 삼각형의 넓이
    """
    return base * height / 2


def circle_area(radius):
    """
    원의 넓이를 계산합니다.
    :param radius: 반지름
    :return: 원의 넓이
    """
    return pi * radius ** 2

def rectangular_prism_area(length, width, height):
    """
    직육면체의 표면적을 계산합니다.
    :param length: 가로 길이
    :param width: 세로 길이
    :param height: 높이
    :return: 직육면체의 표면적
    공식1 세면 넓이의 합 * 2
    공식2 한면 넓이 * 2 + 한면의 둘래 * 2 * 나머지 길이
    """
    return 2 * (length * width + length * height + width * height)

# import sys
# print(sys.path)

# sys.path.append(r"c:\javaStudy\ozcoding\OZCodingSchool\python\module_package")  # 실제 경로로 수정