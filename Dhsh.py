import os
import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from tools import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
import threading
import jwt
stopuser = {}
token = '7409683013:AAHryuB4lwt_1oFdqfrQERwOeRsXYpYjjVo'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=7270942727
admins=['7270942727']
myid = ['7270942727']

# ====== نظام النجوم ======
@bot.message_handler(commands=["mystars"])
def mystars(message):
    user_id = str(message.from_user.id)
    with open('data.json', 'r') as f:
        data = json.load(f)
    stars = data.get(user_id, {}).get("stars", 0)
    bot.send_message(message.chat.id, f"🌟 لديك حالياً {stars} نجمة.")

@bot.message_handler(commands=["addstars"])
def addstars(message):
    if str(message.from_user.id) not in admins:
        return bot.reply_to(message, "❌ غير مصرح لك.")
    try:
        args = message.text.split()
        target_id = args[1]
        amount = int(args[2])
        with open("data.json", "r") as f:
            data = json.load(f)
        if target_id not in data:
            return bot.send_message(message.chat.id, "❌ المستخدم غير موجود")
        data[target_id]["stars"] = data[target_id].get("stars", 0) + amount
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        bot.send_message(message.chat.id, f"✅ تمت إضافة {amount} نجمة للمستخدم {target_id}")
    except:
        bot.send_message(message.chat.id, "❗ الاستخدام: /addstars <id> <عدد>")

@bot.message_handler(commands=["buy"])
def buy(message):
    user_id = str(message.from_user.id)
    try:
        hours = int(message.text.split()[1])
    except:
        return bot.reply_to(message, "❗ الاستخدام: /buy <عدد الساعات>")

    with open("data.json", "r") as f:
        data = json.load(f)

    if user_id not in data:
        return bot.reply_to(message, "❌ لم يتم العثور على بياناتك.")

    stars = data[user_id].get("stars", 0)
    price = hours * 10
    if stars < price:
        return bot.reply_to(message, f"❌ لا تملك عدد كافٍ من النجوم. السعر: {price} نجمة")

    data[user_id]["stars"] -= price
    data[user_id]["plan"] = "VIP"
    now = datetime.now()
    expiry = now + timedelta(hours=hours)
    data[user_id]["timer"] = expiry.strftime("%Y-%m-%d %H:%M")

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    bot.send_message(message.chat.id, f"✅ تم تفعيل VIP لمدة {hours} ساعة. 🌟 تم خصم {price} نجمة.")
# ====== نهاية نظام النجوم ======

f = Faker()
name = f.name()
mail = f.email()
#تحديث 6.2
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start","help"])
def start(message):
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		id=message.from_user.id
		name = message.from_user.first_name
		try:BL=(json_data[str(id)])
		except:
			BL='Free'
			file_path = 'data.json'
			file = open('data.json', 'r+')
			json_data = json.load(file)
			new_data = {
				id : {
	  "plan": "Free",
	  "timer": "none",
	  "funds": 0,
	  "order": ""
				}
			}
			json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
		keyboard = types.InlineKeyboardMarkup()
		
		username = message.from_user.first_name
		
		button2 = types.InlineKeyboardButton(text='My Account', callback_data='acc')
		
		contact_button = types.InlineKeyboardButton(text="ϟ مطور", url="https://t.me/eh_m9")
		
		
		
		ptome = types.InlineKeyboardButton(text="- Auth Getaway ",callback_data='tome1')
		
		ktome = types.InlineKeyboardButton(text="-  Charge Getaway ",callback_data='tome2')
		
		otome = types.InlineKeyboardButton(text="-  Tool",callback_data='tome3')
		
		ptome1 = types.InlineKeyboardButton(text="- 3D OTP ",callback_data='DOLARc')		   		
			

		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		keyboard.add(ptome,ktome)		
		keyboard.add(otome,ptome1)			
		msg = bot.reply_to(message, f'''<b>✨
𝗛𝗶 𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲𝘀 𝗼𝗿 𝗖𝗵𝗮𝗿𝗴𝗲 𝗚𝗮𝘁𝗲𝘀.</b>''', reply_markup=keyboard)

