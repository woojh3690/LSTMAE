from scipy.stats import norm
from mpmath import csch

time = 0
기온 = 22
강수량 = 0

time_map = [1,1,1,1,1,1,2,3,4,10,4,3,4,3,2,2,2,4,10,4,3,2,2,2,1]

def cal_norm(x):
    return norm.pdf(x, loc=22, scale=6.5) * 1000

print("시간 :", time_map[time])
print("기온 :", cal_norm(기온))
print("강수량 :", csch(강수량+0.05))
print("예측 계수 :", time_map[time] * cal_norm(기온) * csch(강수량+0.05))