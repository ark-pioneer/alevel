class SMS():
    def __init__(self, to, from, body):
        self._to = to
        self._from = from
        self._body = body

    def send(self):
        message = self.__format_message()
        print(message)

    def __format_message(self):
        return {
            "to": self._to,
            "from": self._from,
            "body": self._body
        }
    
class Email():
    def __init__(self, to, from, body, cc, bcc):
        self._to = to
        self._from = from
        self._body = body
        self._cc = cc
        self._bcc = bcc

    def send(self):
        message = self.__format_message()
        print(message)

    def __format_message(self):
        return {
            "to": self._to,
            "cc": self._cc,
            "bcc": self._bcc,
            "from": self._from,
            "body": self._body
        }
        

# create an instance of email
# create an instance of SMS