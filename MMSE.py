from qureys import qureyMuti
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
import warnings
warnings.filterwarnings("ignore")

#1、查询语句
MMSE_All = """select a.patient_report_id,sum(a.score) AS moca_score,b.patient_age,c.sex
from t_ht_patient_score a,t_ht_patient_report b,t_ht_patient c
where a.patient_report_id=b.id
and a.patient_id=c.id
and a.is_del=0
and a.question_parent_code in
(select code from t_ht_report where parent_code='MMSE' and is_del=0)
group by a.patient_report_id,c.sex;"""

#2、查询结果
#region
MMSE_All_ = pd.DataFrame(qureyMuti(MMSE_All))
#print(MMSE_All_)
male0_10=[]
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
male11_20=[]
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
male21_30=[]
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
male21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==0)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
# female
female0_10=[]
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female0_10.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=0)&(MMSE_All_.iloc[:,1]<=10)].shape[0])
female11_20=[]
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female11_20.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=11)&(MMSE_All_.iloc[:,1]<=20)].shape[0])
female21_30=[]
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=18)&(MMSE_All_.iloc[:,2]>=0)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=44)&(MMSE_All_.iloc[:,2]>=19)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=59)&(MMSE_All_.iloc[:,2]>=45)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=74)&(MMSE_All_.iloc[:,2]>=60)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]<=89)&(MMSE_All_.iloc[:,2]>=75)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
female21_30.append(MMSE_All_[(MMSE_All_.iloc[:,3]==1)&(MMSE_All_.iloc[:,2]>=90)&(MMSE_All_.iloc[:,1]>=21)&(MMSE_All_.iloc[:,1]<=30)].shape[0])
#endregion

#3、画图
#region总分
Dis_MMSE=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(['0-18', '19-44', '45-59', '60-74', '75-89', '90以上', ])
    .add_yaxis("男0~10",male0_10,stack='stack1')
    .add_yaxis("男11~20",male11_20,stack='stack1')
    .add_yaxis("男21~30",male21_30,stack='stack1')
    .add_yaxis("女0~10",female0_10,stack='stack2')
    .add_yaxis("女11~20",female11_20,stack='stack2')
    .add_yaxis("女21~30",female21_30,stack='stack2')
    #系列设置
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #全局设置
    .set_global_opts(title_opts=opts.TitleOpts(title="量表总分统计",pos_left="center",
                                               title_textstyle_opts=opts.TextStyleOpts(color="blue")),
                     #xy轴名称
                     xaxis_opts=opts.AxisOpts(name="年龄"),
                     yaxis_opts=opts.AxisOpts(name="人数",
                                              #参考线
                                              splitline_opts=opts.SplitLineOpts(is_show=True)),
                     legend_opts=opts.LegendOpts(pos_top="7%",)
                     )
    .render("Dis_MMSE.html")
)
#endregion