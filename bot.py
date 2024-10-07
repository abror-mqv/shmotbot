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


message_template = """Здравствуйте, {name}!\n\nМы заметили, что вы интересуетесь покупкой текстильных изделий. Было бы удобно обсудить ваше сотрудничество?\n\nС уважением, Талгат Абдыганиев.
"""

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
            
            message = message_template.format(name=name)

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
            
            time.sleep(random.randint(1100,1900)) 
# Основной блок программы
with client:
    client.loop.run_until_complete(send_messages())