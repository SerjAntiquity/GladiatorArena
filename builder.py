from gladiator import Gladiator
from collections import OrderedDict
from attributeLibrary import AttributeLibrary


class GladiatorBuilder:
    MAX_ATTRIUBE_SUM = 20

    def __init__(self):
        self.attributes = {}

    def readAttributes(self, attributesMetainfo):
        self.attributes = {attribute["code"]: self.inputAttribute(attribute["name"], attribute["converter"])
                           for attribute in attributesMetainfo}
        self.checkAtrributeSum()
        self.attributes = OrderedDict(sorted(self.attributes.items()))
        self.attributes.move_to_end('nm', last=False)
        return self.attributes

    def inputAttribute(self, attributeName, converter):
        try:
            return converter.convertValue(input("Input gladiator %s: " % (attributeName)))
        except Exception as error:
            print(error)
            return self.inputAttribute(attributeName, converter)

    def getGladiator(self):
        if len(self.attributes) < 1:
            raise Exception("Can't read it. Gladiator data not specified.")
        return Gladiator(self.attributes)

    def checkAtrributeSum(self):
        summ = 0
        for attributeMeta in AttributeLibrary.BASE_SET:
            if attributeMeta["AttrType"] == "battle":
                for attribute in self.attributes:
                    if attributeMeta["code"] == attribute:
                        summ += self.attributes[attribute]
        if summ != GladiatorBuilder.MAX_ATTRIUBE_SUM:
            print("Attribute sum must be equal to %i" % GladiatorBuilder.MAX_ATTRIUBE_SUM)
            a = input("Хотите пересоздать гладиатора? [y/n]").lower()
            if a == "y":
                self.readAttributes(AttributeLibrary.BASE_SET)
            else:
                self.attributes = {}
