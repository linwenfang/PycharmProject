import os
def hanshu(path):
    pathdir=os.listdir(path)
    for name in pathdir:
        if os.path.isfile(path+"\\"+name):
            if name[:3]=='del':
                os.remove(path+'\\'+name)

        else:
            path1=path+'\\'+name
            hanshu(path1)
if __name__ == '__main__':
    path="E:\Papers_dataset\ResempledDataSet\CCA_maj_arff"
    hanshu(path)
