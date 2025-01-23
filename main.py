import qrcode,os
import string,random
import pyfiglet
import qrcode.constants
from colorama import Fore


def home_menu():
    print(Fore.GREEN+f"[1] TEXT to QR\n[2] SEARCH USER\n[0] EXIT")

def cl():
    os.system("cls")

def banner():
    print(Fore.RED+"-----------------------------------------")
    print("   TEXT to QR CODE GENERATOR >> TRFAHIM")
    print("------------------------------------------\n")
def ban_1():
    print(Fore.YELLOW+"\n----------------------------------")   
def ban_2():
    print("----------------------------------\n\n")

def text_banner():
    text = pyfiglet.figlet_format("TEXT to QR")
    print(Fore.GREEN+text)

def generate_qr(user_input, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,
        border=4,
    )
    
    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color="white")
    img.save(file_name)
    cl()
    text_banner()
    banner()
    ban_1()
    print((f"QR code save as '{file_name}'"))
    ban_2()
    
def back_home():
    b_home = input(Fore.BLUE+"\n[B] BACK HOME [E] EXIT >>> ").lower()
    if b_home == "b":
        main()
    elif b_home == "e":
        os._exit(0)
    else:
        main()

def main():
    cl()
    text = pyfiglet.figlet_format("TR TOOLS")
    print(Fore.RED+text)
    home_menu()
    home_input = (input(Fore.CYAN+"\n>>>> "))
    
    try:
        if home_input == "1":
            cl()
            text_banner()
            banner()
            user_input = input(Fore.CYAN+"\nENTER (URL/TEXT) HERE >> ")
            random_digits = (random.choice(string.ascii_uppercase)
                     +(random.choice(string.ascii_lowercase))
                     +(random.choice(string.digits)))
            file_name = (f"QR_image_{random_digits}.png")
            
            generate_qr(user_input, file_name)
            back_home()
    
    except ValueError:
        print("\nTRY AGAIN !!")
        
    
    
    
if __name__ == "__main__":
    main()
