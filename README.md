samchuck quant 사용법


1. data/stocklist에 크롤링할 주식 코드 선택
   ( 현재  Dtata는 3개월에 한번씩 키움증권 영웅문에서 1차 필터링 한 Data를 사용하고 있다. 
      Data는 추가만 하고 삭제는 하지 않는다. 3개월에 한번씩 계속 추가되는 Data 있다.  )
    키움증권의 필터링은 
       영업이익 - 최근 결산 1억원 이상
       PBR - 최근 결산 하위 500개
       PBR - 최근 결산 0.01배 이상
       EPS - 최근 결산 1월 이상
       PSR - 최근 결산 0배 이상 
    이다. 즉... 흑자나는 기업중 PBR 이 낮은 하위 500개 주식

    stocklist.txt 파일은 아래와 같이 구성된다. 

000050
000070
000120
000140
000150
000180
000210

와 같이 주식 코드들이 들어가게 된다. 


2. stock_crawl.py 를 이용해서 크롤링

    url = 'https://finance.naver.com/item/main.nhn?code=' + line

의 html data를 가져와서 파싱 하여 stdout 으로 출력한다. 

크롤링 하면 아래와 같은 data가 생성된다. 

000050 경방 10,700 27,415,270 43.15 0.35 0 2,933
000070 삼양홀딩스 71,900 8,564,271 7.33 0.32 0 6,158
000120 CJ대한통운 90,200 22,812,344 10.20 0.49 0 2577
000140 하이트진로홀딩스 10,220 23,206,765 4.58 0.40 0 2,372
000150 두산 92,600 16,523,835 999 0.65 0 15,301
000180 성창기업지주 2,215 69,751,600 999 0.27 0 1,545
000210 DL 61,000 20,955,884 34.44 0.32 0 12,783

해당 data를 적절한 txt 로 저장하여 excel로 가공하여 사용한다. 

해당 Data는 각각

코드 / 종목명 / 크롤링 당시 주가 / 주식수 / PER / PBR / 배당수익률 / 시가총액
이다.

( 2023년 2월 data는 네이버 웹페이지에서 배당수익률이 제대로 나오지 않아서 해당 data는 제외하고 순위를 구했다.)




3. 엑셀로 분석하여 순위 정하기 / 필터링

엑셀 함수의 countif 를 사용하면 해당 순위를 계산할 수 있다
=COUNTIF($E$2:$E$442,"<="&E2)  --> 442개 중 몇위인지 계산

사용할 파라미터 3개를 sum 해서 종합 순위를 구한다. 
( per / pbr / 배당 수익률 )

엑셀 함수의 vlookup 함수를 사용하면 3개월 전의 순위와 비교해 볼 수 있다.

=VLOOKUP(A2,org_20220731!$A$2:$O$408,15,FALSE)
와 같은 함수 사용. 2번째 함목이 이전 data의 항목

사용한 엑셀은 data 디렉토리의 종목선정.xlx 파일에 있으니 참고하면 된다. 

일단 순위를 정한 뒤 내가 정한 필터링 방법은 다음과 같다. 

지주사 제외
금융사 / 증권사 제외
건설사 제외
적자회사 제외
대형주 제외

위 회사들을 제외하고 상위 회사들 순서대로 재무제표와 회사 개요를 읽어 보면서 선택한다. 

2023년 2월에 선정된 회사는 파란색, 보유주는 노란색... 
회사 선정 원칙이 계속 변하다가 이제 fix가 되어 아직 대형주 / 건설주 / 지주회사가 많이 섞여 있다


4. 매도 원칙 
   이익률 100% 가 넘어가면 익절한다. 
   손절 원칙은 안 정했고, 3달마다 한번씩 있는 rebalancing day 에 종합 순위가
   떨어지면 매도하는 걸로 손절을 대체한다.


5. 리밸런싱
   현재 주식총액 / 주식종목수
   에 맞추어 시장가로 매수 / 매도를 진행한다. 
    


