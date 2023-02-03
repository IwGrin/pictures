
from subMMSE import subMMSE
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
#0、sql语句
DDDXL = """
select a.patient_report_id,sum(a.score) AS DDDXL_score,b.patient_age,c.sex
from t_ht_patient_score a,t_ht_patient_report b,t_ht_patient c
where a.patient_report_id=b.id
and a.patient_id=c.id
and a.is_del=0
and a.question_parent_code='DDDXL'
group by a.patient_report_id,c.sex;
"""

#1、查询结果
male_DDDXL = subMMSE(DDDXL,0)
female_DDDXL = subMMSE(DDDXL,1)

#2、绘图
age_values = ['0~18', '19~44', '45~59', '60~74', '75~89', '90以上']
DIS_DDDXL=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([i for i in range(male_DDDXL.shape[0])])
    .add_yaxis(age_values[0],list(male_DDDXL.iloc[:,0]),stack='male')
    .add_yaxis(age_values[1],list(male_DDDXL.iloc[:,1]),stack='male')
    .add_yaxis(age_values[2],list(male_DDDXL.iloc[:,2]),stack='male')
    .add_yaxis(age_values[3],list(male_DDDXL.iloc[:,3]),stack='male')
    .add_yaxis(age_values[4],list(male_DDDXL.iloc[:,4]),stack='male')
    .add_yaxis(age_values[5],list(male_DDDXL.iloc[:,5]),stack='male')
    .add_yaxis(age_values[0],list(-female_DDDXL.iloc[:,0]),stack='female')
    .add_yaxis(age_values[1],list(-female_DDDXL.iloc[:,1]),stack='female')
    .add_yaxis(age_values[2],list(-female_DDDXL.iloc[:,2]),stack='female')
    .add_yaxis(age_values[3],list(-female_DDDXL.iloc[:,3]),stack='female')
    .add_yaxis(age_values[4],list(-female_DDDXL.iloc[:,4]),stack='female')
    .add_yaxis(age_values[5],list(-female_DDDXL.iloc[:,5]),stack='female')
    .reversal_axis()
    #系列设置
    .set_series_opts(
        #设置label
        label_opts=opts.LabelOpts(is_show=False),
        #设置提示框！！！
        tooltip_opts=opts.TooltipOpts(is_show=False)
                     )
    #全局设置
    .set_global_opts(
                     title_opts=opts.TitleOpts(title="得分",pos_left="20%",pos_top="10%",
                                               title_textstyle_opts=opts.TextStyleOpts()),
                     #xy轴
                     xaxis_opts=opts.AxisOpts(name="人数",
                                              #is_inverse=True,
                                              #设置此函数，使得坐标轴仍为正数！！！
                                              axislabel_opts=opts.LabelOpts(formatter=JsCode("""
                                              function(value){
                                              if(value<0){
                                                return -value;
                                                }else{
                                                return value;
                                                }
                                              }  
                                              """)),
                                              ),

                     yaxis_opts=opts.AxisOpts(name="<——女男——>"),
                     #legend_opts=opts.LegendOpts(pos_top="7%",)
                     )
    .render("DIS_MMSE_DDDXL.html")
)
#endregion