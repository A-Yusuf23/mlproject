import sys
import logging

def error_message_details(error, error_details):
    _, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name: {}, line number: {}, error message: {}".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message
class customException(Exception):
    def __init__(self, error_message,error_detaile:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detaile)

        def str__(self):
            return self.error_message
        
        if __name__ == "__main__":
            try:
                a = 1/0
            except Exception as e:
                logging.info("Divide by zero")
                raise customException(e,sys) from e
    logging.info("Logging has started")