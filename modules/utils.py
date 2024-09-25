

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
        "소소": "9인 이하",
        "소": "10인~99인 이하",
        "중": "100인~499인 이하",
        "대": "500인 이상"
    }
    return scale_map.get(scale, "None")

'''
카테고리화
'''

#근속연수 카테고리
def categorize_service_years(service_year) :
    service_year = service_year.strip()
    one = ["1개월미만","1개월~2개월미만","3개월~4개월미만","4개월~5개월미만","6개월~1년","6개월미만"]
    two = ["1~2년","1년~2년미만"]
    three = ["2~3년","2년~3년미만"]
    four = ["3~4년","3년~4년미만"]
    five = ["4~5년","4년~5년"]
    six = ["5~10년","5년~10년"]

    if service_year in one :
        return "1년미만"
    elif service_year in two :
        return "1~2년미만"
    elif service_year in three :
        return "2~3년미만"
    elif service_year in four :
        return "3~4년미만"
    elif service_year in five :
        return "4~5년미만"
    elif service_year in six :
        return "5~10년미만"
    else:
        return "10년이상"

def categorize_service_years_num(service_year) :
    one = ["1개월미만","1개월~2개월미만","3개월~4개월미만","4개월~5개월미만","6개월~1년","6개월미만"]
    two = ["1~2년","1년~2년미만"]
    three = ["2~3년","2년~3년미만"]
    four = ["3~4년","3년~4년미만"]
    five = ["4~5년","4년~5년"]
    six = ["5~10년","5년~10년"]

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
    else:
        return 7

def categorize_age(age) :
    if age < 18 :
        return "18세미만"
    elif 18 <= age <= 24 :
        return "19~24세이하"
    elif 25 <= age <= 29 :
        return "25~29세이하"
    elif 30 <= age <= 34 :
        return "30~34세이하"
    elif 35 <= age <= 39 :
        return "36~39세이하"
    elif 40 <= age <= 44 :
        return "40~44세이하"
    elif 45 <= age <= 49 :
        return "45~49세이하"
    elif 50 <= age <= 54 :
        return "50~54세이하"
    elif 55 <= age <= 59 :
        return "55~59세이하"
    else:
        return "60세이상"
    
def categorize_age_num(age) :
    if age < 18 :
        return 1
    elif 18 <= age <= 24 :
        return 2
    elif 25 <= age <= 29 :
        return 3
    elif 30 <= age <= 34 :
        return 4
    elif 35 <= age <= 39 :
        return 5
    elif 40 <= age <= 44 :
        return 6
    elif 45 <= age <= 49 :
        return 7
    elif 50 <= age <= 54 :
        return 8
    elif 55 <= age <= 59 :
        return 9
    else:
        return 10

def categorize_scale(scale) :
    one = ["9인이하"]
    two = ["10인~99인이하","50인~99인"]
    three = ["100인~299인이하","100인~499인이하"]
    if scale in one :
        return "9인"
    elif scale in two :
        return "10인~9인이하"
    elif scale in three :
        return "100인~499인이하"
    else :
        return "500인이상"

def categorize_scale_num(scale) :
    one = ["9인이하"]
    two = ["10인~99인이하","50인~99인"]
    three = ["100인~299인이하","100인~499인이하"]
    if scale in one :
        return 1
    elif scale in two :
        return 2
    elif scale in three :
        return 3
    else :
        return 4

def categorize_time(time) :
  if 0 <= time < 6:
      return "0~6시" 
  if 6 <= time < 8:
      return "6~8시" 
  if 8 <= time < 12:
      return "8~12시"  
  if 12 <= time < 13:
      return "12~13시"
  if 13 <= time < 18:
      return "13~18시" 
  if 18 <= time < 21:
      return "18~21시"   
  return "21시~24시"

def categorize_time_num(time) :
  if 0 <= time < 6:
      return 1
  if 6 <= time < 8:
      return 2 
  if 8 <= time < 12:
      return 3 
  if 12 <= time < 13:
      return 4
  if 13 <= time < 18:
      return 5 
  if 18 <= time < 21:
      return 6  
  return 7

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
