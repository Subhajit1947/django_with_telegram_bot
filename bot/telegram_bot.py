# telegram_bot.py
import requests
from django.conf import settings
from .models import TelegramUser

class TelegramBot:
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def handle_update(self, update):
        if 'message' in update and 'text' in update['message']:
            message = update['message']
            if message['text'] == '/start':
                self.handle_start_command(message)

    def handle_start_command(self, message):
        user_data = message['from']
        
        TelegramUser.objects.update_or_create(
            telegram_id=user_data['id'],
            defaults={
                'username': user_data.get('username'),
            }
        )
        
        self.send_message(
            chat_id=message['chat']['id'],
            text=f"Hello {user_data.get('first_name', 'there')}! You've been registered."
        )

    def send_message(self, chat_id, text):
        url = f"{self.base_url}/sendMessage"
        data = {'chat_id': chat_id, 'text': text}
        requests.post(url, json=data)