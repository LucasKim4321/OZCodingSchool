import mymath

print(mymath.version)
print(mymath.triangle_area(2, 4))
print(mymath.circle_area(2))
print(mymath.rectangular_prism_area(2,4,6))

import animals

# 패키지 내부 딕셔너리 사용
print(animals.animals["mammals"])  # {'Primates': [...], 'Carnivores': [...]}
print(animals.animals["birds"])    # {'Raptors': [...], 'Waterfowl': [...]}
