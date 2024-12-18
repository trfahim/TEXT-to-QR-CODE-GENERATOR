import qrcode,os
import qrcode.constants

def banner():
    print("\n-----------------------------------------")
    print("   TEXT to QR CODE GENERATOR >> TRFAHIM")
    print("------------------------------------------\n")
def ban_1():
    print("\n--------------------------")   
def ban_2():
    print("--------------------------\n")
    
def cl():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")


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
    banner()
    ban_1()
    print(f"QR code save as '{file_name}'")
    ban_2()
    
    
def main():
    cl()
    banner()
    user_input = input("Enter the text >>> ")
    file_name = input("Enter the image name ('qr.png') >>> ")
    
    generate_qr(user_input, file_name)
    

if __name__ == "__main__":
    main()
