

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
