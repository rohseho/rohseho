#=============================================================================
### 업비트 자동매매 _변동성+ 이평선  /// 완성 :; 실제 계좌 연동 테스트 해봐야 함...
#==============================================================================
#자동매매 AzyT#
import time
import pyupbit
import datetime

access = "~~bqEGn7bwAWDvPOUUxxaAltzI6Qzr59KJd7Qznw"
secret = "~~xPykYudZ9cxpw0OrpxmH6dv1HiSZumCNW9B9Qr"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

#----------내가 수정함(시작 시간, end시간)---------------------------------
#def get_start_time(ticker):
#  """시작 시간 조회"""
#now = datetime.datetime.now()
#start_time = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(0.375)    # 시작은 오늘날짜 9시부터~~ (9시간/24시간)
#return start_time
#---------------------------------------------------~~~~~~~~~~~~~~~~~~~~~~~~-----

def get_ma15(ticker):                            ### 이동평균선 확인  ##########
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(0.375)    # 시작은 오늘날짜 9시부터~~ (9시간/24시간)
        end_time = start_time + datetime.timedelta(days=1)    # 종료는 그다음날 오전 9시 

         # 09:00 < 현재시간 < 08:59:50 일때 거래를 함
        if start_time < now < end_time - datetime.timedelta(seconds=10):  # 시작과 끝이 동일한 9시가 아닌, 8시59분50초에 종료
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")                                     # ma15에 대해 정의 해줌 
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:     ### 현재가가 target 보다 높으면서, 15일 이동평균 위에 있을 경우 매수
                krw = get_balance("KRW")                                   #  계좌 잔고가 5천원 이상이며, BTC을 매수
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)      # 수수료 0.05% 감안하여 1보다 그만큼 적게 설정함
        else:                                                          #  현재시간 이 08:59:50부터 종가에 전량 매도처리함
            btc = get_balance("BTC")                                   #  BTC잔고를 확인해서 0.00008( 약 5천원)이상이면 매도처리함
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
