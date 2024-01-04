from django.shortcuts import render
from django.conf import settings 
from telebot import TeleBot, types
from apps.contact.models import Contact
from config import token, ADMIN, group_chat_id
# Create your views here.


bot = TeleBot(token, threaded=False)
admin = ADMIN

@bot.message_handler(commands='start')
def start(message:types.Message):
    # TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    bot.send_message(message.chat.id, f'Салам {message.from_user.full_name}')
    
class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_text(message, order_id):
    keyboard = types.InlineKeyboardMarkup()
    accept_button = types.InlineKeyboardButton("Принять", callback_data=f'accept_{order_id}')
    decline_button = types.InlineKeyboardButton("Отклонить", callback_data=f'decline_{order_id}')
    keyboard.add(accept_button, decline_button)

    bot.send_message(group_chat_id, message, reply_markup=keyboard)


def get_text_doctor(message, id):
    bot.send_message(id, message)
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('accept'))
def handle_accept_callback(call: types.CallbackQuery):
    order_id = call.data.split('_')[-1]
    contact = Contact.objects.get(id=order_id)

   
    if contact.is_accepted:
        bot.answer_callback_query(call.id, 'Заказ уже был принят!')
    else:
        
        contact.status = 'Принят'
        contact.is_accepted = True
        contact.save()

       
        user_info = bot.get_chat_member(group_chat_id, call.from_user.id)

       
        bot.send_message(group_chat_id, f'{user_info.user.first_name} принял заказ {order_id}!')
        bot.answer_callback_query(call.id, 'Заказ принят!')

    if call.data.startswith('decline'):
        contact.status = 'Отклонен' 
        contact.save()  



@bot.callback_query_handler(func=lambda call: call.data.startswith('complete'))
def handle_complete_callback(call: types.CallbackQuery):
    order_id = call.data.split('_')[-1]
    contact = Contact.objects.get(id=order_id)

    bot.send_message(call.from_user.id, f'Заказ {order_id} завершен.')
    contact.status = "Завершен"
    contact.save()

    bot.send_message(call.from_user.id, f'Спасибо за ваш заказ {order_id}! Заказ успешно завершен.')


@bot.message_handler()  
def echo(message:types.Message):
    bot.send_message(message.chat.id, "Я вас не понял")
    
