from time import *

time=localtime()
yr=time[0]
mth=time[1]
day=time[2]
hr=time[3]
mins=time[4]
sec=time[5]
for i in range (6):
    if i==2 or i==5:
        print(time[i],end=' ')
    elif i>2 and i!=5:
        print(time[i],end=':')
    if i<2:
        print(time[i],end='-')
'''
yr=int(input())
mth=int(input())
day=int(input())
hr=int(input())
mins=int(input())
sec=int(input())
'''
def gregorian_to_julian(year, month, day):
    i = int((month - 14) / 12)
    jd = day - 32075
    jd += int((1461 * (year + 4800 + i)) / 4)
    jd += int((367 * (month - 2 - (12 * i))) / 12)
    jd -= int((3 * int((year + 4900 + i) / 100)) / 4)
    return jd
   
def jd_convert(godina, mjesec, dan, sati, minuta, sekunda):
    if (mjesec>=3 and mjesec<=10):
        if not (mjesec==3 and dan<28):
            if sati==0:
                sati=23
                dan+=1
            else:
                sati-=1              
    #sati-=1
    if sati<12:
        dan-=1
        sati+=12
    else:
        sati-=12
    #minuta-=1
    #sekunda-=12
    dec=((sekunda/3600)+(minuta/60)+sati)/24
    jd=gregorian_to_julian(godina,mjesec,dan)
    final=dec+jd
    final=str(round(final,6))
    return final

def jd_convert2(UTC, DST, godina, mjesec, dan, sati, minuta, sekunda):
    # if (mjesec>=3 and mjesec<=10):
    #    if not (mjesec==3 and dan<28):
    if DST == 'DA' and not UTC:  # oduzimanje sati ovisno o Daylight Savings Time (DST)
        if sati == 0:
            sati = 23
            dan += 1
        else:
            sati -= 1
    if not UTC:  # oduzimanje sati ovisno o vremenskoj zoni
        sati -= 1
    if sati < 12:  # konvertiranje UTC-a u GMAT
        dan -= 1
        sati += 12
    else:
        sati -= 12
    dec = ((sekunda / 3600) + (minuta / 60) + sati) / 24
    jd = gregorian_to_julian(godina, mjesec, dan)
    final = dec + jd
    final = str(round(final, 6))
    return final
print()	
print(jd_convert(yr,mth,day,hr,mins,sec))
print(jd_convert2(False,'NE',yr,mth,day,hr,mins,sec))
