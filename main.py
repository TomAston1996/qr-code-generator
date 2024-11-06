#  ___________       _____                           _             
# |  _  | ___ \     |  __ \                         | |            
# | | | | |_/ /_____| |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | | | |    /______| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# \ \/' / |\ \      | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
#  \_/\_\_| \_|      \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#ascii font Doom - https://patorjk.com/software/taag/#p=display&f=Doom&t=QR-Generator                                                  
'''
File: qr_generator.py
Brief: generate qr code functionality
Author: Tom Aston
'''

from src.qr_generator import QrGenerator

if __name__ == "__main__":

    qrGenerator = QrGenerator()

    URL: str = 'https://www.tomaston.dev'
    FILL_COLOR: str = 'rgb(15, 22, 36)'
    BACK_COLOR: str = 'rgb(156, 201, 227)'
    LOGO_FILE_PATH: str | None = './image/logo.png' 

    GENERATE_WITH_LOGO = True

    match GENERATE_WITH_LOGO:
        case True:
            qrGenerator.generateQRWithLogo(URL, FILL_COLOR, BACK_COLOR, LOGO_FILE_PATH)
        case _:
            qrGenerator.generateBasicQR(URL, FILL_COLOR, BACK_COLOR)
    