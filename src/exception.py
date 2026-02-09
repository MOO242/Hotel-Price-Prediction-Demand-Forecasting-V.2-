import sys


def err_message_details(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with error message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        self.error_message = err_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
