# Air Guard V2.O

location = ""
pm_list = []
o3_list = []

def input_data():
  global location, pm_list, o3_list

  pm_list = []
  o3_list = []

  location = input("지역명 입력: ")
  day_count = int(input("일수 입력: "))

  for i in range(day_count):
    print(f"\n{i+1}일차 데이터 입력")

    pm = float(input("PM10 입력:"))
    o3 = float(input("O3 입력: "))
    if pm <0 or o3 < 0:
      print("음수 데이터는 저장되지 않습니다.")
      continue
    if pm > 2000 or o3 > 1:
      print("입력 범위를 초과하여 입력을 종료합니다.")
      break

    pm_list.append(pm)
    o3_list.append(o3)

def calculate_stats(pms, o3s):
  if len(pms) == 0:
    return None
    avg_pm = sum(pms) / len(pms)
    avg_o3 = sum(o3s) / len(o3s)

  if avg_pm <=30 and avg_o3 <= 0.03:
    grade = "좋음"
  elif avg_pm <=80 or avg_o3 <= 0.09:
    grade = "보통"
  else:
    grade = "나쁨"

  return [avg_pm, avg_o3, max(pms), max(o3s),mins(pms), min(o3s), grade]

def print results(res):
  print("\n==== 대기질 분석 결과 ====")
  print(f"지역: {location}")
  print(f"평균 PM10: {round(res[0], 2)}")
  print(f"평균 O3: {round(res[1], 4)}")
  print(f"최대 PM10 : {res[2]")
  print(f"최대 O3: {res[3]}")
  print(f"최소 PM10: {res[4]}")
  print(f"등급 :{res[6]}")

  print("\n[일별 데이터]")
  for i in range(len(pm_list)):
    print(f"{i+1}일차 -> PM10: {pm_list[i]}, O3: {o3_list[i]}")
  print("=========================")

while True:
  print("\n[1. 입력] [2. 조회] [3. 종료]")
  menu = input("메뉴 선택:")

 if menu == "1":
   input_data()
 elif menu == "2":
   if len(pm_list) == 0:
     print("입력된 데이터가 없습니다.")
      continue
    result = calculate_stats(pm_list, o3_list)
    if result is None:
      print("유효한 데이터가 없습니다.")
    else:
      print_results(result)
elif menu == "3":
  print("프로그램을 종료합니다.")
  break
else:
  print("올바른 메뉴를 선택하세요.")