@bot.message_handler(commands=["NONONO"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗙𝗥𝗘𝗘 
/bin معلومات بين 
/fake  fake infrot ..US 
/gen Generate cards 
....
𝗩𝗜𝗣 

❤️‍🔥	
━━━━━━━━━━━━
لوحه قديمه سيبك منهت

━━━━━━━
[ϟ] Name: Braintree Auth 1
[ϟ] Format: /chk card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User

━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 2
[ϟ] Format: /b3 card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree chareh 5$
[ϟ] Format: /br card|month|year|cvv
[ϟ] Condition: ON ✅
[ϟ] Type: Only-Vip-User
--
[ϟ] Name: Braintree chareh 1$
[ϟ] Format: /cc card|month|year|cvv
[ϟ] Condition: ON ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: OTP PayPAL V1
[ϟ] Format: /vbv card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: OTP PayPAL V2 
[ϟ] Format: /otp card|month|year|cvv
[ϟ] Condition: OFF ❌
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: OTP PayPAL V3
[ϟ] Format: /vbv3 card|month|year|cvv
[ϟ] Condition: OFF ❌
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Googel Play 0.1$
[ϟ] Format: /go card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: payPaL chareg 1.10$
[ϟ] Format: /pp card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: strip auth 
[ϟ] Format: /au card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name:  PayFow cvv Auth
[ϟ] Format: /pay card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: strip chareg 6$ 
[ϟ] Format: /ss card|month|year|cvv
[ϟ] Condition: ON✅
[ϟ] Type: Only-Vip-User


𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=1960659712'>Itachi 𝙈</a>
━━━━━━━━━━━━━━━━━━━
ϟ - We will adding More Gates....</b>
''',reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == 'tome1')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='VIP', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)    
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = '''-
				𝙰𝚞𝚝𝚑 ❤️‍🔥
ON ✅ Braintree Auth  [قريبا]
- - - - - - - - - - - - - - - - - - - - - - - - 
ON ✅ Stripe AuthV1 [/str]
- - - - - - - - - - - - - - - - - - - - - - - - 

- - - - - - - - - - - - - - - - - - - - -''',
reply_markup=keyboard,parse_mode="HTML")
 
@bot.callback_query_handler(func=lambda call: call.data == 'DOLARc')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='VIP', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)    
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = '''-
			OTP
ON✅OTP paypal V1 [/vbv]
- - - - - - - - - - - - - - - - - - - - - - - - 
ON✅OTP paypal V2 [/vv]
- - - - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - -''',
reply_markup=keyboard,parse_mode="HTML")

                         
                                                                         
@bot.callback_query_handler(func=lambda call: call.data == 'plans')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='VIP', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	contact_button = types.InlineKeyboardButton(text="ϟ للشتراك", url="https://t.me/eh_m9")	
	keyboard.row(back,contact_button)    
	
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = '''
اسعار اشتراك في بوت فحص Itachi 
✮ 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗦𝗲𝗰𝘁𝗶𝗼𝗻 ✮

𝐏𝐑𝐈𝐂𝐈𝐍𝐆 :
♤ 1𝗗𝗮𝘆𝘀 ⥊ 1$	
♤ 𝟯 𝗗𝗮𝘆𝘀 ⥊ 𝟯 $
♤ 𝟕 𝗗𝗮𝘆𝘀 ⥊ 𝟕 $
♤ 𝟏𝟓 𝗗𝗮𝘆𝘀 ⥊ 𝟭𝟯 $
♤ 𝟯𝟬 𝗗𝗮𝘆𝘀 ⥊ 𝟮𝟱 $

𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐌𝐞𝐭𝐡𝐨𝐝𝐬 : اقبل USDT and TON and نجوم and يورزات ثلاثي 
BOT DOLAR
- - - - - - - - - - - - - - - - - - - - -''',
reply_markup=keyboard,parse_mode="HTML")        
                         

@bot.callback_query_handler(func=lambda call: call.data == 'tome2')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='VIP', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)    
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = '''
				Charge 🔥
ON ✅ Stripe Charge 3.50$ [قريبا]
- - - - - - - - - - - - - - - - - - - - - - - - 
ON ✅ Braintree Charge [قريبا]

- - - - - - - - - - - - - - - - - - - - -''',
reply_markup=keyboard,parse_mode="HTML")
                         
                         
                         
                         
                         
                         
                         
@bot.callback_query_handler(func=lambda call: call.data == 'tome3')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='VIP', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)    
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text ='''
			Tool🌟
BIN Info Lookup [/bin]
CC Generate [/gen]
To create fake information [/fake]
id acaont [/id]
- - - - - - - - - - - - - - - - - - - - -''',
reply_markup=keyboard,parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu_callbacrk(call):
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text="ϟ - مطور", url="https://t.me/eh_m9")
	ptome = types.InlineKeyboardButton(text="- Auth Getaway ",callback_data='tome1')
	ktome = types.InlineKeyboardButton(text="-  Charge Getaway ",callback_data='tome2')
	otome = types.InlineKeyboardButton(text="-  Tool",callback_data='tome3')
	
	ptome1 = types.InlineKeyboardButton(text="- 3D OTP ",callback_data='DOLARc')
	
	
	keyboard.add(ptome,ktome)		
	keyboard.add(otome,ptome1)	
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = f'''<b>
✨
𝗛𝗶 𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲𝘀 𝗼𝗿 𝗖𝗵𝗮𝗿𝗴𝗲 𝗚𝗮𝘁𝗲𝘀.</b>''',
reply_markup=keyboard,parse_mode="HTML")
					  					  

@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 </b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 </b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		back1 = types.InlineKeyboardButton(text='خروج🔙', callback_data='menu')		
		
		bra = types.InlineKeyboardButton(text=f"- Braintree Auth ",callback_data='br')
		
		
		ip = types.InlineKeyboardButton(text=f"- Stripe Auth ",callback_data='str')
		
		stch = types.InlineKeyboardButton(text=f"- Stripe Charge ",callback_data='sch')
		
		ot1 = types.InlineKeyboardButton(text=f"- Braintree LookUp 1",callback_data='otp1')
		
		ot2 = types.InlineKeyboardButton(text=f"- Braintree LookUp 2",callback_data='otp2')
		
		
		keyboard.add(bra)
		keyboard.add(ip)
		keyboard.add(stch)
		keyboard.add(ot1)
		keyboard.add(ot2)
		
		bot.reply_to(message, text=f'𝐁𝐎𝐓 𝐕𝐈𝐏 Itachi  𝐒𝐎𝐃𝐎 /𝐝𝐫 𝐁𝐎𝐓',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		cooo = (f"com{id}.txt")
		with open(cooo, "wb") as w:
			w.write(ee)


	

	

######################

# Braintree Auth 

######################

@bot.callback_query_handler(func=lambda call: call.data == 'قريبا')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(bran(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ @eh_m9 ''', reply_markup=mes)
					
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
					
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					
					msg=f'''<b>Approved ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''
					cv = f'''<b> CVV ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

					if "Approved !✅" in last or "The card's security code is incorrect." in last or 'Approved ✅! - Duplicate' in last or 'Approved ✅! - AVS' in last or 'Approved ✅! - Invalid postal code and cvv' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'Card Issuer Declined CVV' in last:
						bot.send_message(call.from_user.id, cv)	
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		






#######################

# Stripe Auth 

######################

@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Stripe Auth'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ @eh_m9 ''', reply_markup=mes)
					
					

					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
					
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					
					msg=f'''<b>Approved ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

					if 'Payment Method Successfully Added' in last or "success" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		


#######################

# Stripe Charge 

######################

@bot.callback_query_handler(func=lambda call: call.data == 'sch')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Stripe Charge 3.50$'
		dd = 0
		live = 0
		ch = 0
		fun = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(cha(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• APPROVED ✅ ➜ [ {live} ] •", callback_data='x')
					inn = types.InlineKeyboardButton(f"• Insufficient Funds ✅ ➜ [ {fun} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• DECLIEND ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• TOTAL 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,inn,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ @eh_m9 ''', reply_markup=mes)
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
					
					cc = n+'|'+mm+'|'+yy+'|'+cvc
 
					inf = f'''<b>Insufficient Funds ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''
					
					msg=f'''<b>Approved ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

					if "CHARGED - 3.50$ ✅" in last :
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'Insufficient Funds' in last:
						fun += 1
						bot.send_message(call.from_user.id, inf)
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
	
	
	
	
	
	
	


