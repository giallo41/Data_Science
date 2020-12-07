
import logging
from attr import attrs, attrib

#@attrs
class CustomeLog:#(object):
#    file_name = attrib()
#    log_level = attrib()
 
    def __init__(self, log_level, file_name):
        self.log_level = log_level
        self.file_name = file_name
        logging.basicConfig(level = self.log_level, 
                            filename = self.file_name,  
                            filemode = 'w',
                            format='%(levelname)s : %(asctime)s : %(filename)s Line : %(lineno)d - %(message)s')
    
    def pring_log(self, txt):
        if self.log_level == logging.INFO:
            logging.info (txt)
        elif self.log_level ==logging.WARNNING:
            logging.warning(txt)
        else:
            logging.warning(txt)
        
    