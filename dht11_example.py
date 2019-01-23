import RPi.GPIO as GPIO
import dht11 #`センサーライブラリ読み込み`
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False) # ワーニング非表示
GPIO.setmode(GPIO.BCM) # GPIOの数字で指定
GPIO.cleanup()          # GPIOの設定を初期化

# read data using pin 14　データ読み込みのPIN番号を設定する
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read() # センサーからデータを取得
    if result.is_valid():    #　センサーからデータが取得できたかを判定
    　　#コンソール出力
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)
