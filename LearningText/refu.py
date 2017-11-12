import collections
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}
old = set(old_dict.keys())
new=set(new_dict.keys())
update_set=old.intersection(new)
delete_set=old.symmetric_difference(update_set)
add_set=new.symmetric_difference(update_set)
print(old)
print(new)
print(update_set)
print(delete_set)
print(add_set)
c = collections.Counter('abcdeabcdabcaba')
print (c)
res=c.most_common(4)
print(res)
for k,v in c.items():
    print(k,v)
for item in c.elements():
    print (item)

dic=collections.OrderedDict()

#dic = {'k1':'vi','k3':'v3','k2':'v2'}
dic['k1']='v1'
dic['k3']='v3'
dic['k2']='v4'
print(dic)






