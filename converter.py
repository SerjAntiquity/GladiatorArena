class BaseConverter():

    def convertValue(self, inputValue):
        raise Exception("Not implemented")


class StringConverter(BaseConverter):

    def convertValue(self, inputValue):
        if len(inputValue) <= 0:
            raise Exception("Incorrect value length.")
        return str(inputValue)


class IntegerConverter(BaseConverter):

    def convertValue(self, inputValue):
        if not inputValue.isdigit():
            raise Exception("Incorrect value. Must be int, and greater than zero")
        return int(inputValue)
