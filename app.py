from attributeLibrary import AttributeLibrary
from gladiator import Gladiator
from builder import GladiatorBuilder


class App():

    def __init__(self):
        self.ALL_FUNCTIONS = {
            "create": {"method": self.createGladiator, "description": "Для создания Гладиатора"},
            "list": {"method": self.listGladiators, "description": "Для просмотра всех созданных гладиаторов"},
            "delete": {"method": self.deleteGladiator, "description": "Для удаления гладиатора из списка"},
            "exit": {"method": self.exitApp, "description": "Для выхода"},
        }
        self.EXIT_CODE = "exit"
        self.gladiatorList = []

    def inputCommand(self):
        DESCRIPTION = "Используй следующие коммандны: \n" + "\n".join(["%s: %s" %
                                                                       (key, self.ALL_FUNCTIONS[key]["description"])
                                                                       for key in self.ALL_FUNCTIONS.keys()])
        print(DESCRIPTION)
        command = ""
        while command != self.EXIT_CODE:
            command = input("command: ").lower()
            try:
                self.ALL_FUNCTIONS[command]["method"]()
            except KeyError:
                print(" \nОй, что - то пошло не так!\n ")
                print(DESCRIPTION)

    def createGladiator(self):
        self.gladiatorList.append(GladiatorBuilder().readAttributes(AttributeLibrary.BASE_SET))

    def listGladiators(self):
        if len(self.gladiatorList) == 0:
            print("нет созданных гладиаторов.")
            return
        for glad in self.gladiatorList:
            print("")
            print(Gladiator(glad))

    def deleteGladiator(self):
        if len(self.gladiatorList) > 0:
            self.listGladiators()
            gladiatorName = str(input("Введите имя гладиатора которого необходимо удалить" + "\n"))
            print("Удаляем "+ gladiatorName)
            for name in self.gladiatorList:
                print(name["nm"])
        else:
            self.listGladiators()

    def exitApp(self):
        print("спасибо что воспользовались нашими услугами")

if __name__ == "__main__":
    App().inputCommand()
