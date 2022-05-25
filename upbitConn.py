
"""교제 : 파이썬을 이용한 비트코인 자동매매 (개정판) 
        ~ 라인 교재 :   https://wikidocs.net/21888 
        ~ https://github.com/sharebook-kr/book-cryptocurrency/tree/master/ch06

 %% 22.5월 22일 학습함"""
##############yT#######업비트 API연동 및 계좌 조회 ###AZ######

import pyupbit

access = "~~bqEGn7bwAWDvPOUUxxaAltzI6Qzr59KJd7Qznw"          # 내꺼 API연동 암호
secret = "~~xPykYudZ9cxpw0OrpxmH6dv1HiSZumCNW9B9Qr"          # 내꺼 API연동 암호
upbit = pyupbit.Upbit(access, secret)

print('한화-',upbit.get_balance("KRW"))         # 보유 현금 조회
print('BTC-',upbit.get_balance("KRW-BTC"))     # KRW-BTC조회
print('XRP-',upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print('ETH-',upbit.get_balance("KRW-ETH"))     # KRW-ETH 조회

print('~~~주요 코인 보유 내역~~~')

print(upbit.get_balances())             # 전계좌 조회, 데이터 테이블 형식
