#  ___________       _____                           _             
# |  _  | ___ \     |  __ \                         | |            
# | | | | |_/ /_____| |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | | | |    /______| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# \ \/' / |\ \      | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
#  \_/\_\_| \_|      \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   

'''
File: logger.py
Brief: JSON Logger
Author: Tom Aston
'''
import datetime

class Log(object):
    '''
    Brief: logger class
    '''
    __logger_template = {
        'Error number': '',
        'Error message': '',
        'Error location': '',
        'Error Object': '',
        'Additional data': '',
        'Time': '',
        'Version number': '',
    }

    __logger_info_template = {
        'Info': '',
        'Info Location': '',
        'Time': '',
        'Version number': ''
    }

    _instance = None

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def log_error(self, error_number: int, error_message: str, error_location: str, error_object: Exception,  additional_data: str) -> None:
        '''
        Brief: Writes a JSON log for a particular error
        '''
        logger_print = self.__logger_template.copy()

        logger_print['Error number'] = error_number
        logger_print['Error message'] = error_message
        logger_print['Error location'] = error_location
        logger_print['Error Object'] = str(error_object)
        logger_print['Additional data'] = additional_data
        logger_print['Time'] = str(datetime.datetime.now())
        logger_print['Version number'] = '1.0'
        
        print("[{}][Error] {}: {}".format( logger_print['Time'], error_number, error_message))
        

    def log_info(self, info_message: str, info_location: str) -> None:
        '''
        Brief: Log info rather than an error
        '''
        logger_print = self.__logger_info_template.copy()

        logger_print['Info'] = info_message
        logger_print['Info Location'] = info_location
        logger_print['Time'] = str(datetime.datetime.now())
        logger_print['Version number'] = '1.0'
        
        print("[{}][INFO] {}: {}".format( logger_print['Time'], info_location, info_message))
