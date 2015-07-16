from attributeLibrary import AttributeLibrary


class Gladiator:

    def __init__(self, attributes):
        self.attributes = attributes

    def __repr__(self):
        return "\n".join(["%s => %s" % (AttributeLibrary.ALL_ATTRIBUTES[key]["name"],
                                        value) for key, value in self.attributes.items()])
