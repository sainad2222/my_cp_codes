from math import *
def calcAngle(h,m): 
        if (h == 12): 
            h = 0
        if (m == 60): 
            m = 0
        hour_angle = 0.5 * (h * 60 + m) 
        minute_angle = 6 * m 
        angle = abs(hour_angle - minute_angle) 
        angle = min(360 - angle, angle) 
        return radians(angle)
a,b,h,m=map(int,input().split())
angle = calcAngle(h,m)
l=(b-a*cos(angle))**2
r1=a**2
r2=(a*cos(angle))**2
print('{0:.{1}f}'.format(sqrt(l+r1-r2),20))
# print("{0.20f}".format(sqrt(l+r1-r2)))