#! /usr/bin/env pyhton3

import ambient
import os

import RPi.GPIO as GPIO
import dht11
import time
import datetime


# initialize GPIO
GPIO.setwarnings(False) # ワーニング非表示
GPIO.setmode(GPIO.BCM) # GPIOの数字で指定
GPIO.cleanup() # GPIOの設定を初期化

# read data using pin 14　データ読み込みのPIN番号を設定する
instance = dht11.DHT11(pin=14)

# ambient環境変数設定
AMBIENT_CHANNEL_ID = int(os.environ['AMBIENT_CHANNEL_ID'])
AMBIENT_WRITE_KEY = os.environ['AMBIENT_WRITE_KEY']
CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '30'))

# ambientオブジェクト作成
am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)

latest_update = datetime.datetime.now() #処理開始時の時刻取得


while True:
    result = instance.read() # センサーからデータを取得
    if result.is_valid():    #　センサーからデータが取得できたかを判定

        if result.tick_last_update > latest_update:
            # データをAmbientに送信する
            am.send({
                'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'd1': result.temperature,
                'd2': result.humidity,
                }
            )

        latest_update = result.tick_last_update

        #コンソール出力
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    #time.sleep(CHECK_SPAN)
    time.sleep(1)
