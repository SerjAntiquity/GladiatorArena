import converter


class AttributeLibrary():
    NAME = {"code": "nm", "name": "Name", "AttrType": "peace", "converter": converter.StringConverter()}
    RANG = {"code": "rng", "name": "Rang", "AttrType": "peace", "converter": converter.StringConverter()}
    HEALTH = {"code": "hp", "name": "Health", "AttrType": "peace", "converter": converter.IntegerConverter()}
    STRENGTH = {"code": "str", "name": "Strength", "AttrType": "battle", "converter": converter.IntegerConverter()}
    DEXTERITY = {"code": "dex", "name": "Dexterity", "AttrType": "battle", "converter": converter.IntegerConverter()}
    CONSTITUTION = {"code": "con", "name": "Constitution", "AttrType": "battle", "converter": converter.IntegerConverter()
        }
    BASE_SET = (NAME, STRENGTH, DEXTERITY, CONSTITUTION)
    ALL_ATTRIBUTES = {
        NAME["code"]: NAME,
        RANG["code"]: RANG,
        HEALTH["code"]: HEALTH,
        STRENGTH["code"]: STRENGTH,
        DEXTERITY["code"]: DEXTERITY,
        CONSTITUTION["code"]: CONSTITUTION,
    }
