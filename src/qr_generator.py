#  ___________       _____                           _             
# |  _  | ___ \     |  __ \                         | |            
# | | | | |_/ /_____| |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | | | |    /______| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# \ \/' / |\ \      | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
#  \_/\_\_| \_|      \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
'''
File: qr_generator.py
Brief: generate qr code functionality
Author: Tom Aston
'''
import qrcode
from PIL import Image
import qrcode.image.pil

class QrGenerator():
    '''
    bief: QR code generator functionality
    '''

    def __init__(self):
        pass


    def __createBasicQrObject(self, url: str, fill_color: str, back_color: str) -> qrcode.image.pil.PilImage:
        '''
        brief: generates foundation qr code PIL image
        '''
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        return qr.make_image(fill=fill_color, back_color=back_color)

    
    def generateBasicQR(self, url: str, fill_color: str = 'black' , back_color: str = 'white'):
        '''
        brief: generates a basic qr code
        '''
        qr_img = self.__createBasicQrObject(url, fill_color, back_color)
        qr_img.save('./basic-qr.png')

    
    def generateQRWithLogo(self, url: str, fill_color: str, back_color: str):
        '''
        brief: generates qr code with logo
        '''
        qr_img = self.__createBasicQrObject(url, fill_color, back_color)

        #resize image using LANCZOS algo (image upscaling quality filter)
        logo = Image.open('./image/logo.png').resize((75, 75), Image.LANCZOS)

        #calculate position at centre of QR code
        offset = ((qr_img.size[0] - 75) // 2, (qr_img.size[1] - 75) // 2)

        qr_img.paste(logo, offset, mask=logo.split()[3] if logo.mode == 'RGBA' else None)

        qr_img.save('./logo-qr.png')
