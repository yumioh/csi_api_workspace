
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
box <- boxplot(gh_data$공사규모, kosha_data$공사규모, names = c("비사고데이터", "사고데이터"), main = "공사규모 BOXPLOT", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$발생시간, kosha_data$발생시간, names = c("비사고데이터", "사고데이터"), main = "발생시간 BOXPLOT", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$근무경력, kosha_data$근무경력, names = c("비사고데이터", "사고데이터"), main = "근무경력 BOXPLOT", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$나이, kosha_data$나이, names = c("비사고데이터", "사고데이터"), main = "나이 BOXPLOT", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$월별, kosha_data$월별, names = c("비사고데이터", "사고데이터"), main = "월별 BOXPLOT", col = c("#F2E64D","#19396d"))
box <- boxplot(gh_data$요일별, kosha_data$요일별, names = c("비사고데이터", "사고데이터"), main = "요일별 BOXPLOT", col = c("#F2E64D","#19396d"))

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
gh_hist = hist(gh_data$나이, breaks = seq(1, 12), plot = FALSE)
kosha_hist = hist(kosha_data$나이, breaks = seq(1, 12), plot = FALSE)

#나이 
gh_hist = hist(gh_data$나이, plot = FALSE)
kosha_hist = hist(kosha_data$나이,plot = FALSE)
#ylim : y축 범위, adjustcolor : 불투명도, xaxt = "n"
plot(gh_hist, col=adjustcolor("#F2E64D", alpha=0.9), xlab="", main = "나이 Histogram",
     ylab="빈도", ylim=c(0, max(65000, kosha_hist$counts)))
plot(kosha_hist, col=adjustcolor("#19396d", alpha=0.9), add = TRUE)

# 범례 추가 cex: FONT SIZE, toright : 범례 위치
legend("topright", legend=c("비사고 데이터", "사고 데이터"), fill=c(adjustcolor("#F2E64D", alpha=0.5), adjustcolor("#19396d", alpha=0.8)), cex=0.8)

#공사규모 x축 레이블 추가
axis(1, at=c(1:4), labels=c("200명 이상", "50~200인 미만", "9인~50인 미만", "9인 미만"), cex.axis=0.8)

#발생시간 x축 레이블 추가
axis(1, at = c(1:12), labels=c("2~4시","20~22시","4~6시","22~24시","0~2시","18~20시","6~8시","16~18시","12~14시","14~16시","8~10시","10~12시"), cex.axis = 0.8)

#근무경력 x축 레이블 추가
axis(1, at = c(1:8), labels=c("6개월미만","6개월~1년미만","1~2년미만","2~3년미만","3~4년미만","4~5년미만","5~10년미만","10년이상"), cex.axis = 0.8)

#나이 x축 레이블 추가
#axis(1, at = c(1,2,3,4,5,6,7,8,9,10), labels=c("18세미만","19~24세이하","25~29세이하","30~34세이하","35~39세이하","40~44세이하","45~49세이하","50~54세이하","55~59세이하","60세이상"), cex.axis = 0.8)
axis(1, at=seq(min(gh_hist$breaks), max(gh_hist$breaks), by=5), labels=seq(min(gh_hist$breaks), max(gh_hist$breaks), by=5))

#월별이 x축 레이블 추가
axis(1, at = c(1,2,3,4,5,6,7,8,9,10,11,12), labels=c("1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"), cex.axis = 0.8)

#요일별 x축 레이블 추가
axis(1, at = c(1,2,3,4,5,6,7), labels=c("월","화","수","목","금","토","일"), cex.axis = 0.8)


#######bar그래프 그리기 ############

# 고정된 위치를 위한 계산
n_groups <- length(all_times)   # 실제 그룹의 수
group_width <- 2                # 막대 간격
start_position <- 1             # 시작 위치
positions <- seq(from=start_position, by=group_width, length.out=n_groups)

# 비사고 데이터와 사고 데이터의 발생시간 값 빈도 계산
gh_freq <- table(gh_data$나이)         
kosha_freq <- table(kosha_data$나이)

# gh_freq와 kosha_freq의 이름을 숫자형으로 변환해 정렬
####나이 레이블이 순서가 마지 않아 변경을 위해 작성 
gh_freq_sorted <- gh_freq[order(as.numeric(names(gh_freq)))]
kosha_freq_sorted <- kosha_freq[order(as.numeric(names(kosha_freq)))]

# 비사고 데이터와 사고 데이터에서 발생한 고유한 발생시간 값을 중복 없이, 오름차순으로 정렬한 값
# sort : 정렬 unique : 중복된 값 제거 
# 발생시간의 모든 범위 확보
all_times <- sort(unique(c(names(gh_freq), names(kosha_freq)))) 

####나이 레이블이 순서가 마지 않아 변경을 위해 작성 
all_times <- sort(as.numeric(unique(c(names(gh_freq_sorted), names(kosha_freq_sorted)))))

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
bp <- barplot(combined_data, 
        beside = TRUE,                    # 막대를 나란히 배치
        col = c("#F2E64D", "#19396d"),    # 각각의 색상 지정
        main = "나이 barplot",
        ylim = c(0,5000),
        ylab = "빈도", 
        xlab = "나이",
        xaxt = "n") #x축 레이블 없애기 

# 범례 추가
legend("topright", 
       legend = c("비사고 데이터", "사고데이터"), 
       fill = c("#F2E64D", "#19396d"), 
       cex = 0.8)


#1: x축, 2:y축, colMeans : 중앙에 배치
#공사규모
axis(1, at=colMeans(bp), labels=c("200명 이상", "50~200인 미만", "9인~50인 미만", "9인 미만"), cex.axis = 0.8)

#발생시간
axis(1, at=colMeans(bp), labels=c("2~4시","20~22시","4~6시","22~24시","0~2시","18~20시","6~8시","16~18시","12~14시","14~16시","8~10시","10~12시"), cex.axis = 0.8)

#근무경력 x축 레이블 추가
axis(1, at=colMeans(bp), labels=c("6개월미만","1년미만","1~2년미만","2~3년미만","3~4년미만","4~5년미만","5~10년미만","10년이상"), cex.axis = 0.8)

#월별이 x축 레이블 추가
axis(1, at=colMeans(bp), labels=c("1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"), cex.axis = 0.8)

#나이 x축 레이블 추가
#$axis(1, at=colMeans(bp), labels=c("18세미만","19~24세이하","25~29세이하","30~34세이하","35~39세이하","40~44세이하","45~49세이하","50~54세이하","55~59세이하","60세이상"), cex.axis = 0.8)
axis(1, at=colMeans(bp), labels=names(gh_freq_full), cex.axis = 0.8)

#요일별 x축 레이블 추가
axis(1, at=colMeans(bp), labels=c("월","화","수","목","금","토","일"), cex.axis = 0.8)



