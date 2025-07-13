import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading


import threading
import time
from telebot import types

stopuser = {}
token = '7703376251:AAHNKBwal_K85gA68Vd-FuhNOGihD9askrA'
bot=telebot.TeleBot(token,parse_mode="HTML")
bot_working=True

admin=5268530944

myid = ['871257147']

admins = ['871257147']


private_group_id = -1002357494667

approved_group_id = -1002465740460


mainc = "https://t.me/Otp_ninja1_bot"  # تأكد من أن الرابط صحيح


cache_file = "bin_cache.json"






import telebot
from telebot.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton, PreCheckoutQuery
from datetime import datetime, timedelta
import json

# Default subscription prices
prices_file = "prices.json"

# Load prices from file or use defaults
def load_prices():
    try:
        with open(prices_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"ho": 8, "da": 50, "mo": 80}

def save_prices(prices):
    with open(prices_file, "w") as file:
        json.dump(prices, file, indent=4)

prices = load_prices()

# Bot token and Admin ID

ADMIN_ID = 871257147

# Command to update prices
@bot.message_handler(func=lambda message: message.text.lower().startswith("/set"))
def set_prices(message):
    global prices
    if message.chat.id != ADMIN_ID:
        bot.reply_to(message, "You are not authorized to perform this action.")
        return

    command = message.text.replace("/set", "").strip()
    for line in command.splitlines():
        if line.startswith("1"):
            prices["ho"] = int(line.split()[1])
        elif line.startswith("2"):
            prices["da"] = int(line.split()[1])
        elif line.startswith("3"):
            prices["mo"] = int(line.split()[1])

    save_prices(prices)
    bot.reply_to(
        message,
        f"Prices updated successfully:\n"
        f"- 1 Hour: {prices['ho']} 🌟\n"
        f"- 1 Day: {prices['da']} 🌟\n"
        f"- 1 Week: {prices['mo']} 🌟"
    )

# Show subscription options
@bot.message_handler(func=lambda message: message.text.lower().startswith(".buy") or message.text.lower().startswith("/buy"))
def respondn_to_vhk(message):
    kk = InlineKeyboardMarkup(row_width=1)
    cmm = InlineKeyboardButton(f"~ 1 hour • {prices['ho']}🌟", callback_data='hour')
    cm = InlineKeyboardButton(f"~ 1 day • {prices['da']}🌟", callback_data='day')
    cm1 = InlineKeyboardButton(f"~ 2 day • {prices['mo']}🌟", callback_data='week')
    kk.add(cmm, cm, cm1)
    bot.reply_to(
        message,
        f'''- Auto Pay ~ ✅                                    
~ VIP Subscribe ~                                    
- 1 hour: {prices['ho']} 🌟                                    
- 1 day: {prices['da']} 🌟                                    
- 2 day: {prices['mo']} 🌟                                    ''',
        reply_markup=kk
    )

# Handle callback for hour subscription
@bot.callback_query_handler(func=lambda call: call.data == 'hour')
def menu_callback_hour(call):
    Sid = call.from_user.id
    title = 'Bot Ninja VIP'
    expire = datetime.now() + timedelta(hours=1)
    price = [LabeledPrice(label=title, amount=prices['ho'])]  # No multiplication
    bot.send_invoice(
        chat_id=Sid,
        title=title,
        description="~ Bot Ninja VIP Subscribe",
        invoice_payload=f"{expire}",
        provider_token="",
        currency="XTR",
        prices=price
    )

# Handle callback for day subscription
@bot.callback_query_handler(func=lambda call: call.data == 'day')
def menu_callback_day(call):
    Sid = call.from_user.id
    title = 'Bot Ninja VIP'
    expire = datetime.now() + timedelta(hours=24)
    price = [LabeledPrice(label=title, amount=prices['da'])]  # No multiplication
    bot.send_invoice(
        chat_id=Sid,
        title=title,
        description="~ Bot Ninja VIP Subscribe",
        invoice_payload=f"{expire}",
        provider_token="",
        currency="XTR",
        prices=price
    )

# Handle callback for week subscription
@bot.callback_query_handler(func=lambda call: call.data == 'week')
def menu_callback_week(call):
    Sid = call.from_user.id
    title = 'Bot Ninja VIP'
    expire = datetime.now() + timedelta(hours=48)
    price = [LabeledPrice(label=title, amount=prices['mo'])]  # No multiplication
    bot.send_invoice(
        chat_id=Sid,
        title=title,
        description="~ Bot Ninja VIP Subscribe",
        invoice_payload=f"{expire}",
        provider_token="",
        currency="XTR",
        prices=price
    )

# Handle checkout
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query: PreCheckoutQuery):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Handle successful payment
@bot.message_handler(content_types=['successful_payment'])
def successful_payment_handler(message):
    user_id = message.chat.id
    amount_paid = message.successful_payment.total_amount
    if amount_paid == prices["ho"]:
        duration_hours = 1
        plan = '1 Hour Subscription'
    elif amount_paid == prices["da"]:
        duration_hours = 24
        plan = '1 Day Subscription'
    elif amount_paid == prices["mo"]:
        duration_hours = 48
        plan = '2 Days Subscription'
    else:
        bot.send_message(user_id, "Invalid payment amount.")
        return

    expiration_time = datetime.now() + timedelta(hours=duration_hours)
    expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")

    # Save subscriber data
    try:
        with open("data.json", "r") as file:
            subscribers = json.load(file)
    except FileNotFoundError:
        subscribers = {}

    subscribers[str(user_id)] = {
        "timer": expiration_time_str,
        "plan": plan
    }

    with open("data.json", "w") as file:
        json.dump(subscribers, file, indent=2, ensure_ascii=False)

    bot.send_message(
        user_id,
        f"✅ Payment successful!\nYour subscription expires on {expiration_time_str}."
    )

    # Notify admin
    try:
        chat = bot.get_chat(user_id)
        frs = chat.first_name
        use = chat.username
        user_display = f"Name: {frs}\nUsername: @{use}" if use else f"Name: {frs}\nUsername: Not Available"
    except Exception:
        user_display = "Name: Unknown\nUsername: Unknown"

    bot.send_message(
        ADMIN_ID,
        f"📢 New Subscriber:\n"
        f"- User ID: {user_id}\n"
        f"- Plan: {plan}\n"
        f"- Expiration: {expiration_time_str}\n"
        f"{user_display}"
    )















command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
def man_function(message):
    def my_function():
        name = message.from_user.first_name
        user_id = message.from_user.id

        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        try:
            BL = json_data[str(user_id)]['plan']
        except KeyError:
            BL = 'Free - Not Subscribed'
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            new_data = {
                user_id: {
                    "plan": "Free - Not Subscribed",
                }
            }

            existing_data.update(new_data)
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

        if BL == 'Free - Not Subscribed':    
            # يمكنك هنا حذف أو تعديل الجزء الذي يتعلق برسالة الترحيب
            pass  # لا ترسل أي رسالة ترحيبية في حالة عدم الاشتراك
        
        else:
            # يمكنك هنا حذف أو تعديل الجزء الذي يتعلق برسالة الترحيب عند الاشتراك
            pass  # لا ترسل أي رسالة ترحيبية في حالة الاشتراك النشط
    
    my_thread = threading.Thread(target=my_function)
    my_thread.start()
	
	
	

	
	

	

import json
import os
import time
from datetime import datetime, timedelta
from telebot import types

@bot.message_handler(content_types=["document"])
def main(message):
    name = message.from_user.first_name
    id = str(message.from_user.id)  # تحويل id إلى string للاستخدام كـ مفتاح في json
    
    # تحميل بيانات JSON
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    
    try:
        BL = json_data[str(id)]['plan']
    except KeyError:
        BL = 'Free - Not Subscribed'
    
    # تحقق من الاشتراك
    if BL == 'Free - Not Subscribed':
        update_user_data(id, 'Free - Not Subscribed')  # تحديث حالة المستخدم
        send_subscription_message(message)
        return
    
    # التحقق من وقت الاشتراك
    date_str = json_data[str(id)].get('timer', 'none').split('.')[0]
    try:
        provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except Exception:
        send_subscription_message(message)
        return

    current_time = datetime.now()
    required_duration = timedelta(hours=0)
    
    if current_time - provided_time > required_duration:
        send_expiration_message(message)
        update_user_subscription(id, 'none', 'Free - Not Subscribed')
        return
    
    # تحميل ملف الكومبو
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    user_combo_file = f"combo_{id}.txt"
    
    with open(user_combo_file, "wb") as w:
        w.write(downloaded_file)

    # إرسال قائمة البوابات المتاحة
    send_gateway_options(message)

