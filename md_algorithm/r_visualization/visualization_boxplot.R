
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

#boxplot 그래프 그리기
box <- boxplot(gh_data$공사규모, kosha_data$공사규모, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 공사 규모", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$발생시간, kosha_data$발생시간, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 발생시간", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$근무경력, kosha_data$근무경력, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 근무경력", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$나이, kosha_data$근무경력, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 나이", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$월별, kosha_data$월별, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 월별", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$요일별, kosha_data$요일별, names = c("비사고데이터", "사고데이터"), main = "비사고 vs 사고데이터 요일별", col = c("#F2E64D","#19396d"))

#boxplot 통계값
box_stats <- box$stats 
# 최소값, 제1사분위수(25%), 중위수, 제3사분위수(75%), 최대값 boxplot에 표기
text(x = c(1.5, 2.5), y = box_stats[1,], labels = round(box_stats[1,], 2), col = "Red", cex = 0.9, font=2)
text(x = c(1.5, 2.5), y = box_stats[2,], labels = round(box_stats[2,], 2), col = "Red", cex = 0.9, font=2)
text(x = c(1.5, 2.5), y = box_stats[3,], labels = round(box_stats[3,], 2), col = "Red", cex = 0.9, font=2)
text(x = c(1.5, 2.5), y = box_stats[4,], labels = round(box_stats[4,], 2), col = "Red", cex = 0.9, font=2)
text(x = c(1.5, 2.3), y = box_stats[5,], labels = round(box_stats[5,], 2), col = "Red", cex = 0.9, font=2)