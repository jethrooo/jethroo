# 파일명: s1218_7.py

scores = [80, 90, 85, 78, 92]

sum = 0
for score in scores:
    sum = sum + score
avg = sum / len(scores)
print(f"합계는 {sum}입니다.")
print(f"평균은 {avg:.1f}입니다.")
