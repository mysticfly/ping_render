import requests
import time

while True:
    try:
        requests.get('https://test-crypto-notify-2.onrender.com/notify')
        print('Сайт работает нормально') # вставьте код, который выполняется, когда сайт работает
    except:
        print('Сайт не работает!') # вставьте код, который выполняется, когда сайт не работает
        # можно добавить дополнительные действия, например отправить уведомление или перезапустить сайт
    time.sleep(20) # 600 секунд = 10 минут
    
if __name__ == '__main__':
    app.run()
