## best K값 구하기 ##
import pyupbit
import numpy as np
import time

ticker='KRW-BTC'                                                                 ## ticker 변수화
peorid=14                                                                      ## 백테스트 기간 변수화

print(ticker,'-',peorid)

def get_ror(k=0.5):
   #df = pyupbit.get_ohlcv("KRW-XRP",count=100)                         #  리플 백테스트 기간, 최근 몇 일간 기준으로 최적의 K값 구함 
    df = pyupbit.get_ohlcv(ticker,count=peorid)                           ##### ticker 및 백테스트 기간 
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0005
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.1, 0.1):                                      # 0.1부터 1.1까지 0.1씩 증가함 
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))

time.sleep(1.1)
#######################################################
ticker='KRW-XRP'
print(ticker,'-',peorid)

def get_ror(k=0.5):
   #df = pyupbit.get_ohlcv("KRW-XRP",count=100)                         #  리플 백테스트 기간, 최근 몇 일간 기준으로 최적의 K값 구함 
    df = pyupbit.get_ohlcv(ticker,count=peorid)   
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0005
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.1, 0.1):                                      # 0.1부터 1.1까지 0.1씩 증가함 
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))

time.sleep(1.1)
#######################################################
ticker='KRW-ETH'
print(ticker,'-',peorid)

def get_ror(k=0.5):
   #df = pyupbit.get_ohlcv("KRW-XRP",count=100)                         #  리플 백테스트 기간, 최근 몇 일간 기준으로 최적의 K값 구함 
    df = pyupbit.get_ohlcv(ticker,count=peorid)   
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0005
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.1, 0.1):                                      # 0.1부터 1.1까지 0.1씩 증가함 
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
