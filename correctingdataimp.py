import numpy as np
from pandas import DataFrame,Series
import pandas as pd

from correctingdata import original_data

ORITXT = 'HSFAVOUCHERS20180420.txt'

def load(orignaltxt):
    arr = np.loadtxt(orignaltxt, encoding='gbk', dtype=np.str, delimiter=',')
    original_data = DataFrame(arr)
    return original_data

def save(data_df,newtxt):
    np.savetxt(newtxt,data_df,fmt='%s', delimiter = ',',encoding='gbk')

def wrongdata():
    data_df = original_data
    wrongdata = data_df(data_df[24].str.contains(r'.*?股票估值增值.*')) & (data_df[17] == '0')
    return wrongdata

def correctdata():
    data_df = original_data
    correctdata = data_df[~(data_df[24].str.contains(r'.*?股票估值增值.*')) & (data_df[17] == '0')]
    return correctdata

def correctingdata():
    # correctingdata and output
    correctingdatatmp = wrongdata.copy()

    correctingdatatmp.iloc[:, 17] = correctingdatatmp.iloc[:, 16]
    correctingdatatmp.iloc[:, 16] = pd.to_numeric(correctingdatatmp.iloc[:, 16]) + pd.to_numeric('0.01')
    print(correctingdatatmp.iloc[:, 16])

    # correctingdatatmp.iloc[:,16] = correctingdatatmp.iloc[:,16].astype(str)
    correctingdatatmp.iloc[:, 16] = pd.Series.to_string(correctingdatatmp.iloc[:, 16])
    print(correctingdatatmp.iloc[:, 16])

    correctingdatatmp2 = wrongdata.copy()
    correctingdatatmp2.iloc[:, [16, 17]] = "0.01"
    correctingdata2 = correctingdatatmp2.copy()
    # correctingdata2.iloc[:,11]= correctingdatatmp2.iloc[:,11].replace(['40','50'],['50','40'])
    correctingdata2.iloc[:, 11] = correctingdatatmp2.iloc[:, 11].replace('40', '50_tmp').replace('50', '40').replace(
        '50_tmp', '50')
    correctingdata = correctingdatatmp.append(correctingdata2)


if __name__ == '__main__':
    # load txt
    load(ORITXT)

    #generate corect data and output
    correctdata()
    save(correctdata,'correctdata.txt')
    wrongdata()
    save(wrongdata,'wrongdata.txt')
    correctingdata()
    save(correctingdata,'correctingdata.txt')

