import pyupbit
import numpy as np
                                                                      # 변동성 돌파 전략 백테스트,파이썬을 이용한 비트코인 자동매매 , 7-2장
df = pyupbit.get_ohlcv("KRW-BTC",count=120)                             # KRW, 최근 7일 가격( open, high,low,close,volume )

df['range'] = (df['high'] - df['low']) * 0.5                          # 변동폭 * K 계산 , (전일고가- 전일저가)* K값
df['target'] = df['open'] + df['range'].shift(1)                      # target(매수가)= 시작가 + 전일 변동폭 ~~ range 컬럼을 한칸씩 밑으로 내림(.shift(1)) : 즉 전일 
fee = 0.0005                                                          # 수수료


 # ror(수익율계산) / np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],                       #  조건문 참 즉 target보다 당일 고가가 높을때
                     df['close'] / df['target'] - fee,1)                #  매수 진행 하여, 수익률 계산되고, 조건이 거짓이며, 매수가 되지 않아, 수익율은 유지(1)
                    

df['hpr'] = df['ror'].cumprod()                                            # 누적 곱 계산(cumprod)->누적 수익률
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100     # Drow Down 계산(누적 최대 값과 현재 hpr 차이/누적 최대값*100)
print("MDD(%): ", df['dd'].max())

df.to_csv("dd1.csv")                                                       # CSV 파일 저장

# df.to_excel("dd.xlsx")                                                    # 엑셀파일 저장 오류 발새 중(ValueError: Excel does not support datetimes with timezones)

print(df)
