#coding=gbk
class Kaodigua:
    def __init__(self):
        self.cookLevel=0
        self.cookString='����'
        self.cookElement=[]
    def __str__(self):
        msg=self.cookString+'�ع�'
        if len(self.cookElement)>0:
            msg=msg+'('
            for ele in self.cookElement:
                msg=msg+ele+','
            msg=msg.strip(',')#ȥ��msg��β�Ķ���
            msg=msg+')'
        return msg
    def addElements(self,element):
        self.cookElement.append(element)
    '''cook����'''
    def cook(self,time):
        self.cookLevel+=time
        if self.cookLevel>=8:
            self.cookString='�عϿ��ɻ��ˡ�����'
            print('�عϿ��ɻ��ˡ�����')
        elif self.cookLevel>=5:
            self.cookString='�عϿ����ˡ�����'
            print('�عϿ����ˡ�����')
        elif self.cookLevel>=3:
            self.cookString='�عϻ�û�졣����'

            print('�عϻ�û�졣����')
        else:
            print('�������ġ�����')

newDigua=Kaodigua()
newDigua.cook(1)
newDigua.addElements('����')
print(newDigua)


