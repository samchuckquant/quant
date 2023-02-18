# -*- coding: utf-8 -*-

import requests
from time import sleep


"""

#url = https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930
"""

def getStr(str, t1, t2) :
    r = ""
    
    p1 = str.find(t1)
#    print (p1)
    if p1 == -1 :
        return r
    s1 = str[p1+len(t1):]

    p2 = s1.find(t2)
#    print (p2)
    if p2 == -1 :
        return r
    
    r = s1[:p2]
    
    return r
    


#s1 = getStr(str, "기업개요(", ")</title>")
#s2 = getStr(str.replace(" ","").replace("\n","").replace("\t",""), "발행주식수/유동비율</th><tdclass=\"num\">", "주")


file = open("data/stocklist.txt", "r")

while True :
    line = file.readline()
    print (line)
    continue
    if not line :
        break

    url = 'https://finance.naver.com/item/main.nhn?code=' + line
    html = requests.get(url).text
    html = html.replace(" ","").replace("\n","").replace("\t","")
        
    p1 = getStr(html, "<dd>종목명", "</dd>")
    p2 = getStr(html, "<dd>현재가", "전일대비")
    p3 = getStr(html, "상장주식수</th><td><em>", "</em></td></tr>")
    
#    pers1 = "합산순이익을수정평균발행주식수로나눈값이며,보통주와우선주를합산해서계산합니다.</p><spanclass=\"arrow\"></span></div></div></th><td><emid=\"_per\">"

    p4 = getStr(html, "<emid=\"_per\">", "</em>")

#    pbrs1 = "BPS는최근분기자본총계를수정평균발행주식수로나눈값이며,보통주와우선주를합산해서계산합니다.</p><spanclass=\"arrow\"></span></div></div></th><td><emid=\"_pbr\">"

    p5 = getStr(html, "<emid=\"_pbr\">", "</em>")
    
    p6 = getStr(html, "<emid=\"_dvr\">", "</em>").replace("조", "")
    
    if p4 == "":
        p4 = "999"
        
    if p5 == "":
        p5 = "0"
        
    if p6 == "":
        p6 = "0"
        
    p7 = getStr(html,  "<emid=\"_market_sum\">", "</em>").strip().replace("조", "")

    if p7 == "":
        p7 = "0"
    
    print (line.replace("\n", ""), p1, p2, p3, p4, p5, p6, p7)
    
    
    
    sleep(0.3)
    
