# 문제 6
first = int(input("1차 점수 입력: "))
second = int(input("2차 점수 입력: "))

if first >= 80 and second >= 80:
    print("합격")
else:
    print("불합격")

# 문제 9
score = int(input("점수 입력: "))

if score >= 90:
    print(f"{score}점은 A학점")
elif score >= 80:
    print(f"{score}점은 B학점")
elif score >= 70:
    print(f"{score}점은 C학점")
elif score >= 60:
    print(f"{score}점은 D학점")
else:
    print(f"{score}점은 F학점")

# 문제 3
seasons = ['겨울', '겨울', '겨울', '봄', '봄', '봄',
           "여름", "여름", "여름", "가을", "가을", "가을", "겨울"]
month = int(input("월 입력: "))
result = seasons[month]
print(f"{month}월은 {result}")

# 문제 6
distance = int(input("배송거리 입력: "))

if distance < 5:
    print("배송 불가")

elif distance < 50:
    print("배송료: 3500원")

elif distance < 100:
    print("배송료: 4000원")

elif distance < 300:
    print("배송료: 4500원")

elif distance < 500:
    print("배송료: 5000원")

else:
    print("배송료: 6000원")
