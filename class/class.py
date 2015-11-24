# -*- coding: UTF-8 -*-
# -*Application Start*-
class Berbon(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def say(self):
        print (self.name)
        print (self.type)

appCCB = Berbon('建设银行', 'O2O')
appBeiLong = Berbon('贝利龙', 'C2C')

appCCB.say()
appBeiLong.say()
# -*Application End*-