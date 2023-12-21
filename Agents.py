import random

def generate_random_user_agent():
    brand_models = {
        "Samsung": ["Galaxy S21", "Galaxy A52", "Galaxy Note 20", "Galaxy Z Fold 2", "Galaxy S20", "Galaxy A71", "Galaxy Tab S7"],
        "Realme": ["8 Pro", "Narzo 30", "C25", "7", "X7 Pro", "GT"],
        "LG": ["G8 ThinQ", "V60 ThinQ", "Velvet", "G7", "Stylo 6", "Gram"],
        "Motorola": ["Moto G Power", "Moto Razr", "Moto Edge", "Moto G Stylus", "Moto One Fusion+", "Moto G Play"],
        "Sony": ["Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 5 II", "Xperia 1 II", "Xperia XZ3"],
        "Oneplus": ["9 Pro", "8T", "Nord", "7T", "6T", "9R"],
        "Vivo": ["X60 Pro", "Y20", "V21e", "S1 Pro", "Nex", "X50 Pro"],
        "Oppo": ["Find X3 Pro", "A74", "Reno 5", "F19 Pro", "A54", "Find X2 Neo"],
        "Infinix": ["Hot 10", "Note 10 Pro", "Zero 8", "Smart 5", "Hot 9", "Note 8"],
        "Techno": ["Camon 17 Pro", "Spark 7", "Phantom X", "Pova", "Camon 16", "Spark 5 Pro"],
        "Itel": ["Vision 1", "A23", "P37", "S16", "A56", "A25"],
        "Qmobile": ["QInfinity Prime", "Noir E3 Dual", "Black Two", "Evok Power", "I8i", "L2 Classic"],
        "Amazon": ["Kindle Fire HD 10", "Fire HD 8", "Fire 7", "Kindle Oasis", "Fire HD 10 Plus", "Fire HD 8 Kids Edition"],
        "Micromax": ["In Note 1", "In 1b", "iN 2b", "In 1", "Canvas Infinity", "Bharat 5 Pro"]
    }

    language_codes = ["en_US", "bn_BD", "en_GB", "es_ES", "fr_FR", "de_DE"]

    fba_version = ["59.0.0.15.313", "60.0.0.20.234", "61.0.0.22.283", "96.0.0.17.70", "101.0.0.18.70", "126.0.0.23.77", "141.0.0.31.91"]

    fbb_version = str(random.randint(0, 999999999))
    density = f"{random.uniform(1.0, 3.0):.1f}"
    width = str(random.randint(300, 1200))
    height = str(random.randint(500, 1500))
    fbcr = random.choice(["Jazz", "Null", "Verizon", "AT&T", "T-Mobile", "Sprint", "Vodafone", "Airtel", "Grameenphone", "Robi", "Teletalk", "Banglalink", "MTN", "9mobile", "Globacom"])
    fbsv = str(random.randint(6, 12))
    fbop = random.choice(["1", "2", "3", "4", "5"])
    fbca = random.choice(["arm64-v8a", "armeabi-v7a"])
    fbpn = random.choice(["com.facebook.katana", "com.facebook.lite", "com.instagram.android", "comfacebook.orca"])

    brand = random.choice(list(brand_models.keys()))
    fbmf = brand
    fbdv = f"{brand} {random.choice(brand_models[brand])}"
    fblc = random.choice(language_codes)

    fban = f"[FBAN/FB4A;FBAV/{random.choice(fba_version)};FBBV/{fbb_version};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{brand};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBOP/{fbop};FBCA/{fbca}]"

    return fban

# Ask the user for input on the number of user agents to generate
num_agents = int(input("Enter the number of user agents to generate: "))

# Ask the user for the file path to save the generated user agents
file_path = input("Enter the file path to save the generated user agents (e.g., 'user_agents.txt'): ")

# Generate the specified number of random user agents
with open(file_path, 'w') as file:
    for _ in range(num_agents):
        random_user_agent = generate_random_user_agent()
        file.write(random_user_agent + '\n')

print(f"User agents have been saved to {file_path}")

# Generate the specified number of random user agents
for _ in range(num_agents):
    random_user_agent = generate_random_user_agent()
    print(random_user_agent)
