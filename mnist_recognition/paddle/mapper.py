import numpy as np


##���ݷ�����ʸ���Ԥ������0-9
def map_number(pre_array):
    pred = np.argsort(pre_array)[-1]
    return pred