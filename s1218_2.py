# 파일명: s1218_2.py

money = int(input("소지금액 입력: "))
card  = input("카드 소지여부[yes/no]: ").lower()

if money >= 4000 or card == "yes":
    print("택시를 타고 가라")
else:
    print("걸어 가라")