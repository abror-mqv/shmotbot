import csv
import time
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, InputUserDeactivatedError
import random

# Вводим ваши данные
api_id = '29382353' 
api_hash = '9868ad42d5b06b05da36c62e45115f02'  
phone_number = '996227722777' 

# api_id = 21866422      
# api_hash = 'aedfe8a16ea63ddd2b2ac1937de8918c'   
# phone_number = '+996559808243'  


message_template_1 = """Здравствуйте, {name}!

Предлагаем услуги по пошиву одежды и текстиля в цехах Кыргызстана для оптовых покупателей. Гарантируем высокое качество, индивидуальный подход и конкурентные цены.

Готовы обсудить заказ? Свяжитесь с нами в ответ на это сообщение.

С уважением,
Талгат Абдыганиев
"""

message_template_2 = """Приветствую, {name}!

Предлагаем вам услуги по пошиву текстиля и одежды оптом на наших производствах в Кыргызстане. Обеспечиваем высокое качество, внимательное отношение к заказам и гибкие ценовые предложения.

Будем рады обсудить ваш заказ. Напишите в ответ на это сообщение!

С уважением,  
Талгат Абдыганиев. 
"""

message_template_3 = """Здравствуйте, {name}!

Мы специализируемся на пошиве одежды и текстильных изделий для оптовых покупателей в цехах Кыргызстана. Работаем с гарантией качества, предлагаем индивидуальный подход и выгодные цены.

Готовы обсудить ваш заказ? Ответьте на это сообщение.

С уважением,  
Талгат Абдыганиев. 
"""

message_template_4 = """Добрый день, {name}!

Наша команда занимается пошивом одежды и текстиля на заказ для оптовых клиентов в Кыргызстане. Мы предлагаем высокие стандарты качества, гибкость в работе и конкурентные цены.

Хотите обсудить детали сотрудничества? Свяжитесь с нами в ответ на это сообщение.

С уважением,  
Талгат Абдыганиев. 
"""


messages = [
    message_template_1, 
    message_template_2, 
    message_template_3, 
    message_template_4
]

# Инициализация клиента Telethon
client = TelegramClient(phone_number, api_id, api_hash)

# Функция для отправки сообщений пользователям
async def send_messages():
    with open('members-hackingfashion.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            username = row.get('username')  # Получаем username
            name = row['name']

            if not username:  # Пропускаем, если нет username
                print(f"Пропуск пользователя {name}, так как нет username.")
                continue
            
            message = random.choice(messages).message_template.format(name=name)

            try:
                print(f"Отправка сообщения для username {username} ({name})...")
                await client.send_message(username, message)
                print(f"Сообщение успешно отправлено для {username}")
            except PeerFloodError:
                print("ОШИБКА: Слишком много запросов, попробуйте позже.")
                break  # Остановка процесса рассылки при превышении лимитов
            except UserPrivacyRestrictedError:
                print(f"ОШИБКА: Пользователь {name} ограничил получение сообщений.")
            except InputUserDeactivatedError:
                print(f"ОШИБКА: Аккаунт пользователя {name} деактивирован.")
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {name}: {e}")
            
            time.sleep(600)  # Задержка в 2 секунды между отправками
# Основной блок программы
with client:
    client.loop.run_until_complete(send_messages())