def shoha_menu():
    UMO="IN-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/GitHub6G/Git-Hub/blob/main/Approval.txt").text
    if id in DARK:
        'main()'
    else:
        os.system("clear")
        os.system("xdg-open https://chat.whatsapp.com/KQaGgAfTTQOI3UtM3EyIKf")
        time.sleep(3.0)
        
        os.system("clear")
        logo()
        print( '''    ╭──────  \x1b[1;92m•\x1b[1;91m•\x1b[1;96m• \x1b[0m DETAILS \x1b[1;96m•\x1b[1;91m•\x1b[1;92m• \x1b[0m  ──────────╮
    │       YOUR KEY IS NOT APROVED       │
    │         THIS TOOL IS PAID           │   
    ╰─────────────────────────────────────╯''')
        print ("")
        print("")
        print ( '''  ╭─────  \x1b[1;92m•\x1b[1;91m•\x1b[1;96m• \x1b[0m PAYMENT METHOD \x1b[1;96m•\x1b[1;91m•\x1b[1;92m• \x1b[0m  ────────╮
  │          	 JAZZCASH     	      	    │
  │            				    │   
  │    15 Days 350RS | 30 Days 600RS        │  
  │          			    	    │
  ╰─────────────────────────────────────────╯''')
        print("")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        name = input(" Your Name : ")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://wa.me/+923021431324")
        shoha_menu()

shoha_menu() 
