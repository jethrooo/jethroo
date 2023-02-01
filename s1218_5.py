# 파일명: s1218_5.py
# 3과목의 점수들을 입력받아 평균을 구하고, 
# 평균에 따른 결과를 출력하는 프로그램
# 90점이상 A등급, 80점이상 B등급, 70점이상 C등급
# 60점이상 D등급, 그외(60점미만) F등급

score1 = int(input("1과목 점수: "))
score2 = int(input("2과목 점수: "))
score3 = int(input("3과목 점수: "))
avg = (score1 + score2 + score3) / 3

print("\n입력하신 점수의 결과입니다.")
print(f"평균: {avg:.1f} 점")
if 90 <= avg:   print("결과: A 등급")
elif 80 <= avg: print("결과: B 등급")
elif 70 <= avg: print("결과: C 등급")
elif 60 <= avg: print("결과: D 등급")
else:           print("결과: F 등급")
