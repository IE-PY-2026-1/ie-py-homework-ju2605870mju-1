# Air Guard V1.O

location = input("지역명 입력: ")
day_count = int(input("일수 입력: "))

pm_list = []
o3_list = []

total_pm10 = 0
total_o3 = 0

for i in range(n):
  pm = float(input("PM10 입력: "))
  O3 = float(input("O3 입력: "))

  if pm10 < 0 or o3 <0:
    continue

  pm_list.append(pm)
  o3_list.append(o3)
  
  total_pm += pm
  total_o3 += o3

avg_pm10 = total_pm / len(pm_list)
avg_o3= total_o3 / len(o3_list)

if avg_pm <= 30 and avg_o3 <= 0.03:
  grade = "좋음"
elif avg_pm <= 80 or avg_o3 <= 0.09:
  grade = "보통"
else:
  grade = "나쁨"

print("지역: ", location)
print("평균 PM10: ", avg_pm)
print("평균 O3: ", avg_o3)
print("등급: ", grade)

for i in range(len(pm_list)):
  print(i+1, "일차: , pm_list[i], o3_list[i])