########################

# Braintree LookUp 1

########################

@bot.callback_query_handler(func=lambda call: call.data == 'otp1')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree LookUp 1'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('??𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(otp1(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• PASSED ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• REJECTED ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• TOTAL 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ @eh_m9 ''', reply_markup=mes)
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
					
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					
					msg=f'''<b> PASSED ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

					if "challenge_required" in last :
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		

	
	




################

# Braintree Lookup 2

################



@bot.callback_query_handler(func=lambda call: call.data == 'otp2')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree LookUp 2'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(otp2(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• PASSED ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• REJECTED ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• TOTAL 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ @eh_m9 ''', reply_markup=mes)
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
					
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					
					msg=f'''<b> Passed ✅

[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
{str(dato(cc[:6]))}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''
					if "challenge_required" in last :
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @eh_m9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		

















#######################

#Braintree Auth

#######################

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(bran(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>Approved ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	cv=f'''<b>CVV ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	msgd=f'''<b>DECLINED ❌

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	if "Approved !✅" in last or 'Approved ✅! - Duplicate' in last or 'Approved ✅! - AVS' in last or 'Approved ✅! - Invalid postal code and cvv' in last or 'Charged ✅' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif 'Card Issuer Declined CVV' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=cv)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	





######################

# Stripe Auth

######################
				
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='stripe Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b> Approved ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	msgd=f'''<b> DECLINED ❌

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''
	if "Payment Method Successfully Added" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
		
		

	
		
			
				

################

# Stripe Charge 3.50$

################

	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.ch') or message.text.lower().startswith('/ch'))
def respond_to_vbv(message):
	gate='Stripe Charge 3.50$'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(cha(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b> APPROVED ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	msgd=f'''<b> DECLINED ❌

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	inf = f'''<b> Insufficient Funds ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	if "CHARGED - 3.50$ ✅" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif 'Insufficient Funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=inf)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	
		





		
########################

# Braintree LookUp 1	
			
########################
		
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	gate='Braintree LookUp 1'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(otp1(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	
	msg=f'''<b> Passed ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	msgd=f'''<b> REJECTED ❌

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	if "challenge_required" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	
	
	
	
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vv') or message.text.lower().startswith('/vv'))
def respond_to_vbv(message):
	gate='Braintree LookUp 2'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/eh_m9")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(otp2(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	
	msg=f'''<b> Passed ✅

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	msgd=f'''<b> REJECTED ❌

[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

{str(dato(cc[:6]))}

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @eh_m9⚡</b>'''

	if "challenge_required" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)




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
			msg=f'''<b>𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
			تم تفعيل الاشتراك الخاص بك
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
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
			pas = 'ITACHI-'+'2025'+'-'+''.join(random.choices(characters, k=4))
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
			msg=f'''<b>ꁴ Code Created Successfully ✅		

ꁴ Expire in ➩ {ig}
ꁴ Code ➩ <code>{pas}</code>

ꁴ For redeem The Code Use /redeem code</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()





@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or 'NoUsername'  # التعامل مع حالة عدم وجود اسم مستخدم
    
    response_message = f'''» bilgi ✅ {user_first_name}
        ID » <code>{user_id}</code>
Name » {user_first_name}
Userame » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')



	
	
	
@bot.message_handler(commands=['scr'])
def send_sc_messages(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "Scraping Started...⏳")
    command_parts = message.text.split()

    if len(command_parts) < 3:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, 
                              text="Command format: /scr [username/bin] [limit]")
        return

    input_data = command_parts[1]
    limit = int(command_parts[2])

    if input_data.isdigit() and len(input_data) >= 6:  # نفترض أن البين يتكون من 6 أرقام على الأقل
        # سكرب من بين
        bin = input_data
        count = limit

        cards = generate_cards(bin, count)
        file_path = "ITACHI.txt"

        with open(file_path, "w") as file:
            file.write("\n".join(cards))

        bin_info = get_bin_info(bin[:6])

        additional_info = (f'''
            ●●●●●●●●●●●

• Name ~ Scraperer 🧡, 

• Bin ~ {bin[:10]}\n

• Total Found ~ {count}\n
●●●●●●●●●●●
        ''')

        with open(file_path, "rb") as file:
            bot.send_document(chat_id, file, caption=additional_info)
            bot.delete_message(chat_id=chat_id, message_id=initial_message.message_id)
    else:
        # سكرب من قناة
        username = input_data

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        messages_text, channel_name = loop.run_until_complete(get_last_messages(username, limit))

        if channel_name:
            save_to_file(messages_text)

            file_len = len(messages_text.split('\n')) if messages_text else 0
            captain_info = f"""
●●●●●●●●●●●

• Name ~ Scr

• Channel ~ {channel_name}

• Total Found ~ {file_len}

●●●●●●●●●●●"""

            with open('ITACHI.txt', 'rb') as file:
                markup = types.InlineKeyboardMarkup()
                
                dev_button = telebot.types.InlineKeyboardButton(text="𝗗𝗘𝗩", url='https://t.me/eh_m9')
                markup.add(dev_button)
                bot.send_document(chat_id, file, caption=captain_info, parse_mode='none', reply_markup=markup)
                bot.delete_message(chat_id=chat_id, message_id=initial_message.message_id)
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, 
                                  text="Failed to get messages from the channel.")


    
    
    
    
    
    




@bot.message_handler(func=lambda message: message.text.lower().startswith('.seecr') or message.text.lower().startswith('/seecr'))
def respond_to_vbv(message):
	def my_function():
		
		cmd=message.text
		try:
			try:
				link=cmd.split(' ')[1]
				amount=cmd.split(' ')[2]
				if int(amount) > 10000000:
					ko = (bot.reply_to(message, "<b>The maximum limit is 10000000 🜨</b>",parse_mode="HTML").message_id)
					return
			except:
				ko = (bot.reply_to(message, "<b>Usage: /scr username amount bin (optional)</b>",parse_mode="HTML").message_id)
				return
			try:
				key=cmd.split(' ')[3]
			except:
				key=''
			ko = (bot.reply_to(message, "<b>Scraping...⌛</b>",parse_mode="HTML").message_id)
		
			def heavy_task():
				start_time = time.time()
				response = requests.get(f'https://il-p-26-d89b06c63011.herokuapp.com/scraper?link={link}&amount={amount}&keyword={key}')
				ccs=(response.text)
				if 'server encountered an internal' in ccs:
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Oops! encountered an error while scraping. Here are the details:
	
➜ Code: USERNAME_INVALID
➜ Message: The username is invalid
	
Please make sure you entered the correct username. If you believe this is an error, please check the spelling and try again. If the issue persists, kindly reach out to our support team for further assistance.</b>''',parse_mode="HTML")
					return
				name=(message.from_user.first_name)
				user=message.from_user.username
				with open('DOLAR.txt', 'w') as file:
					file.write(ccs)
				end_time = time.time()
				execution_time = end_time - start_time
				ui=len(ccs)
				try:
					bot.send_document(message.chat.id, open('ITACHI.txt', 'rb'),caption=f'''<b>𝑺𝑪𝑹𝑨𝑷𝑷𝑰𝑵𝑮 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬𝑫 ✅
		
𝑺𝑶𝑼𝑹𝑪𝑬 ➜ {link}
𝑨𝑴𝑶𝑼𝑵𝑻 ➜ {amount}
𝑭𝑶𝑼𝑵𝑫 ➜ {ui}
𝑻𝑰𝑴𝑬 » ➜ {"{:.1f}".format(execution_time)} 𝑺𝑬𝑪𝑶𝑵𝑫𝑺
		
𝑹𝑬𝑸𝑼𝑬𝑺𝑻 𝑩𝒀 ➜ <a href='https://t.me/{user}'>{name}</a>

𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 ➜ @eh_m9 </b>''',parse_mode="HTML")
					bot.delete_message(message.chat.id, ko)
				except Exception as e:
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='No cards found 🚫',parse_mode="HTML")
					return
			p = Process(target=heavy_task)
			p.start()
		except Exception as e:
			print('ERROR : ',e)
			ko = (bot.reply_to(message, "<b>An unknown error has occurred</b>",parse_mode="HTML").message_id)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()




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

def dato(zh):
 
 

 
 
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''ϟ BIN Info -> {brand} - {card_type} - {level}
ϟ Bank -> {bank} - {country_flag}
ϟ Country -> {country_name} [ {country_flag} ]'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'
		
				
						
								
@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>	
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅	
ϟ - BIN -></b> <code>{cc}</code>
<b>{str(dato(cc[:6]))}</b>''')										
												

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

@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)
            # طلب معلومات الـ BIN من API
data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()																																																				
				
@bot.message_handler(func=lambda message: message.text.lower().startswith('.fake') or message.text.lower().startswith('/fake'))
def respond_to_vbv(message):
	def my_function():
		try:
			try:
				u=message.text.split('fake ')[1]
			except:
				u='US'
			parsed_data = requests.get(f'https://randomuser.me/api/?nat={u}').json()
			results = parsed_data['results']
			result = results[0]
			name = f"{result['name']['title']} {result['name']['first']} {result['name']['last']}"
			street_number = result['location']['street']['number']
			street_name = result['location']['street']['name']
			city = result['location']['city']
			state = result['location']['state']
			country = result['location']['country']
			postcode = result['location']['postcode']
			fake = Faker()
			phone = fake.phone_number()
			email = fake.email()
			formatted_address = f"""<b>📍{country} Address Generator

𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲:   	<code>{name}</code>
𝗖𝗶𝘁𝗶𝘆 𝗧𝗼𝘄𝗻 𝗩𝗶𝗹𝗹𝗮𝗴𝗲: <code>{city}</code>
𝗦𝘁𝗮𝘁𝗲/𝗣𝗿𝗼𝘃𝗶𝗻𝗰𝗲/𝗥𝗲𝗴𝗶𝗼𝗻:  <code>{state}</code>
𝗣𝗼𝘀𝘁𝗮𝗹 𝗖𝗼𝗱𝗲: <code>{postcode}</code>
𝗦𝘁𝗿𝗲𝗲𝘁 𝗔𝗱𝗱𝗿𝗲𝘀𝘀:  <code>{street_number} {street_name}</code>
𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿: <code>{phone}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{country}</code>
𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗘𝗺𝗮𝗶𝗹: {email}</b>
			"""
			bot.reply_to(message, formatted_address,parse_mode="HTML")
		except:
			bot.reply_to(message, "Country code not found or not available.")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
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
@bot.message_handler(func=lambda message: message.text.lower().startswith('.mmm') or message.text.lower().startswith('/mmm'))
def respond_to_vbv(message):
		try:
			bm = message.reply_to_message.text
		except:
		   bm=message.text
		regex = r'\d+'
		try:
			matches = re.findall(regex, bm)
		except:
			bot.reply_to(message,'<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>',parse_mode="HTML")
			return
		bin = ''.join(matches)[:6]
		ko = (bot.reply_to(message, "<b>Checking Your bin...⌛</b>",parse_mode="HTML").message_id)
		if len(re.findall(r'\d', bin)) >= 6:
			pass
		else:
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>''',parse_mode="HTML")
			return
		cc = gen(bin)
		brand, card_type, bank, country, country_flag, status = info(cc.split('|')[0])		
		if 'card_number_invalid' in status:
			msg='<b>𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌</b>'
		else:
			msg=f'''<b>
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅
	
𝐁𝐈𝐍 ➜ <code>{bin[:6]}</code>
	
𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {card_type} - {brand}  
𝐁𝐚𝐧𝐤 ➜ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}</b> '''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode="HTML")







				
			
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'	
print("BOT NEW 💫")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")