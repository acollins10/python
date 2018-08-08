import numpy as np

import pandas as pd

labels = ['a', 'b', 'c']

my_list = [10, 20, 30]
my_arr = np.array([10, 20, 30])
d = {'a':10, 'b':20, 'c':30}

pd.Series(data=my_list)
Out[10]: 
0    10
1    20
2    30
dtype: int64

pd.Series(my_list, labels)
Out[11]: 
a    10
b    20
c    30
dtype: int64

pd.Series(my_arr)
Out[15]: 
0    10
1    20
2    30
dtype: int32

pd.Series(my_arr, labels)
Out[16]: 
a    10
b    20
c    30
dtype: int32

pd.Series(d)
Out[17]: 
a    10
b    20
c    30
dtype: int64

pd.Series(data=labels)
Out[18]: 
0    a
1    b
2    c
dtype: object

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])

ser1
Out[20]: 
USA        1
Germany    2
USSR       3
Japan      4
dtype: int64

ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])

ser2
Out[22]: 
USA        1
Germany    2
Italy      5
Japan      4
dtype: int64

ser1['USA']
Out[23]: 1

ser1 + ser2
Out[24]: 
Germany    4.0
Italy      NaN
Japan      8.0
USA        2.0
USSR       NaN
dtype: float64

ser2['Italy']
Out[25]: 5