def update_user_data(user_id, plan):
    with open('data.json', 'r') as json_file:
        existing_data = json.load(json_file)
    
    new_data = {
        user_id: {
            "plan": plan,
        }
    }
    existing_data.update(new_data)
    
    with open('data.json', 'w') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

def update_user_subscription(user_id, timer, plan):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    
    json_data[user_id]['timer'] = timer
    json_data[user_id]['plan'] = plan
    
    with open('data.json', 'w') as file:
        json.dump(json_data, file, indent=2)

def send_subscription_message(message):
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(text="♤ Programmers - Hasan", url="https://t.me/CHANNEL_NINJA_CHK")
    keyboard.add(contact_button)
    bot.send_message(chat_id=message.chat.id, text=f'''<b>♤ Welcome Dear -> {message.from_user.first_name} ♤
♤ Youre Not Subscribed in Check NINAJ Bot ❌
♤ Channel ~ @CHANNEL_NINJA_CHK
♤ For Show Bot Prices Send -> /buy
♤ Programmers ~ @P_3_V </b>''', reply_markup=keyboard)

def send_expiration_message(message):
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(text="♤ Programmers - Hasan", url="https://t.me/CHANNEL_NINJA_CHK")
    keyboard.add(contact_button)
    bot.send_message(chat_id=message.chat.id, text='''<b>♤ Your Subscription has Expired • لاتستطيع استخدام البوت لانه انتهى اشتراكك </b>''', reply_markup=keyboard)

def send_gateway_options(message):
    keyboard = types.InlineKeyboardMarkup()
    gateways = [
 #       types.InlineKeyboardButton(text="♤ 3DS Lookup Otp ♤️", callback_data='br1'),
        types.InlineKeyboardButton(text="♤ Otp PayPal-1 ♤️", callback_data='br11'),
#        types.InlineKeyboardButton(text="♤ Otp PayPal-2 ♤️", callback_data='br2'),
#        types.InlineKeyboardButton(text="♤ Otp PayPal-3 ♤️", callback_data='br3')
        
    ]
    
    for gateway in gateways:
        keyboard.add(gateway)
    
    bot.reply_to(message, text='♤ Chose The Gateway You Want to use from Bellow', reply_markup=keyboard)
			
			
			



	
	
import requests
from bs4 import BeautifulSoup
import pycountry

