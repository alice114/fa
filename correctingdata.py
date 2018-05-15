import numpy as np
from pandas import DataFrame,Series
import pandas as pd

#load txt
arr=np.loadtxt('HSFAVOUCHERS20180420.txt',encoding='gbk',dtype=np.str,delimiter = ',')

#convert to dataframe
original_data = DataFrame(arr)

#generate corect data and output
correct_data = original_data[~((original_data[24].str.contains(r'.*?股票估值增值.*'))&(original_data[17]=='0'))]
np.savetxt('correctdata.txt',correct_data,fmt='%s', delimiter = ',',encoding='gbk')

#generate wrong data and output
wrong_data = original_data[(original_data[24].str.contains(r'.*?股票估值增值.*'))&(original_data[17]=='0')]
np.savetxt('wrongdata.txt',wrong_data,fmt='%s', delimiter = ',',encoding='gbk')

#correctingdata and output
correctingdatatmp = wrong_data.copy()

correctingdatatmp.iloc[:,17] = correctingdatatmp.iloc[:,16]
correctingdatatmp.iloc[:,16] = pd.to_numeric(correctingdatatmp.iloc[:,16])+ pd.to_numeric('0.01')
# print(correctingdatatmp.iloc[:,16])

# correctingdatatmp.iloc[:,16] = correctingdatatmp.iloc[:,16].astype(str)
correctingdatatmp.iloc[:,16] = correctingdatatmp.iloc[:,16].to_string(float_format='%.2f',index = False).split('\n')
# correctingdatatmp.iloc[:,16] = pd.Series.to_string(correctingdatatmp.iloc[:,16])
# print(correctingdatatmp.iloc[:,16])

# a = pd.Series.to_string(correctingdatatmp.iloc[:,16], index = False, header = False)
# print(a)
# b = a.split('\n')
# print(b)

# myformat = lambda x: '%.2f'%x
# correctingdatatmp.iloc[:,16] = correctingdatatmp.iloc[:,16].to_string(float_format=myformat)
# correctingdatatmp.iloc[:,16] = correctingdatatmp.iloc[:,16].to_string(float_format='%.2f')
# print(correctingdatatmp.iloc[:,16])

correctingdatatmp2 = wrong_data.copy()
correctingdatatmp2.iloc[:,[16,17]] = "0.01"
correctingdata2 = correctingdatatmp2.copy()
# correctingdata2.iloc[:,11]= correctingdatatmp2.iloc[:,11].replace(['40','50'],['50','40'])
correctingdata2.iloc[:,11]= correctingdatatmp2.iloc[:,11].replace('40','50_tmp').replace('50','40').replace('50_tmp','50')
correctingdata = correctingdatatmp.append(correctingdata2)
np.savetxt('correctingdata.txt',correctingdata,fmt='%s', delimiter = ',',encoding='gbk')