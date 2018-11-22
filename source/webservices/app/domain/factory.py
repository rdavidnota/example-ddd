from app.domain.base import Base
import re
from app.domain import RegexBasicFormat, RegexFormatTwo, RegexFormatThree, RegexFormatFour


class Factory(Base):

    def __init__( self ):
        self.phone = ""
        self.street_name = ""
        self.number = ""
        self.neighbourhood = ""
        self.city = ""
        self.state = ""

    def get_address( self ):
        address = '{number} {street_name}'.format(number=self.number, street_name=self.street_name)

        if not address and not address.isspace():
            address += ', {neighbourhood}'.format(neighbourhood=self.neighbourhood)

        if not address and not address.isspace():
            address += ', {city}'.format(city=self.city)

        if not address and not address.isspace():
            address += ' - {state}'.format(state=self.state)

        return address

    def split_basic_format( self, address: str ):
        params = address.split(' ')

        self.number = ""
        self.street_name = ""

        sw = True
        for param in params:
            if (sw):
                self.number = param
                sw = False
            else:
                self.street_name += ' {param}'.format(param=param)

    def split_format_two( self, address: str ):
        self.splitBasicFormat(address)
        params = self.streetname.split(', ')
        sw = True

        for param in params:
            if (sw):
                self.streetname = param
                sw = False
            else:
                self.neighbourhood += ' {neighbourhood}'.format(neighbourhood=param)

    def split_format_three( self, address: str ):
        self.split_format_two(address)

        params = self.neighbourhood.split(', ')
        sw = True

        for param in params:
            if (sw):
                self.neighbourhood = param
                sw = False
            else:
                self.city += ' {city}'.format(city=param)

    def split_format_four( self, address: str ):
        self.split_format_three(address)

        params = self.city.split('- ')

        sw = True

        for param in params:
            if (sw):
                self.city = param
                sw = False
            else:
                self.state += ' {state}'.format(state=param)

    def set_address( self, address: str ):
        if re.match(RegexBasicFormat, address):
            self.split_basic_format(address)
        elif re.match(RegexFormatTwo, address):
            self.split_format_two(address)
        elif re.match(RegexFormatThree, address):
            self.split_format_three(address)
        elif re.match(RegexFormatFour, address):
            self.split_format_four(address)
        else:
            raise Exception('El formato de la dirrecion no corresponde a algun formato valido')
