# -*- coding: UTF-8 -*-
# -*Application Start*-
class Berbon(object):
    location = '天府大道中段'#类属性，实例共享
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.__dev = 'FED'#不可访问属性
    def say(self):
        print (self.name)
        print (self.type)
        print (self.__dev)

appCCB = Berbon('建设银行', 'O2O')
appBeiLong = Berbon('贝利龙', 'C2C')

appCCB.say()
print ('====================')
appBeiLong.say()
print ('====================')
#rint (appCCB.__dev)
print (appCCB.location)
# -*Application End*-