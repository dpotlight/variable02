
# 켄타우리는 지구로부터 40 * 10**12km
#빛의 속도로 프록시마 켄타우리까지 간다면 시간이 얼마나 걸리는지 광년 단위로 계산해보자     
#빛의속도: 30000km/sec
#광년 : 빛이 1년에 진행하는 거리


distance = 40e12 #거리   
#시간 = 거리 / 속력
velocity = 30000리 #속력    

time = distance / velocity #시간    
light_year = time / (60.0*60.0*24.0*365) #단위를 km/sec --> 광년    
print('프록시마 켄타우리 별까지 걸리는 시간은 %s광년입니다' %light_year)

