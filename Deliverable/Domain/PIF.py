class PIF:
    def __init__(self):
        self.__content = []

    def content(self):
        return self.__content

    def insert(self, _id, code):
        self.__content.append((_id, code))

    def __str__(self):
        return str(self.__content)
