# 파일명: s1218_3.py

pocket = input("소지 물품들: ").split()

if 'money' in pocket or 'card' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어 가라')