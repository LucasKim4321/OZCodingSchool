# main.py

# oz_package 패키지의 oz_module_1 모듈을 'one'이라는 별칭으로 임포트합니다.
import oz_package.oz_module_1 as one

# oz_package 패키지의 oz_module_2 모듈을 'two'라는 별칭으로 임포트합니다.
import oz_package.oz_module_2 as two

# oz_module_1 모듈에서 정의된 val_1 변수를 출력합니다.
print(one.val_1)

# oz_module_2 모듈에서 정의된 val_2 변수를 출력합니다.
print(two.val_2)

# 변수도 가능하고 함수도 가능함.