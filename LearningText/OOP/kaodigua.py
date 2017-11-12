#coding=gbk
class Kaodigua:
    def __init__(self):
        self.cookLevel=0
        self.cookString='生的'
        self.cookElement=[]
    def __str__(self):
        msg=self.cookString+'地瓜'
        if len(self.cookElement)>0:
            msg=msg+'('
            for ele in self.cookElement:
                msg=msg+ele+','
            msg=msg.strip(',')#去掉msg首尾的逗号
            msg=msg+')'
        return msg
    def addElements(self,element):
        self.cookElement.append(element)
    '''cook方法'''
    def cook(self,time):
        self.cookLevel+=time
        if self.cookLevel>=8:
            self.cookString='地瓜烤成灰了。。。'
            print('地瓜烤成灰了。。。')
        elif self.cookLevel>=5:
            self.cookString='地瓜烤熟了。。。'
            print('地瓜烤熟了。。。')
        elif self.cookLevel>=3:
            self.cookString='地瓜还没熟。。。'

            print('地瓜还没熟。。。')
        else:
            print('还是生的。。。')

newDigua=Kaodigua()
newDigua.cook(1)
newDigua.addElements('辣椒')
print(newDigua)


