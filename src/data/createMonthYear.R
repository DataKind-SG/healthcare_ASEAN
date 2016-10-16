# R Script created on DataJam (27 Aug 2016) to convert SG weekly disease data to monthly series

setwd("~/../../Desktop/healthcare_ASEAN/Data")
library(zoo)
library(dplyr)
dat<-read.csv("weekly-infectious-bulletin-cases (1).csv",stringsAsFactors=FALSE)
# Subset data for dengue, malaria
dat<-dat[grep("Dengue|Malaria",dat$disease),]
temp<-strsplit(dat$epi_week,"-W")

# take year
dat$Year<-sapply(temp,function(x){x[[1]]})

# take week
dat$Week<-sapply(temp,function(x){x[[2]]})
rm(temp)

# convert week 53 to week 52
dat$Week[dat$Week==53]<-52

# Create new var weekyear
dat$monthYear<-as.Date(as.yearmon(paste(0,dat$Week, dat$Year, sep = "-"),"%w-%W-%Y"))

# Aggregate to monthly by summing
dat<-dat %>% group_by(monthYear,disease) %>% summarise(totalCases=sum(number_of_cases,na.rm=TRUE))

# Write out data
write.csv(dat,file="SG_monthly_data.csv",row.names=FALSE)
