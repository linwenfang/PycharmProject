import numpy as np
TP=int(input('TP='))
FP=int(input('FP='))
TN=int(input('TN='))
FN=int(input('FN='))
Gmeas=np.sqrt((TP/(TP+FP))*(TN/(TN+FN)))
print(Gmeas)