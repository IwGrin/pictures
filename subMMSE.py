import pandas as pd
import numpy as np
from qureys import qureyMuti

def subMMSE(sql, sex):
    """
    该函数意在查找MMSE的各子项目结果值
    :param sql: MMSE各子项目的select语句
    :param sex: sex=0：男；sex=1：女
    :return:
    """
    sqlRes = pd.DataFrame(qureyMuti(sql)) #自定义的sql查询函数--querys.py
    sqlRes.columns = ["id", "score", "age", "sex"]
    age_condition = [(sqlRes['age'] <= 18),
                     (sqlRes['age'] >= 19) & (sqlRes['age'] <= 44),
                     (sqlRes['age'] >= 45) & (sqlRes['age'] <= 59),
                     (sqlRes['age'] >= 60) & (sqlRes['age'] <= 74),
                     (sqlRes['age'] >= 75) & (sqlRes['age'] <= 89),
                     (sqlRes['age'] >= 90)]
    age_values = ['0~18', '19~44', '45~59', '60~74', '75~89', '90以上']
    sqlRes['age_range'] = np.select(age_condition, age_values) #在sql查询结果的dataframe中添加一列，根据age
    res = pd.DataFrame(np.zeros([len(set(sqlRes['score'])), len(age_values)]))#保存最终的返回值结果，是一个数据框，大小为子项目的score的类型个数x年龄范围
    res.columns = age_values
    for i in range(len(set(sqlRes['score']))):
        for j in range(len(age_values)):
            res.iloc[i, j] = \
            sqlRes[(sqlRes["sex"] == sex) & (sqlRes['score'] == i) & (sqlRes['age_range'] == age_values[j])].count()[0]#根据条件赋值
    return res
