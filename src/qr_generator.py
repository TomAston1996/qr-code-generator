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

from src.logger import Log

class QrGenerator():
    '''
    bief: QR code generator functionality
    '''

    log = Log.get_instance()

    def __init__(self) -> None:
        '''
        brief: contructor class
        '''
        self.log.log_info(f'QR Generator class instatiated...', self.__class__.__name__)


    def __createBasicQrObject(self, url: str, fill_color: str, back_color: str) -> qrcode.image.pil.PilImage:
        '''
        brief: generates foundation qr code PIL image
        '''
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        return qr.make_image(fill=fill_color, back_color=back_color)
    

    def __remove_illegal_chars_from_url_string(self, url: str) -> str:
        '''
        beif: removes any back slashes etc from url so it can be used in the filename

        i.e. https://tomaston.dev -> tomaston.dev
        '''
        _temp_arr = url.split('.')
        return _temp_arr[len(_temp_arr) - 2] + '.' +  _temp_arr[-1]


    def generateBasicQR(self, url: str, fill_color: str = 'black' , back_color: str = 'white') -> None:
        '''
        brief: generates a basic qr code
        '''
        qr_img = self.__createBasicQrObject(url, fill_color, back_color)
        
        output_file_path = f'./basic-qr-{self.__remove_illegal_chars_from_url_string(url)}.png'

        qr_img.save(output_file_path)

        self.log.log_info(f'New QR code generated at {output_file_path}', self.__class__.__name__)

    
    def generateQRWithLogo(
            self,
            url: str,
            fill_color: str = 'black', 
            back_color: str = 'white',
            logo_file_path: str = './image/logo.png'
            ) -> None:
        '''
        brief: generates qr code with logo
        '''
        qr_img = self.__createBasicQrObject(url, fill_color, back_color)

        SIDE_LENGTH = 75

        #resize image using LANCZOS algo (image upscaling quality filter)
        logo = Image.open(logo_file_path).resize((SIDE_LENGTH, SIDE_LENGTH), Image.LANCZOS)

        #calculate position at centre of QR code
        offset = ((qr_img.size[0] - SIDE_LENGTH) // 2, (qr_img.size[1] - SIDE_LENGTH) // 2)

        qr_img.paste(logo, offset, mask=logo.split()[3] if logo.mode == 'RGBA' else None)

        output_file_path = f'./logo-qr-{self.__remove_illegal_chars_from_url_string(url)}.png'

        qr_img.save(output_file_path)

        self.log.log_info(f'New QR code generated at {output_file_path}', self.__class__.__name__)
