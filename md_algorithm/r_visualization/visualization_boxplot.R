
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

###### 히스토그램 그리기 ######

#histgram 그리기 plot = FALSE는 histogram을 그리지 않고 데이터만 계산
gh_hist = hist(gh_data$공사규모, plot = FALSE)
kosha_hist = hist(kosha_data$공사규모, plot = FALSE)

#ylim : y축 범위, adjustcolor : 불투명도
plot(gh_hist, col=adjustcolor("#F2E64D", alpha=0.8), ylim=c(0,65000), main = "공사규모 비교")
plot(kosha_hist, col=adjustcolor("#19396d", alpha=0.7), add = TRUE)

# 범례 추가 cex: FONT SIZE, toright : 범례 위치
legend("topright",legend=c("비사고데이터","사고데이터터"),fill=c("#F2E64D","#19396d"),cex = 0.6)



#######bar그래프 그리기 ############

# 비사고 데이터와 사고 데이터의 발생시간 값 빈도 계산
gh_freq <- table(gh_data$발생시간)         
kosha_freq <- table(kosha_data$발생시간)

# 비사고 데이터와 사고 데이터에서 발생한 고유한 발생시간 값을 중복 없이, 오름차순으로 정렬한 값
# sort : 정렬 unique : 중복된 값 제거 
# 발생시간의 모든 범위 확보
all_times <- sort(unique(c(names(gh_freq), names(kosha_freq))))  

# gh_freq와 kosha_freq 모두에 대해 발생시간 범위를 일치시키기 위해 0으로 채워줌
gh_freq_full <- rep(0, length(all_times))
#벡터에 이름 부여
names(gh_freq_full) <- all_times
#실제 빈도의 값 이름에 맞춰서 채우기
gh_freq_full[names(gh_freq)] <- gh_freq

kosha_freq_full <- rep(0, length(all_times))
names(kosha_freq_full) <- all_times
kosha_freq_full[names(kosha_freq)] <- kosha_freq

# 두 데이터를 나란히 결합
combined_data <- rbind(gh_freq_full, kosha_freq_full)

# 두 데이터를 나란히 그리기
barplot(combined_data, 
        beside = TRUE,                    # 막대를 나란히 배치
        col = c("#F2E64D", "#19396d"),    # 각각의 색상 지정
        main = "발생시간 빈도 비교",
        ylim = c(0,65000),
        ylab = "빈도", 
        xlab = "발생시간")

# 범례 추가
legend("topright", 
       legend = c("비사고 데이터", "사고 데이터"), 
       fill = c("#F2E64D", "#19396d"), 
       cex = 0.8)

