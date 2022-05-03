import string

from venv.dataFactoryInterface import dataFactoryInterface

if __name__ == "__main__":
    interface = dataFactoryInterface()

    #int
    obj = interface.create("int")
    paras = {"datarange":(0,10),"num":5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    #str
    # obj = interface.create("str")
    # paras = {"datarange":string.ascii_uppercase,"num":8,"strlen":8}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    #self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num":5,"struct":{"int": {"datarange":(0,100)}, "float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)


    # self defined class
    # obj = interface.create("selfDefinedClass")
    # paras = {"num":5,"classname":"MyClass","parameters":5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)