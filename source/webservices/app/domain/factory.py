from app.domain.base import Base
import re
from app.domain import RegexBasicFormat, RegexFormatTwo, RegexFormatThree, RegexFormatFour


class Factory(Base):

    def __init__(self):

        self.phone = ""
        self.__street_name = ""
        self.__number = ""
        self.__neighbourhood = ""
        self.__city = ""
        self.__state = ""

    def get_address(self):
        address = '{number} {street_name}'.format(number=self.__number, street_name=self.__street_name)

        if not address and not address.isspace():
            address += ', {neighbourhood}'.format(neighbourhood=self.__neighbourhood)

        if not address and not address.isspace():
            address += ', {city}'.format(city=self.__city)

        if not address and not address.isspace():
            address += ' - {state}'.format(state=self.__state)

        return address

    def set_address(self, address: str):
        if re.match(RegexBasicFormat, address):
            self.__split_basic_format(address)
        elif re.match(RegexFormatTwo, address):
            self.__split_format_two(address)
        elif re.match(RegexFormatThree, address):
            self.__split_format_three(address)
        elif re.match(RegexFormatFour, address):
            self.__split_format_four(address)
        else:
            raise Exception('El formato de la dirrecion no corresponde a algun formato valido')

    def to_json(self):
        return {'phone': self.phone, 'address': self.get_address()}

    def __split_basic_format(self, address: str):
        params = address.split(' ')
        self.__number = ""
        self.__street_name = ""

        sw = True
        for param in params:
            if sw:
                self.__number = param.strip()
                sw = False
            else:
                if not param and not param.isspace():
                    self.__street_name += ' {param}'.format(param=param.strip())

    def __split_format_two(self, address: str):
        self.splitBasicFormat(address)
        params = self.__street_name.split(', ')
        sw = True

        for param in params:
            if sw:
                self.__street_name = param.strip()
                sw = False
            else:
                if not param and not param.isspace():
                    self.__neighbourhood += ' {neighbourhood}'.format(neighbourhood=param.strip())

    def __split_format_three(self, address: str):
        self.__split_format_two(address)
        params = self.__neighbourhood.split(', ')
        sw = True

        for param in params:
            if sw:
                self.__neighbourhood = param.strip()
                sw = False
            else:
                if not param and not param.isspace():
                    self.__city += ' {city}'.format(city=param.strip())

    def __split_format_four(self, address: str):
        self.__split_format_three(address)
        params = self.__city.split('- ')
        sw = True

        for param in params:
            if sw:
                self.__city = param.strip()
                sw = False
            else:
                if not param and not param.isspace():
                    self.__state += ' {state}'.format(state=param.strip())
