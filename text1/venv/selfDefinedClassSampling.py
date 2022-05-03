from venv.dataFactory import dataFactory


class selfDefinedClassSapling(dataFactory):
    def __init__(self):
        self.__name = "selfDefinedClassSapling"
    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result