class Yiffer:

    instance = None

    class __Yiffer:

        def yiff_me(self, name):
            return 'I like to yiff {} UwU'.format(name)

    def __init__(self):
        if self.instance == None:
            self.instance = self.__Yiffer()

    def __getattr__(self, name):
        return getattr(self.instance, name)
