import random # 먼저 random 모듈을 import 합니다.

print("부산대학교 casino에 오신 것을 환영합니다")

a = random.randint(1,10) + random.randint(1,10) 
#random.randint을 사용해 1부터 10까지의 숫자를 생성하고 합을 계산한 결과를 a에 저장합니다.

number = int(input("숫자를 입력하세요: ")) 
cal = True # While을 사용하기 위해 bool 형태의 변수를 설정합니다.
try_number = 0 # 시도 횟수를 확인하기 위한 변수를 설정합니다.
while cal:
    if abs(a - number) <= 1: # abs를 사용해 절댓값이 1 이하인 경우를 상정합니다.
        print("win!")
        print("정답은 %s 입니다!" %a)
        cal = False # 더 이상 추측하지 않아도 되므로 while을 종료하기 위해 False로 바꿔 프로그램을 마칩니다.
        
    #나머지 두 경우에선 높거나 작은 경우이므로, 조언을 해주고 다시 입력받습니다. 다시 했기에 시도 횟수를 변경합니다.
    
    elif a - number > 1 and try_number == 0: # 다시 시도함을 확인하기 위해 해당 변수의 변화 여부를 확인합니다.
        print("더 높은 숫자입니다")
        try_number += 1 # 다시 시도함을 확인하기 위해 해당 변수에 1을 더합니다.
        number = int(input("숫자를 입력하세요: "))
    elif a - number < -1 and try_number == 0:
        print("더 낮은 숫자입니다")
        try_number += 1
        number = int(input("숫자를 입력하세요: "))
    else: # 둘 다 틀렸을 경우 fail을 표시하면서 정답을 알려주고 해당 프로그램을 마칩니다.
        print("fail...")
        print("정답은 %s 입니다" %a)
        cal = False
