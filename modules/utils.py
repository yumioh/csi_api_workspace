

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
    else:
        return day
    

#공사규모 사람수 형태로 변환
def convert_scale_to_person_range(scale):
    scale_map = {
        "소소": "1인~9인",
        "소": "10인~99인",
        "중": "100인~499인",
        "대": "500인 이상"
    }
    return scale_map.get(scale, "None")
