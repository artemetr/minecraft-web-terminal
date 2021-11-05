class WsStandardResponses:
    invalid_data_format = dict(status=False, error='Invalid data format')
    undefined_action = dict(status=False, error='Undefined action')
    success_auth = dict(status=True, action='auth', response='Auth was successful')
    auth_failed = dict(status=False, action='auth', error='Incorrect auth data')
    auth_timeout = dict(status=False, action='auth', error='Auth timeout')

    @staticmethod
    def log_message(message: str, type_: str = None):
        return dict(action='log_message', response=dict(message=message, type=type_))


class WsLogMessageTypes:
    error = 'error'
    input = 'input'
    output = 'output'
