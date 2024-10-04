#영어 날짜를 한글 날짜로 변경
def day_to_korean(day) :
    if day == "Monday":
        return "월"
    elif day == "Tuesday" :
        return "화"
    elif day == "Wednesday" :
        return "수"
    elif day == "Thursday" :
        return "목"
    elif day == "Friday" :
        return "금"
    elif day == "Saturday":
        return "토"
    elif day == "Sunday":
        return "일"
    else:
        return day
    

#공사규모 사람수 형태로 변환
def convert_scale_to_person_range(scale):
    scale_map = {
        "소소": "9인",
        "소": "9인~50인",
        "중": "50~200인",
        "대": "200인"
    }
    return scale_map.get(scale, "None")

'''
카테고리화
'''

#근속연수 카테고리
def categorize_service_years(service_year) :
    service_year = service_year.strip()
    one = ["1개월미만","1개월~2개월미만","3개월~4개월미만","4개월~5개월미만","6개월미만"]
    two = ["6개월~1년"]
    three  = ["1~2년","1년~2년미만"]
    four = ["2~3년","2년~3년미만"]
    five = ["3~4년","3년~4년미만"]
    six = ["4~5년","4년~5년"]
    seven = ["5~10년","5년~10년"]

    if service_year in one :
        return "6개월미만"
    elif service_year in two :
        return "6개월~1년미만"
    elif service_year in three :
        return "1~2년미만"
    elif service_year in four :
        return "2~3년미만"
    elif service_year in five :
        return "3~4년미만"
    elif service_year in six :
        return "4~5년미만"
    elif service_year in seven :
        return "5~10년미만"
    else:
        return "10년이상"

def categorize_service_years_num(service_year) :
    one = ["1개월미만","1개월~2개월미만","3개월~4개월미만","4개월~5개월미만","6개월미만"]
    two = ["6개월~1년"]
    three  = ["1~2년","1년~2년미만"]
    four = ["2~3년","2년~3년미만"]
    five = ["3~4년","3년~4년미만"]
    six = ["4~5년","4년~5년"]
    seven = ["5~10년","5년~10년"]

    if service_year in one :
        return 1
    elif service_year in two :
        return 2
    elif service_year in three :
        return 3
    elif service_year in four :
        return 4
    elif service_year in five :
        return 5
    elif service_year in six :
        return 6
    elif service_year in seven :
        return 7
    else:
        return 8

# def categorize_age(age) :
#     if age < 18 :
#         return "18세미만"
#     elif 18 <= age <= 24 :
#         return "19~24세이하"
#     elif 25 <= age <= 29 :
#         return "25~29세이하"
#     elif 30 <= age <= 34 :
#         return "30~34세이하"
#     elif 35 <= age <= 39 :
#         return "36~39세이하"
#     elif 40 <= age <= 44 :
#         return "40~44세이하"
#     elif 45 <= age <= 49 :
#         return "45~49세이하"
#     elif 50 <= age <= 54 :
#         return "50~54세이하"
#     elif 55 <= age <= 59 :
#         return "55~59세이하"
#     else:
#         return "60세이상"
    
# def categorize_age_num(age) :
#     if age < 18 :
#         return 1
#     elif 18 <= age <= 24 :
#         return 2
#     elif 25 <= age <= 29 :
#         return 3
#     elif 30 <= age <= 34 :
#         return 4
#     elif 35 <= age <= 39 :
#         return 5
#     elif 40 <= age <= 44 :
#         return 6
#     elif 45 <= age <= 49 :
#         return 7
#     elif 50 <= age <= 54 :
#         return 8
#     elif 55 <= age <= 59 :
#         return 9
#     else:
#         return 10


def categorize_scale(scale) :
    one = ["100인~299인","100인~499인"]
    two = ["10인~99인","50인~99인"]
    three = ["9인~50인"]
    if scale in one :
        return "200인이상"
    elif scale in two :
        return "50~100미만"
    elif scale in three :
        return "9~50인미만"
    else :
        return "9인미만"

#소소(9인 미만) : 4 
#소(9~50인 미만) : 3
#중(50인~200인미만) : 2
#대(200인이상) : 1
def categorize_scale_num(scale) :
    one = ["100인~299인","100인~499인"]
    two = ["10인~99인","50인~99인"]
    three = ["9인~50인"]
    if scale in one :
        return 1
    elif scale in two :
        return 2
    elif scale in three :
        return 3
    else :
        return 4

#2시간 간격으로 변경
def categorize_time(time) : 
  if 0 <= time < 2:
      return "0~2시" 
  if 2 <= time < 4:
      return "2~4시"
  if 4 <= time < 6:
      return "4~6시" 
  if 6 <= time < 8:
      return "6~8시"  
  if 8 <= time < 10:
      return "8~10시" 
  if 10 <= time < 12:
      return "10~12시" 
  if 12 <= time < 14:
      return "12~14시" 
  if 14 <= time < 16:
      return "14~16시"  
  if 16 <= time < 17:
      return "16~18시"
  if 18 <= time < 20:
      return "18~20시" 
  if 20 <= time < 22:
      return "20~22시"   
  return "22시~24시"

#한국산업안전보건공단_시간대별 사고사망수 순서로 숫자 매김
def categorize_time_num(time) :
  if 0 <= time < 2:
      return 5
  if 2 <= time < 4:
      return 1
  if 4 <= time < 6:
      return 3
  if 6 <= time < 8:
      return 7
  if 8 <= time < 10:
      return 11
  if 10 <= time < 12:
      return 12
  if 12 <= time < 14:
      return 9
  if 14 <= time < 16:
      return 10
  if 16 <= time < 18:
      return 8
  if 18 <= time < 20:
      return 6
  if 20 <= time < 22:
      return 2
  return 4

def categorize_day_num(day) :
  if day == "월" :
      return 1
  if day == "화" :
      return 2
  if day == "수" :
      return 3
  if day == "목" :
      return 4
  if day == "금" :
      return 5
  if day == "토" :
      return 6
  return 7