def dato(zh):
    try:
        # إعداد العناوين (Headers) للطلب
        meet_headers = {
            'Referer': 'https://bincheck.io/ar',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        }

        # إرسال الطلب وجلب الصفحة
        response = requests.get(f'https://bincheck.io/ar/details/{zh[:6]}', headers=meet_headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # البحث عن الجداول
        table1 = soup.find('table', class_='w-full table-auto')
        rows1 = table1.find_all('tr')

        table2 = soup.find_all('table', class_='w-full table-auto')[1]
        rows2 = table2.find_all('tr')

        # استخراج المعلومات
        info = {}
        
        for row in rows1:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'العلامة التجارية للبطاقة':
                    info['brand'] = cell2_text.upper()
                elif cell1_text == 'نوع البطاقة':
                    info['card_type'] = cell2_text.upper()
                elif cell1_text == 'تصنيف البطاقة':
                    info['card_level'] = cell2_text.upper()
                elif cell1_text == 'اسم المصدر / البنك':
                    info['bank'] = cell2_text.upper()

        for row in rows2:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'اسم الدولة ISO':
                    info['country_name'] = cell2_text.upper()
                    # استخراج العلم باستخدام pycountry
                    country = pycountry.countries.get(name=info['country_name'])
                    info['flag'] = getattr(country, 'flag', "") if country else ""
                elif cell1_text == 'عملة البلد ISO':
                    info['currency'] = cell2_text.upper()

        # صياغة النتيجة
        brand = info.get('brand', 'UNKNOWN')
        card_type = info.get('card_type', 'UNKNOWN')
        card_level = info.get('card_level', 'UNKNOWN')
        bank = info.get('bank', 'UNKNOWN')
        country_name = info.get('country_name', 'UNKNOWN')
        country_flag = info.get('flag', '')

        mn = f'''[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] 𝗜𝗻𝗳𝗼 -> {brand} - {card_type} - {card_level}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] 𝗕𝗮𝗻𝗸 : {bank} - {country_flag}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 : {country_name} [ {country_flag} ]'''
        return mn

    except Exception as e:
        print(f"Error fetching BIN info: {e}")
        return 'No info'
	
	
	





import threading
import time
from telebot import types

MAX_LINES = 200
stopuser = {}  # لتعقب حالة كل مستخدم

# تعريف المتغيرات لتخزين حالة كل بوابة








@bot.message_handler(commands=['onb1'])
def enable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb1'])
def disable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')








@bot.message_handler(commands=['onb2'])
def enable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb2'])
def disable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')





@bot.message_handler(commands=['onb3'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb3'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        







@bot.message_handler(commands=['onb4'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb4'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')










from telebot import types

# تعريف المتغيرات لحالة البوابات
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True


MAX_LINES = 200

@bot.message_handler(commands=['gate'])
def show_menu(message):
    if str(message.from_user.id) in admins:
        markup = types.InlineKeyboardMarkup(row_width=1)
        toggle_br1 = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        toggle_br2 = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        toggle_br3 = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        toggle_br4 = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        
        br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({toggle_br1})", callback_data='toggle_br1')
        br2_button = types.InlineKeyboardButton(f"Braintree Auth 2 ({toggle_br2})", callback_data='toggle_br2')
        br3_button = types.InlineKeyboardButton(f"Braintree Auth 3 ({toggle_br3})", callback_data='toggle_br3')
        br4_button = types.InlineKeyboardButton(f"Braintree Auth 4 ({toggle_br4})", callback_data='toggle_br4')
        limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
        
        markup.add(br1_button, br2_button, br3_button, br4_button)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'You are not the owner 🤍')

@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_') or call.data == 'set_limits')
def handle_toggle(call):
    global check_enabled_br1, check_enabled_br2, check_enabled_br3, check_enabled_br4, MAX_LINES
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == 'toggle_br1':
        check_enabled_br1 = not check_enabled_br1
        status = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Lookup 1 is now {status}.")
    elif call.data == 'toggle_br2':
        check_enabled_br2 = not check_enabled_br2
        status = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Lookup 2 is now {status}.")
    elif call.data == 'toggle_br3':
        check_enabled_br3 = not check_enabled_br3
        status = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Lookup 3 is now {status}.")
    elif call.data == 'toggle_br4':
        check_enabled_br4 = not check_enabled_br4
        status = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Lookup 4 is now {status}.")
    elif call.data == 'set_limits':
        # إرسال رسالة للمستخدم لإدخال قيمة جديدة لـ MAX_LINES
        bot.send_message(chat_id, "Please enter the new limit value for Gate limits as /set_limit 1500")

    # تحديث الرسالة لعرض الحالة الجديدة
    markup = types.InlineKeyboardMarkup(row_width=1)
    br1_button = types.InlineKeyboardButton(f"Braintree Lookup 1 ({'Enable✅' if check_enabled_br1 else 'Disable❌'})", callback_data='toggle_br1')
    br2_button = types.InlineKeyboardButton(f"Braintree Lookup 2 ({'Enable✅' if check_enabled_br2 else 'Disable❌'})", callback_data='toggle_br2')
    br3_button = types.InlineKeyboardButton(f"Braintree Lookup 3 ({'Enable✅' if check_enabled_br3 else 'Disable❌'})", callback_data='toggle_br3')
    br4_button = types.InlineKeyboardButton(f"Braintree Lookup 4 ({'Enable✅' if check_enabled_br4 else 'Disable❌'})", callback_data='toggle_br4')
    limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
    markup.add(br1_button, br2_button, br3_button, br4_button, limits_button)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Choose an option:", reply_markup=markup)


@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    global MAX_LINES
    try:
        # التحقق من أن المرسل هو الأدمن
        if str(message.from_user.id) not in admins:
            bot.reply_to(message, "Sorry, you do not have permission to use this command.")
            return
        
        # استخراج القيمة الجديدة للحد
        if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            new_limit = int(message.text.split()[1])
            MAX_LINES = new_limit
            bot.reply_to(message, f"Gate limit has been set to {MAX_LINES}.")
            
            # تحديث قائمة الخيارات في الرسالة
            show_menu(message)
        else:
            bot.reply_to(message, "Please use the correct format: /set_limit 1500.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        print(f"Error: {e}")





@bot.message_handler(commands=['stop'])
def stop_command(message):
    user_id = str(message.from_user.id)

    # التحقق مما إذا كان للمستخدم فحص نشط
    if user_id in stopuser and stopuser[user_id]['status'] == 'start':
        # استخرج معرف الفحص النشط
        check_id = stopuser[user_id]['check_id']
        
        # تحديث الحالة لإيقاف الفحص
        stopuser[user_id]['status'] = 'stop'
        
        bot.send_message(chat_id=message.chat.id, text="- Stopping your current check... ⏸")
    else:
        bot.send_message(chat_id=message.chat.id, text="- No active check to stop! ⛔")



        

	
	
	
	
	
import threading
import time
from telebot import types

MAX_LINES = 200
stopuser = {}  # لتعقب حالة كل مستخدم وفحصه
check_enabled_br1 = True  # لتتبع ما إذا كان فحص Braintree Auth 1 مفعلًا أم لا

# بوابة Braintree Auth 1
@bot.callback_query_handler(func=lambda call: call.data == 'br1')
def menu_callback(call):
    user_id = call.from_user.id
    user_first_name = call.from_user.first_name
    user_username = call.from_user.username or user_first_name

    id = str(user_id)
    user_combo_file = f"combo_{id}.txt"  # استخدام ملف الكومبو الخاص بالمستخدم

    # التحقق مما إذا كانت البوابة مفعلة
    if not check_enabled_br1:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] != 'stopped':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    # إنشاء معرف فحص خاص لكل فحص
    check_id = str(time.time())  # استخدام الوقت كمعرف فحص فريد

    def my_function():
        gate = '3DS Lookup'
        dd = 0
        live = 0
        cm = 0

        # إرسال رسالة أولية
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..")

        try:
            with open(user_combo_file, 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start', 'check_id': check_id}  # تخزين حالة الفحص الحالي

                for cc in lines:
                    # التحقق بشكل دوري من حالة التوقف
                    if stopuser[id]['status'] == 'stop' and stopuser[id]['check_id'] == check_id:
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣')
                        stopuser[id]['status'] = 'stopped'
                        return

                    start_time = time.time()
                    try:
                        last = str(otps(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data=f'stop_{check_id}')  # تخصيص زر "Stop" للفحص الحالي
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @P_3_V </b>''',
                                          reply_markup=mes)

                    # تنسيق الرسالة لتكون مشابهة للبطاقة المطلوبة
                    result_msg = f'''#3DS_Lookup_Paypal_1  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "Successful" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "Successful" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

                    if "Successful" in last:
                        live += 1
                        bot.send_message(call.from_user.id, result_msg, parse_mode="HTML")
                    else:
                        dd += 1

                    #time.sleep(20)  # استخدام مهلة قصيرة للتحقق بشكل متكرر من حالة التوقف

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @P_3_V')

    # بدء الفحص في مسار منفصل
    my_thread = threading.Thread(target=my_function)
    my_thread.start()	

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_'))
def stop_check(call):
    user_id = str(call.from_user.id)
    check_id = call.data.split('_')[1]  # استخراج معرف الفحص من الزر

    if user_id in stopuser:
        # إذا كان الفحص نشطًا
        if stopuser[user_id]['status'] == 'start' and stopuser[user_id]['check_id'] == check_id:
            stopuser[user_id]['status'] = 'stop'
            bot.send_message(chat_id=call.message.chat.id, text='- Stopping your current check... ⏸')
        else:
            bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
	




	




import threading
import time
from telebot import types

MAX_LINES = 200
stopuser = {}  # لتعقب حالة كل مستخدم وفحصه
check_enabled_br1 = True  # لتتبع ما إذا كان فحص Braintree Auth 1 مفعلًا أم لا

# قائمة البوابات المتاحة
gateways = [otps, vbv, ch, otps7, vbvbs]  # البوابات المختلفة التي سيتم استخدامها

# بوابة Braintree Auth 1
@bot.callback_query_handler(func=lambda call: call.data == 'br11')
def menu_callback(call):
    user_id = call.from_user.id
    user_first_name = call.from_user.first_name
    user_username = call.from_user.username or user_first_name

    id = str(user_id)
    user_combo_file = f"combo_{id}.txt"  # استخدام ملف الكومبو الخاص بالمستخدم

    # التحقق مما إذا كانت البوابة مفعلة
    if not check_enabled_br1:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] != 'stopped':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    # إنشاء معرف فحص خاص لكل فحص
    check_id = str(time.time())  # استخدام الوقت كمعرف فحص فريد

    def my_function():
        dd = 0
        live = 0
        cm = 0
        gate_number = 0  # رقم البوابة الذي سيتم تتبعه

        # إرسال رسالة أولية
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..")

        try:
            with open(user_combo_file, 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start', 'check_id': check_id}  # تخزين حالة الفحص الحالي

                for cc in lines:
                    # التحقق بشكل دوري من حالة التوقف
                    if stopuser[id]['status'] == 'stop' and stopuser[id]['check_id'] == check_id:
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣')
                        stopuser[id]['status'] = 'stopped'
                        return

                    start_time = time.time()

                    # التبديل بين البوابات بشكل دوري
                    gateway_function = gateways[gate_number]
                    try:
                        last = str(gateway_function(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    # تحديث رقم البوابة
                    gate_number = (gate_number + 1) % len(gateways)

                    # تحديث الرسائل
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    cm66 = types.InlineKeyboardButton(f"• Gate {gate_number + 1} •", callback_data='x')  # عرض رقم البوابة
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data=f'stop_{check_id}')  # تخصيص زر "Stop" للفحص الحالي
                    mes.add(cm1, status, cm3, cm4, cm5, cm66, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate_number + 1} 💫
- Programmer -> @P_3_V </b>''',
                                          reply_markup=mes)

                    # تنسيق الرسالة لتكون مشابهة للبطاقة المطلوبة
                    result_msg = f'''#3DS_Lookup_Paypal_1  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "Successful" in last else "Live ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

                    if "3DS Challenge Required" in last:
                        live += 1
                        bot.send_message(call.from_user.id, result_msg, parse_mode="HTML")
                    else:
                        dd += 1

                    #time.sleep(20)  # استخدام مهلة قصيرة للتحقق بشكل متكرر من حالة التوقف

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @P_3_V')

    # بدء الفحص في مسار منفصل
    my_thread = threading.Thread(target=my_function)
    my_thread.start()    

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_'))
def stop_check(call):
    user_id = str(call.from_user.id)
    check_id = call.data.split('_')[1]  # استخراج معرف الفحص من الزر

    if user_id in stopuser:
        # إذا كان الفحص نشطًا
        if stopuser[user_id]['status'] == 'start' and stopuser[user_id]['check_id'] == check_id:
            stopuser[user_id]['status'] = 'stop'
            bot.send_message(chat_id=call.message.chat.id, text='- Stopping your current check... ⏸')
        else:
            bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
	










	
import threading
import time
from telebot import types

MAX_LINES = 200
stopuser = {}  # لتعقب حالة كل مستخدم وفحصه
check_enabled_br2 = True  # لتتبع ما إذا كان فحص Braintree Auth 1 مفعلًا أم لا

# بوابة Braintree Auth 1
@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
    user_id = call.from_user.id
    user_first_name = call.from_user.first_name
    user_username = call.from_user.username or user_first_name

    id = str(user_id)
    user_combo_file = f"combo_{id}.txt"  # استخدام ملف الكومبو الخاص بالمستخدم

    # التحقق مما إذا كانت البوابة مفعلة
    if not check_enabled_br2:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] != 'stopped':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    # إنشاء معرف فحص خاص لكل فحص
    check_id = str(time.time())  # استخدام الوقت كمعرف فحص فريد

    def my_function():
        gate = '3DS Lookup Paypal-2'
        dd = 0
        live = 0
        cm = 0

        # إرسال رسالة أولية
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..")

        try:
            with open(user_combo_file, 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start', 'check_id': check_id}  # تخزين حالة الفحص الحالي

                for cc in lines:
                    # التحقق بشكل دوري من حالة التوقف
                    if stopuser[id]['status'] == 'stop' and stopuser[id]['check_id'] == check_id:
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣')
                        stopuser[id]['status'] = 'stopped'
                        return

                    start_time = time.time()
                    try:
                        last = str(otps4(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data=f'stop_{check_id}')  # تخصيص زر "Stop" للفحص الحالي
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @P_3_V </b>''',
                                          reply_markup=mes)

                    # تنسيق الرسالة لتكون مشابهة للبطاقة المطلوبة
                    result_msg = f'''#3DS_Lookup_Paypal_2  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

                    if "3DS Challenge Required" in last:
                        live += 1
                        bot.send_message(call.from_user.id, result_msg, parse_mode="HTML")
                    else:
                        dd += 1

                    #time.sleep(20)  # استخدام مهلة قصيرة للتحقق بشكل متكرر من حالة التوقف

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @P_3_V')

    # بدء الفحص في مسار منفصل
    my_thread = threading.Thread(target=my_function)
    my_thread.start()	

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_'))
def stop_check(call):
    user_id = str(call.from_user.id)
    check_id = call.data.split('_')[1]  # استخراج معرف الفحص من الزر

    if user_id in stopuser:
        # إذا كان الفحص نشطًا
        if stopuser[user_id]['status'] == 'start' and stopuser[user_id]['check_id'] == check_id:
            stopuser[user_id]['status'] = 'stop'
            bot.send_message(chat_id=call.message.chat.id, text='- Stopping your current check... ⏸')
        else:
            bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
	










import threading
import time
from telebot import types

MAX_LINES = 200
stopuser = {}  # لتعقب حالة كل مستخدم وفحصه
check_enabled_br3 = True  # لتتبع ما إذا كان فحص Braintree Auth 1 مفعلًا أم لا

# بوابة Braintree Auth 1
@bot.callback_query_handler(func=lambda call: call.data == 'br3')
def menu_callback(call):
    user_id = call.from_user.id
    user_first_name = call.from_user.first_name
    user_username = call.from_user.username or user_first_name

    id = str(user_id)
    user_combo_file = f"combo_{id}.txt"  # استخدام ملف الكومبو الخاص بالمستخدم

    # التحقق مما إذا كانت البوابة مفعلة
    if not check_enabled_br3:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] != 'stopped':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    # إنشاء معرف فحص خاص لكل فحص
    check_id = str(time.time())  # استخدام الوقت كمعرف فحص فريد

    def my_function():
        gate = '3DS Lookup Paypal-3'
        dd = 0
        live = 0
        cm = 0

        # إرسال رسالة أولية
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..")

        try:
            with open(user_combo_file, 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start', 'check_id': check_id}  # تخزين حالة الفحص الحالي

                for cc in lines:
                    # التحقق بشكل دوري من حالة التوقف
                    if stopuser[id]['status'] == 'stop' and stopuser[id]['check_id'] == check_id:
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣')
                        stopuser[id]['status'] = 'stopped'
                        return

                    start_time = time.time()
                    try:
                        last = str(otpspaypal2(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data=f'stop_{check_id}')  # تخصيص زر "Stop" للفحص الحالي
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @P_3_V </b>''',
                                          reply_markup=mes)

                    # تنسيق الرسالة لتكون مشابهة للبطاقة المطلوبة
                    result_msg = f'''#3DS_Lookup_Paypal_3  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

                    if "3DS Challenge Required" in last:
                        live += 1
                        bot.send_message(call.from_user.id, result_msg, parse_mode="HTML")
                    else:
                        dd += 1

                    #time.sleep(20)  # استخدام مهلة قصيرة للتحقق بشكل متكرر من حالة التوقف

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @P_3_V')

    # بدء الفحص في مسار منفصل
    my_thread = threading.Thread(target=my_function)
    my_thread.start()	

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_'))
def stop_check(call):
    user_id = str(call.from_user.id)
    check_id = call.data.split('_')[1]  # استخراج معرف الفحص من الزر

    if user_id in stopuser:
        # إذا كان الفحص نشطًا
        if stopuser[user_id]['status'] == 'start' and stopuser[user_id]['check_id'] == check_id:
            stopuser[user_id]['status'] = 'stop'
            bot.send_message(chat_id=call.message.chat.id, text='- Stopping your current check... ⏸')
        else:
            bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No active check to stop! ⛔')
	









import json
from datetime import datetime, timedelta

# دالة تحقق من خطة المستخدم
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)]['plan']
        timer = json_data[str(user_id)]['timer']
        if user_plan != 'Free - Not Subscribed':
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                    return True
            except Exception as e:
                return False
    return False













user_locks = {}
last_command_usage = {}



@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 1
    if not check_enabled_br1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق إذا كان هناك فحص قيد التنفيذ لهذا المستخدم
    if user_locks.get(user_id):
        #bot.reply_to(message, "<b>Your previous check is still in progress. Please wait until it finishes.</b>", parse_mode="HTML")
        return

    # تم إزالة الجزء المتعلق بـ ANTI SPAM

    # تحديث وقت الاستخدام الأخير
    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        # قفل المستخدم الحالي حتى ينتهي الفحص
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return 

            cc = message.text.replace('.vbv ', '').replace('/vbv ', '')
            gate = '3DS Lookup'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "successful" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "successful" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')







user_locks = {}
last_command_usage = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sq') or message.text.lower().startswith('/sq'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 1
    if not check_enabled_br1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق إذا كان هناك فحص قيد التنفيذ لهذا المستخدم
    if user_locks.get(user_id):
        return

    # تحديث وقت الاستخدام الأخير
    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        # قفل المستخدم الحالي حتى ينتهي الفحص
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return 

            cc = message.text.replace('.sq ', '').replace('/sq ', '')
            gate = '3DS Lookup Paypal-1'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup_Paypal_1  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')








user_locks = {}
last_command_usage = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp') or message.text.lower().startswith('/pp'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    if not check_enabled_br2:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    if user_locks.get(user_id):
        return

    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return

            cc = message.text.replace('.pp ', '').replace('/pp ', '')
            gate = '3DS Lookup Paypal-2'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps2(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup_Paypal_2  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')











user_locks = {}
last_command_usage = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.p3') or message.text.lower().startswith('/p3'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    if user_locks.get(user_id):
        return

    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return

            cc = message.text.replace('.p3 ', '').replace('/p3 ', '')
            gate = '3DS Lookup Paypal-3'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps3(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup_Paypal_3  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')











user_locks = {}
last_command_usage = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.p4') or message.text.lower().startswith('/p4'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    if user_locks.get(user_id):
        return

    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return

            cc = message.text.replace('.p4 ', '').replace('/p4 ', '')
            gate = '3DS Lookup Paypal-4'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps4(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup_Paypal_4  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')





user_locks = {}
last_command_usage = {}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.p5') or message.text.lower().startswith('/p5'))
def respond_to_vhk(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or user_first_name
    current_time = datetime.now()

    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    if user_locks.get(user_id):
        return

    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        user_locks[user_id] = True
        try:
            m = message.text
            cc = str(reg(m))
            if cc == 'None':
                bot.reply_to(message, '''<strong>🚫 Your card number is not valid. Try to input a valid card number. ⛔</strong>''')
                return

            cc = message.text.replace('.p5 ', '').replace('/p5 ', '')
            gate = '3DS Lookup Paypal-5'
            ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
            start_time = time.time()

            try:
                last = str(otps5(cc))
            except:
                last = 'Gateway Error ❌'

            end_time = time.time()
            execution_time = end_time - start_time

            # رسائل الرد
            result_msg = f'''#3DS_Lookup_Paypal_5  🌩
━━━━━━━━━━━━━
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Cc: <code>{cc}</code>
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Status: {"Approved! ✅" if "3DS Challenge Required" in last else "Rejected ❌"}
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Response: {last}

{str(dato(cc[:6]))}

[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] T/t: {"{:.2f}".format(execution_time)}(s) | [Px: {"Live! ✅" if "3DS Challenge Required" in last else "Live! ✅"}] 
[<a href="https://t.me/Otp_ninja1_bot">ϟ</a>] Req: @{user_username} | [VIP]
━━━━━━━━━━━━━
Dev by : <code>@P_3_V</code> 🌤'''

            bot.edit_message_text(text=result_msg, chat_id=message.chat.id, message_id=ko, parse_mode="HTML")

        finally:
            # إزالة القفل بعد انتهاء الفحص
            user_locks[user_id] = False
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed NINJA CHK !❌

Your ID : {message.chat.id}
Programmer - @P_3_V''')







def generate_credit_card(message, bot, ko):
    try:
        # البحث عن رقم البطاقة والبيانات الأخرى في الرسالة
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            
            # التحقق من صحة BIN
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""

            # توليد 10 بطاقات ائتمان
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)

                # تحديد طول الـ CVV بناءً على نوع البطاقة
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)

                # توليد بطاقة ائتمان مع الشهر، السنة، والـ CVV
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"

            # جلب معلومات الـ BIN
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'

            # إرسال النتيجة إلى المستخدم
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {card_type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="<b>BIN not recognized. Please enter a valid BIN ❌</b>")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10




def gen(bin):
 remaining_digits = 16 - len(bin)
 card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
 digits = [int(digit) for digit in card_number]
 for i in range(len(digits)):
  if i % 2 == 0:
   digits[i] *= 2
   if digits[i] > 9:
    digits[i] -= 9
 
 checksum = sum(digits)
 checksum %= 10
 checksum = 10 - checksum
 if checksum == 10:
  checksum = 0
 card_number += str(checksum)
 return card_number
import requests

@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
    try:
        # محاولة قراءة النص الذي تم الرد عليه إذا كان موجودًا
        bm = message.reply_to_message.text
    except:
        # إذا لم يكن هناك رسالة تم الرد عليها، استخدم النص الحالي
        bm = message.text
    
    # استخراج الأرقام من الرسالة
    regex = r'\d+'
    try:
        matches = re.findall(regex, bm)
    except:
        bot.reply_to(message, '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>', parse_mode="HTML")
        return

    # الحصول على أول 6 أرقام من BIN
    bin = ''.join(matches)[:6]
    ko = bot.reply_to(message, "<b>Checking Your bin...⌛</b>", parse_mode="HTML").message_id

    # التحقق من أن الـ BIN يتكون من 6 أرقام على الأقل
    if len(bin) >= 6:
        try:
            # طلب معلومات الـ BIN من API
            data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country = data.get('country_name', 'Unknown')
            country_flag = data.get('country_flag', '🏳️')
            bank = data.get('bank', 'Unknown')
            
            # تكوين الرسالة النهائية
            msg = f'''<b>
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅
    
𝐁𝐈𝐍 ➜ <code>{bin}</code>
    
𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {card_type} - {brand}  
𝐁𝐚𝐧𝐤 ➜ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}
</b> '''
        except:
            # في حال حدوث خطأ أثناء طلب البيانات
            msg = '<b>𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌</b>'
    else:
        msg = '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>'
    
    # تعديل الرسالة الأصلية مع النتيجة
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
 ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
 generate_credit_card(message,bot,ko)








import requests
import random
import string
from telebot import TeleBot

# قائمة جميع رموز الدول المدعومة بواسطة randomuser.me وأسماؤها البديلة
country_aliases = {
    "us": ["us", "usa", "america"],
    "gb": ["gb", "uk", "britain", "england"],
    "fr": ["fr", "france"],
    "de": ["de", "germany"],
    "es": ["es", "spain"],
    "nl": ["nl", "netherlands", "holland"],
    "au": ["au", "australia"],
    "br": ["br", "brazil"],
    "ca": ["ca", "canada"],
    "ch": ["ch", "switzerland"],
    "dk": ["dk", "denmark"],
    "fi": ["fi", "finland"],
    "ie": ["ie", "ireland"],
    "in": ["in", "india"],
    "ir": ["ir", "iran"],
    "mx": ["mx", "mexico"],
    "nz": ["nz", "new zealand"],
    "no": ["no", "norway"],
    "rs": ["rs", "serbia"],
    "tr": ["tr", "turkey"],
    "ua": ["ua", "ukraine"]
}

# دالة للبحث عن رمز الدولة بناءً على الاسم البديل
def get_country_code(input_code):
    input_code = input_code.lower()
    for code, aliases in country_aliases.items():
        if input_code in aliases:
            return code
    return None

# دالة لجلب البيانات من API وتوليد معلومات وهمية بناءً على الدولة
def get_fake_data(country_code):
    # توليد اسم مستخدم عشوائي
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # توليد البريد الإلكتروني المؤقت
    emails = f"{username}@teleworm.us"
    
    if country_code not in country_aliases:
        return f"Error: The country {country_code.upper()} is not supported for fake data generation."

    try:
        # جلب البيانات من API باستخدام رمز الدولة المدخل
        response = requests.get(f"https://randomuser.me/api/?nat={country_code}&inc=name,location,phone")

        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        
        response_data = response.json()
        
        # تحقق من الاستجابة
        if 'results' not in response_data or not response_data['results']:
            return "Error: No results found."

        user_info = response_data['results'][0]

        # الحصول على المعلومات الشخصية
        name = f"Dr. {user_info['name']['first']} {user_info['name']['last']}"
        street_address = f"{user_info['location']['street']['number']} {user_info['location']['street']['name']}"
        city = user_info['location']['city']
        state = user_info['location']['state']
        postal_code = user_info['location']['postcode']
        phone = user_info['phone']
        country = user_info['location']['country']

        # صياغة الرد بالشكل المطلوب مع رابط فتح البريد الوهمي
        user_data = f"""
📍 {country} Address Generator

𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: <code>{name}</code>
𝗦𝘁𝗿𝗲𝗲𝘁 𝗔𝗱𝗱𝗿𝗲𝘀𝘀: <code>{street_address}</code>
𝗖𝗶𝘁𝗶𝗲𝘀/𝗧𝗼𝘄𝗻𝘀/𝗩𝗶𝗹𝗹𝗮𝗴𝗲: <code>{city}</code>
𝗦𝘁𝗮𝘁𝗲/𝗽𝗿𝗼𝘃𝗶𝗻𝗰𝗲/𝗿𝗲𝗴𝗶𝗼𝗻: <code>{state}</code>
𝗣𝗼𝘀𝘁𝗮𝗹 𝗖𝗼𝗱𝗲: <code>{postal_code}</code>
𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿: <code>{phone}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{country}</code>
𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗘𝗺𝗮𝗶𝗹: <code>{emails}</code> <a href='https://www.fakemailgenerator.com/#/teleworm.us/{username}/' target='_blank' style='color: blue;'>[Open link]</a>
"""
        return user_data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "Error: Could not fetch the data."
    except Exception as e:
        print(f"General error: {e}")
        return "Error: An unexpected error occurred."

# التعامل مع الأوامر /fake {country_code}
@bot.message_handler(func=lambda message: message.text.lower().startswith('.fake') or message.text.lower().startswith('/fake'))
def generate_fake_data(message):
    try:
        # قراءة رمز الدولة بعد .fake
        input_data = message.text.split(" ")[1]  
        
        # البحث عن رمز الدولة باستخدام الأسماء البديلة
        country_code = get_country_code(input_data)

        if country_code is None:
            bot.reply_to(message, f"Error: The country code or name '{input_data}' is not recognized. Please use a valid country code or name.")
            return

        # جلب البيانات الشخصية الوهمية بناءً على رمز الدولة
        user_data = get_fake_data(country_code)

        # إرسال المعلومات الشخصية للمستخدم
        bot.reply_to(message, user_data, parse_mode='HTML')

    except IndexError:
        bot.reply_to(message, 'Please provide a country code or name after the command. Usage: .fake {country_code or country_name}')
    except Exception as e:
        print(f"Error in generate_fake_data: {e}")
        bot.reply_to(message, 'An error occurred. Please try again.')

# قائمة الدول المدعومة
@bot.message_handler(commands=['countries'])
def list_supported_countries(message):
    country_list = ', '.join([', '.join(aliases).upper() for aliases in country_aliases.values()])  # تحويل رموز الدول إلى أحرف كبيرة
    bot.reply_to(message, f"The following country codes and names are supported: {country_list}")











import telebot
import re  # To use regular expressions for BIN validation

# Name of the file that holds the blocklist
BLOCKLIST_FILE = 'blocklist.txt'

# Function to handle the /block command
@bot.message_handler(commands=['block'])
def block_bin(message):
    # Verify the user is an admin
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return

    # Extract the BIN from the command and validate it
    try:
        bin_to_block = message.text.split()[1]
        # Check if the BIN is exactly 6 digits
        if not re.fullmatch(r"\d{6}", bin_to_block):
            bot.reply_to(message, "Please enter a valid 6-digit BIN. Example: /block 421689")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a BIN to block. Example: /block 421689")
        return

    # Add BIN to the blocklist file
    with open(BLOCKLIST_FILE, 'a') as file:
        file.write(f"{bin_to_block}\n")

    # Confirm blocking
    bot.reply_to(message, f"BIN {bin_to_block} has been added to the blocklist.")

# Function to handle the /unblock command
@bot.message_handler(commands=['unblock'])
def unblock_bin(message):
    # Verify the user is an admin
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return

    # Extract the BIN from the command and validate it
    try:
        bin_to_unblock = message.text.split()[1]
        # Check if the BIN is exactly 6 digits
        if not re.fullmatch(r"\d{6}", bin_to_unblock):
            bot.reply_to(message, "Please enter a valid 6-digit BIN. Example: /unblock 421689")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a BIN to unblock. Example: /unblock 421689")
        return

    # Read the blocklist file and rewrite it without the specified BIN
    try:
        with open(BLOCKLIST_FILE, 'r') as file:
            lines = file.readlines()

        # Remove the specified BIN if it exists
        with open(BLOCKLIST_FILE, 'w') as file:
            removed = False
            for line in lines:
                if line.strip() != bin_to_unblock:
                    file.write(line)
                else:
                    removed = True

        # Confirm unblocking
        if removed:
            bot.reply_to(message, f"BIN {bin_to_unblock} has been removed from the blocklist.")
        else:
            bot.reply_to(message, f"BIN {bin_to_unblock} was not found in the blocklist.")

    except FileNotFoundError:
        bot.reply_to(message, "The blocklist file does not exist.")









import telebot
from telebot import types
import json
from datetime import datetime


# تعريف المتغيرات لحالة البوابات
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True


# تحميل بيانات المستخدم من data.json
def load_user_data(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    return json_data.get(str(user_id), {})

# تحديث بيانات المستخدم في data.json
def save_user_data(user_id, data):
    with open('data.json', 'r') as file:
        json_data = json.load(file)

    json_data[str(user_id)] = data

    with open('data.json', 'w') as file:
        json.dump(json_data, file, indent=4)

# نصوص اللغات المختلفة
texts = {
    "en": {
        "welcome": """<strong>𝗛𝗶 𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲𝘀 𝗼𝗿 𝗖𝗵𝗮𝗿𝗴𝗲 𝗚𝗮𝘁𝗲𝘀.
</strong>""",
        "auth_gates": lambda: f"""<strong>𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋
        
{('ON ✅' if check_enabled_br1 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 𝟭 /sq 
{('ON ✅' if check_enabled_br2 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 𝟮 /pp 
{('ON ✅' if check_enabled_br3 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 𝟯 /p3
𝗨𝘀𝗲 /buy 𝘁𝗼 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝗩𝗜𝗣 𝗣𝗟𝗔𝗡
</strong>""",
        "charge_gates": lambda: f"""<strong>Charge Gates

𝗨𝘀𝗲 /buy 𝘁𝗼 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝗩𝗜𝗣 𝗣𝗟𝗔𝗡
</strong>""",
        "settings": "Settings",
        "languages": "Languages",
        "information": "Information",
        "back": "↩️ Back"
    },
    "ar": {
        "welcome": """<strong>مرحباً انقر على الأزرار أدناه للوصول إلى فحص لايف أو فحص تشارج.
</strong>""",
        "auth_gates": lambda: f"""<strong>𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋

{('ON ✅' if check_enabled_br1 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 /sq 
{('ON ✅' if check_enabled_br2 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 𝟮 /pp
{('ON ✅' if check_enabled_br3 else 'OFF ❌')} 𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋 𝟯 /p3
𝗨𝘀𝗲 /buy 𝘁𝗼 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝗩𝗜𝗣 𝗣𝗟𝗔𝗡
</strong>""",
        "charge_gates": lambda: f"""<strong>فحص تشارج

𝗨𝘀𝗲 /buy 𝘁𝗼 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝗩𝗜𝗣 𝗣𝗟𝗔𝗡
</strong>""",
        "settings": "الإعدادات",
        "languages": "اللغات",
        "information": "معلوماتي",
        "back": "↩️ العودة"
    }
}

from datetime import datetime
import json
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    man_function(message)
    user_id = message.from_user.id
    user_data = load_user_data(user_id)
    current_language = user_data.get("language", "en")

    # القائمة الرئيسية التي تظهر عند الضغط على زر Start
    key = types.InlineKeyboardMarkup()
    gateway_button = types.InlineKeyboardButton(text='Gateways' if current_language == "en" else 'البوابات', callback_data='Gateway')
    tools_button = types.InlineKeyboardButton(text='Tools' if current_language == "en" else 'الأدوات', callback_data='Tools')
#    information_button = types.InlineKeyboardButton(text='Information' if current_language == "en" else 'المعلومات', callback_data='Information')
    settings_button = types.InlineKeyboardButton(text='Settings' if current_language == "en" else 'الإعدادات', callback_data='Settings')
    key.add(gateway_button, tools_button)
    key.add(settings_button)

    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, text=texts[current_language]["welcome"].format(first_name=first_name), parse_mode='html', reply_markup=key)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    user_id = call.from_user.id
    user_data = load_user_data(user_id)
    current_language = user_data.get("language", "en")

    if call.data == 'Gateway':
        show_gateway_options(call.message, current_language)
    elif call.data == 'AuthGates':
        show_auth_gates(call.message, current_language)
    elif call.data == 'ChargeGates':
        show_charge_gates(call.message, current_language)
    elif call.data == 'Tools':
        show_tools(call.message, current_language)  # إضافة دالة show_tools
    elif call.data == 'Information':
        show_information(call, current_language)
    elif call.data == 'Settings':
        show_settings(call.message, current_language)
    elif call.data == 'Languages':
        show_languages(call.message, current_language)
    elif call.data == 'lang_en':
        current_language = "en"
        user_data["language"] = "en"
        save_user_data(user_id, user_data)
        back(call.message, current_language)
    elif call.data == 'lang_ar':
        current_language = "ar"
        user_data["language"] = "ar"
        save_user_data(user_id, user_data)
        back(call.message, current_language)
    elif call.data == 'Back':
        back(call.message, current_language)

def show_gateway_options(message, current_language):
    # دالة تظهر خيارات البوابات بعد الضغط على "Gateway"
    key = types.InlineKeyboardMarkup()
    auth_gate_button = types.InlineKeyboardButton(text='𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋' if current_language == "en" else '𝟯𝘿𝙎 𝙇𝙊𝙊𝙆𝙐𝙋', callback_data='AuthGates')
 #   charge_gate_button = types.InlineKeyboardButton(text='Charge Gates' if current_language == "en" else 'فحص تشارج', callback_data='ChargeGates')
    back_button = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(auth_gate_button)
    key.add(back_button)

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=texts[current_language].get("gateway_options", "Gateway Options"),  # إضافة نص مخصص لهذا الجزء
        parse_mode="html",
        reply_markup=key
    )

def show_auth_gates(message, current_language):
    key = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(back_button)
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=texts[current_language]["auth_gates"](),
        parse_mode="html",
        reply_markup=key
    )

def show_charge_gates(message, current_language):
    key = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(back_button)
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=texts[current_language]["charge_gates"](),
        parse_mode="html",
        reply_markup=key
    )

# إضافة دالة show_tools


def show_tools(message, current_language):
    # إعداد لوحة المفاتيح
    key = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(back_button)

    # تحديد النص الذي سيتم عرضه باستخدام f-string
    if current_language == "en":
        text = f"""
<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: 3ds Lookup</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /vbv</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: VIP USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖲𝗍𝖺𝗍𝗎𝗌: ON ✅</strong>

<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: Fake Address</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /fake us</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: FREE USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] status: ON ✅</strong>

<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: Gen Cards</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /gen 440393</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: FREE USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] status: ON ✅</strong>
"""



    else:
        text = f"""
<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: 3ds Lookup</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /vbv</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: VIP USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖲𝗍𝖺𝗍𝗎𝗌: ON ✅</strong>

<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: Fake Address</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /fake us</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: FREE USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] status: ON ✅</strong>

<strong>[<a href='{mainc}'>⽷</a>] 𝖭𝖺𝗆𝖾: Gen Cards</strong>
<strong>[<a href='{mainc}'>⽷</a>] Command: /gen 440393</strong>
<strong>[<a href='{mainc}'>⽷</a>] 𝖳𝗒𝗉𝖾: FREE USERS</strong>
<strong>[<a href='{mainc}'>⽷</a>] status: ON ✅</strong>
"""

    # تعديل النص في الرسالة وإضافة لوحة المفاتيح
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=text,
        parse_mode="html",  # تأكد من أن الرسالة ستعرض بتنسيق HTML
        reply_markup=key  # إضافة لوحة المفاتيح
    )







def show_settings(message, current_language):
    key = types.InlineKeyboardMarkup()
    languages = types.InlineKeyboardButton(text=texts[current_language]["languages"], callback_data='Languages')
    information = types.InlineKeyboardButton(text=texts[current_language]["information"], callback_data='Information')
    back = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(languages)
    key.add(information)
    key.add(back)
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<strong>Settings</strong>" if current_language == "en" else "<strong>الإعدادات</strong>",
        parse_mode="html",
        reply_markup=key
    )

def show_languages(message, current_language):
    key = types.InlineKeyboardMarkup()
    en = types.InlineKeyboardButton(text="English", callback_data='lang_en')
    ar = types.InlineKeyboardButton(text="العربية", callback_data='lang_ar')
    back = types.InlineKeyboardButton(text=texts[current_language]["back"], callback_data='Back')
    key.add(en, ar)
    key.add(back)

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<strong>Choose your language:</strong>" if current_language == "en" else "<strong>اختر لغتك:</strong>",
        parse_mode="html",
        reply_markup=key
    )

def show_information(call, current_language):
    user_id = call.from_user.id
    username = call.from_user.username
    first_name = call.from_user.first_name

    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
    except Exception as e:
        bot.send_message(call.message.chat.id, f'- Error reading data file: {e}')
        return

    user_data = json_data.get(str(user_id), {})
    plan = user_data.get('plan', 'NO PLAN')

    info_text = f"""<strong>User Information</strong>
• User ID: {user_id}
• Username: @{username if username else 'Not Available'}
• First Name: {first_name}
• Plan: {plan}
"""

    if plan == "VIP Subscribed":
        end_time_str = user_data.get('timer', None)
        if end_time_str:
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
            now = datetime.now()
            time_left = end_time - now
            days_left = time_left.days
            hours_left = time_left.seconds // 3600
            info_text += f"• Subscription ends in: {days_left} days and {hours_left} hours\n"
        else:
            info_text += "• Subscription end time: Not Available\n"

    bot.send_message(
        chat_id=call.message.chat.id,
        text=info_text,
        parse_mode="html"
    )

def back(message, current_language):
    key = types.InlineKeyboardMarkup()
    gateway_button = types.InlineKeyboardButton(text='Gateway' if current_language == "en" else 'البوابات', callback_data='Gateway')
    tools_button = types.InlineKeyboardButton(text='Tools' if current_language == "en" else 'الأدوات', callback_data='Tools')
#    information_button = types.InlineKeyboardButton(text='Information' if current_language == "en" else 'المعلومات', callback_data='Information')
    settings_button = types.InlineKeyboardButton(text='Settings' if current_language == "en" else 'الإعدادات', callback_data='Settings')
    key.add(gateway_button, tools_button)
    key.add(settings_button)

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=texts[current_language]["welcome"].format(first_name=message.from_user.first_name),
        parse_mode='html',
        reply_markup=key
    )














@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>♤ BIN Info Lookup  🔍
	
♤ - BIN -></b> <code>{cc}</code>

<b>{str(dato(cc[:6]))}</b>''')












                



import json
import threading
from datetime import datetime
import time




def get_user_info(user_id):
    try:
        chat = bot.get_chat(user_id)
        user_name = chat.first_name
        user_username = chat.username
        return user_name, user_username
    except Exception as e:
        m = (f"Error retrieving user info for ID {user_id}: {e}")
        return 'Unknown', 'Unknown'

def notify_admins(user_id, user_data):
    user_name, user_username = get_user_info(user_id)
    message = f'''- Subscription Expired Notification 🕒

• User ID: {user_id}
• User Name: {user_name}
• Username: @{user_username}
• Plan: {user_data.get('plan', 'Free - Not Subscribed')}
• Expiration Date: {user_data.get('timer', 'N/A')}
'''
    for admin_id in myid:
        bot.send_message(admin_id, message)

def notify_user(user_id):
    try:
        bot.send_message(user_id, "Your Subscription Has Expired.")
    except Exception as e:
        m = (f"Error notifying user {user_id}: {e}")

def update_subscription_status():
    try:
        # قراءة بيانات المستخدمين من ملف data.json
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        current_time = datetime.now()
        updated = False  # لنعرف إذا كانت هناك تحديثات

        for user_id, user_data in json_data.items():
            timer_str = user_data.get('timer', None)
            if timer_str:
                try:
                    expiration_time = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                    
                    if current_time > expiration_time:
                        user_data['plan'] = 'Free - Not Subscribed'
                        del user_data['timer']  # حذف الوقت بعد التحديث
                        updated = True
                        # إرسال إشعار إلى الأدمن
                        notify_admins(user_id, user_data)
                        # إرسال إشعار إلى المستخدم
                        notify_user(user_id)
                except ValueError:
                    m = (f"Date format error for user {user_id} with date {timer_str}")
        
        if updated:
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = ("Subscription status updated.")
    
    except Exception as e:
        mm = (f"Error updating subscription status: {e}")

def schedule_check():
    while True:
        update_subscription_status()
        time.sleep(1)  # تحقق كل دقيقة

# بدء عملية التحقق من الاشتراكات في خيط منفصل
check_thread = threading.Thread(target=schedule_check)
check_thread.start()


















import json
from datetime import datetime, timedelta

# دالة تحقق من خطة المستخدم
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)].get('plan', 'Free - Not Subscribed')
        timer = json_data[str(user_id)].get('timer', None)
        if user_plan != 'Free - Not Subscribed' and timer:
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                    return True
            except Exception as e:
                print(f"Error parsing date for user {user_id}: {e}")
                return False
    return False
    
    
    



@bot.message_handler(commands=['kil'])
def qwwe(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            idd = message.from_user.id
            mes = message.text.replace("/kil ", "")
            bot.send_message(idd, mes)

            # إرسال الرسائل للمشتركين من data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)

            for user_id, details in json_data.items():
                if check_user_plan(user_id):
                    try:
                        mp += 1
                        bot.send_message(user_id, text=mes)
                    except Exception as e:
                        erop += 1
                        print(f"Error sending message to user {user_id}: {e}")

            bot.reply_to(message, f'''- Hello Hassan
• Done Send - {mp}
• Bad Send - {erop}''')
        except Exception as err:
            bot.reply_to(message, f'- Was An error : {err}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")






import threading
import json

# إنشاء قفل لمنع التداخل أثناء الإرسال
send_lock = threading.Lock()

@bot.message_handler(commands=['all'])
def qwwe(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            idd = message.from_user.id
            mes = message.text.replace("/all ", "")
            bot.send_message(idd, mes)

            # تحميل قائمة المستخدمين من data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)

            # استخدام القفل لتأمين عملية الإرسال
            with send_lock:
                for user_id, details in json_data.items():
                    # إرسال الرسالة لكل المستخدمين بغض النظر عن خطة الاشتراك
                    try:
                        mp += 1
                        bot.send_message(user_id, text=mes)
                    except Exception as e:
                        erop += 1
                        print(f"Error sending message to user {user_id}: {e}")

            # الرد على المرسل بعد انتهاء العملية
            bot.reply_to(message, f'''- Hello Hassan
• Done Send - {mp}
• Bad Send - {erop}''')
        except Exception as err:
            bot.reply_to(message, f'- Was An error : {err}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")









@bot.message_handler(commands=["tot"])
def adode(message):
    if str(message.from_user.id) in myid:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        vip_count = 0
        for user_id, details in json_data.items():
            user_plan = details.get('plan', 'Free - Not Subscribed')
            timer = details.get('timer', None)
            if user_plan != 'Free - Not Subscribed' and timer:
                try:
                    date_str = timer.split('.')[0]
                    provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    current_time = datetime.now()
                    if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                        vip_count += 1
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")

        bot.reply_to(message, f'- Total VIP Subscribers: {vip_count}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")











import json
from datetime import datetime

@bot.message_handler(commands=['sh'])
def show_vip_subscribers(message):
    if str(message.chat.id) in myid:
        try:
            with open('data.json', 'r') as file:
                json_data = json.load(file)
        except Exception as e:
            bot.send_message(message.chat.id, f'- Error reading data file: {e}')
            return

        total_subscribers = 0
        subscriber_details = []

        for user_id, user_data in json_data.items():
            plan = user_data.get('plan', 'NO PLAN')
            if plan == 'VIP Subscribed':
                timer = user_data.get('timer', 'NO EXPIRATION DATE')
                if timer != 'NO EXPIRATION DATE':
                    try:
                        expiration_date = datetime.strptime(timer, "%Y-%m-%d %H:%M")
                        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M")
                    except ValueError:
                        expiration_date_str = 'INVALID DATE FORMAT'
                else:
                    expiration_date_str = 'NO EXPIRATION DATE'
                
                # الحصول على تفاصيل المستخدم
                try:
                    chat = bot.get_chat(user_id)
                    user_name = chat.first_name
                    user_username = chat.username
                    if user_name:
                        user_display = f"Name: {user_name}\nUsername: @{user_username}" if user_username else f"Name: {user_name}\nUsername: Not Available"
                    else:
                        # Skip users with no valid name
                        continue
                except Exception as e:
                    # Skip users with errors retrieving data
                    continue
                
                subscriber_details.append(f'''• User ID: {user_id}
{user_display}
• Plan: {plan}
• Expiration Date: {expiration_date_str}
━━━━━━━━━━━━━━━━━━━━━━
''')

                total_subscribers += 1

        if subscriber_details:
            details_message = "\n".join(subscriber_details)
            bot.send_message(message.chat.id, f'''- VIP Subscriber Details ✅💫

{details_message} - Total VIP Subscribers -> {total_subscribers} ✅
''')
        else:
            bot.send_message(message.chat.id, '- No VIP subscribers found.')

















@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or 'NoUsername'  # التعامل مع حالة عدم وجود اسم مستخدم
    
    response_message = f'''🌟 Welcome » {user_first_name}
🆔 ID » <code>{user_id}</code>
📛 Name » {user_first_name}
🧑 Username » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')



	
	
	







@bot.message_handler(commands=["menu"])
def adodre(message):
	if str(message.chat.id) in myid:
		bot.reply_to(message,'''- Welcome My Boss ♡
- Start Check Bot ¦ /start
- Add New Subscriber ¦ /add + ID
- Total Bot Users ¦ /tot
- Send Msg Forr All ¦ /kil + msg
- Delete A Subsc ¦ /dele + ID
- Show Sub's ID's ¦ /sh
- Stop And Start The Gate's /gate
- To Ban The Bins /block
- To unBan The Bins /unblock
------------------------------------
• Programmer ¦ @P_3_V
• Channel ¦ @CHANNEL_NINJA_CHK''')





	















import json
from datetime import datetime

def remove_subscription(user_id):
    try:
        # قراءة بيانات المستخدمين من ملف data.json
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
            # تحويل الخطة إلى FREE
            json_data[user_id]['plan'] = 'Free - Not Subscribed'
            del json_data[user_id]['timer']  # حذف الوقت إن وجد
            
            # كتابة البيانات المعدلة إلى data.json
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = (f"Subscription for user {user_id} has been set to FREE.")
        else:
            mm= (f"User ID {user_id} not found in data.json.")
    
    except Exception as e:
        m = (f"Error removing subscription for user {user_id}: {e}")

@bot.message_handler(commands=['dele'])
def qwwem(message):
    if str(message.chat.id) in admins:
        user_id = message.text.replace("/dele ", "")
        
        # تحويل اشتراك المستخدم إلى FREE
        remove_subscription(user_id)
        
        try:
            chat = bot.get_chat(user_id)
            frs = chat.first_name
            use = chat.username
            bot.send_message(message.chat.id, f'''- Done ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}

- IS Removed From Subscribers ✅''')
        except Exception as e:
            bot.send_message(message.chat.id, f'''- UnSuccessful Removal ❌

• User might not have opened your bot.

- Error -> {e}''')
    else:
        bot.send_message(message.chat.id, "You do not have permission to execute this command.")







import json
import threading
from datetime import datetime, timedelta
import random
import string

# وظيفة توليد كود
@bot.message_handler(commands=["code"])
def generate_code(message):
    def my_function():
        id = message.from_user.id
        if not str(id) in myid:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            
            characters = string.ascii_uppercase + string.digits
            pas = 'NINJA-' + '2024' +'-' + ''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            expiration_time = current_time + timedelta(hours=h)
            plan = 'VIP Subscribed'
            expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
            
            new_data = {
                pas: {
                    "plan": plan,
                    "timer": expiration_time_str
                }
            }
            
            existing_data.update(new_data)
            
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            
            msg = f'''<b>♤ Check NINAJ Code
♤ Expire in -> {expiration_time_str}
♤ Code -> <code>{pas}</code>
            
♤ For redeem The Code Use /redeem code</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f'<b>ERROR : {e}</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# وظيفة استرداد كود
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            # استخراج الكود من الرسالة
            re = message.text.split(' ')[1]
            
            # قراءة البيانات من data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            
            # تحقق من وجود الكود في البيانات
            if re in json_data:
                timer = json_data[re].get('timer', 'Unknown')
                typ = json_data[re].get('plan', 'Free - Not Subscribed')

                # تحديث بيانات المستخدم الحالي
                json_data[str(message.from_user.id)] = {
                    'timer': timer,
                    'plan': typ
                }
                
                # حذف الكود القديم
                del json_data[re]
                
                # كتابة البيانات المعدلة إلى data.json
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=2, ensure_ascii=False)

                msg = f'''<b>♤ Check NINAJ CHK Subscribtion Done ✅
♤ Expires in -> {timer}</b>'''
                bot.reply_to(message, msg, parse_mode="HTML")
            else:
                bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")

        except KeyError as e:
            print(f'KeyError: {e}')
            bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '<b>There was an error processing your request. Please try again later.</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from datetime import datetime, timedelta
import json
import threading

# وظيفة إضافة مستخدم جديد إلى خطة VIP أو تعديل الوقت المتبقي
@bot.message_handler(commands=['add'])
def add_subscription(message):
    def my_function():
        try:
            chid = message.chat.id
            command_text = message.text.replace('/add ', '')
            user_id, additional_hours = command_text.split()
            additional_hours = int(additional_hours)

            if str(message.chat.id) in myid:
                current_time = datetime.now()

                # قراءة البيانات من data.json
                with open('data.json', 'r') as json_file:
                    existing_data = json.load(json_file)

                # متغير لتحديد إذا كان المستخدم جديدًا
                is_new_vip = False

                # التحقق مما إذا كان المستخدم يمتلك خطة VIP بالفعل
                if user_id in existing_data and 'timer' in existing_data[user_id]:
                    # جلب وقت انتهاء الخطة الحالي
                    current_expiration_str = existing_data[user_id]['timer']
                    current_expiration_time = datetime.strptime(current_expiration_str, "%Y-%m-%d %H:%M")

                    # إضافة الساعات الجديدة إلى الوقت المتبقي
                    new_expiration_time = current_expiration_time + timedelta(hours=additional_hours)
                    new_expiration_str = new_expiration_time.strftime("%Y-%m-%d %H:%M")
                    
                    # تحديث بيانات المستخدم
                    existing_data[user_id]['timer'] = new_expiration_str
                else:
                    # المستخدم جديد، يتم إضافة اشتراك VIP جديد
                    new_expiration_time = current_time + timedelta(hours=additional_hours)
                    new_expiration_str = new_expiration_time.strftime("%Y-%m-%d %H:%M")
                    plan = 'VIP Subscribed'

                    # تحديث بيانات المستخدم الجديد
                    existing_data[user_id] = {
                        'timer': new_expiration_str,
                        'plan': plan
                    }

                    # تعيين المستخدم كـ VIP لأول مرة
                    is_new_vip = True

                # كتابة البيانات المعدلة إلى data.json
                with open('data.json', 'w') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

                # حساب المدة بالأيام والساعات
                total_hours = (new_expiration_time - current_time).total_seconds() / 3600
                duration_days = int(total_hours // 24)
                remaining_hours = int(total_hours % 24)

                # بناء النص لعرض الأيام والساعات
                duration_display = f"{duration_days} day{'s' if duration_days > 1 else ''} and {remaining_hours} hour{'s' if remaining_hours > 1 else ''}"

                # يوم الفوترة التالي
                next_billing_day = new_expiration_time.strftime("%d-%m-%Y %H:%M:%S")

                # الحصول على تفاصيل المستخدم
                try:
                    chat = bot.get_chat(user_id)
                    frs = chat.first_name
                    use = chat.username
                    user_display = f"Name: {frs}\nUsername: @{use}" if use else f"Name: {frs}\nUsername: Not Available"
                except Exception as e:
                    user_display = f"Name: Unknown\nUsername: Unknown"

                # إرسال رسالة إلى المشرف
                bot.send_message(chid, f'''- Done Update -> <code>{user_id}</code> 

• Subscription Duration -> {duration_display}
• {user_display}
- Updated in Subscribers List ✅''')

                # إرسال رسالة ترحيب فقط إذا كان المستخدم جديدًا
                if is_new_vip:
                    combined_message = (
                        f"Hello, Thank you for renewing your NINJA CHK membership! [🇺🇸]\n\n"
                        f"You can check the details here:\n\n"
                        f"Days Added: {duration_days}\n"
                        f"Next Billing Day: {next_billing_day}\n"
                        f"Membership Condition: VIP Subscribed!\n\n"
                    )

                    # إرسال الرسالة المدمجة إلى المستخدم
                    bot.send_message(user_id, combined_message)

            else:
                bot.send_message(chid, ' - Unauthorized Access !!!!')
        except Exception as e:
            bot.reply_to(message, f'- Was An Error -> {e}')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()


@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𓆩𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆𓆪! 🎉🐥   𝐃ev : 『@f_k4f』  »»{timer}
🐥»»{typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='saiccchk-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>╠═══════════════════════════╣
𓆩𝐊𝐞𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝𓆪
                       🌹💸	
✿├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
✿├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
✿├『@f_k4f』
✿├𝑲𝒆𝒚 »»»<code>{pas}</code>	
✿├𝙐𝙨𝙖𝙜𝙚»»»/redeem [𝗞𝗘𝗬]
╠════════════════════════════╣
</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()







def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
		continue