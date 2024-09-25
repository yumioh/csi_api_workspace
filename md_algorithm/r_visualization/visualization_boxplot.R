
#default 경로 설정
setwd("C:/workplace/csi_api_workspace/md_algorithm/")
getwd()

install.packages()

#카테고리한 gh data 불려오기
gh_data = read.csv("./data/gh_categorize.csv")
kosha_data = read.csv("./data/kosha_categorize.csv")

#stat 데이터 보기
summary(gh_data)
summary(kosha_data)

#boxplot
# 최소값, 제1사분위수(25%), 증위값, 제3사분위수(75%), 최대값
boxplot(gh_data$공사규모, kosha_data$공사규모, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 공사 규모")
boxplot(gh_data$발생시간, kosha_data$발생시간, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 발생시간")
boxplot(gh_data$근무경력, kosha_data$근무경력, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 근무경력")
boxplot(gh_data$나이, kosha_data$근무경력, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 나이")
boxplot(gh_data$월별, kosha_data$월별, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 월별")
boxplot(gh_data$요일별, kosha_data$요일별, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 요일별")


