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

    qrGenerator.generateBasicQR("https://www.tomaston.dev", fill_color='rgb(15, 22, 36)', back_color='rgb(156, 201, 227)')
    qrGenerator.generateQRWithLogo("https://www.tomaston.dev", fill_color='rgb(15, 22, 36)', back_color='rgb(156, 201, 227)')