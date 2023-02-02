from qureys import qureyMuti,qureyOne
from pyecharts.charts import Pie,Line,Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
#region1、查询语句
# 累计人数
sqlAcc = 'select count(id) from t_ht_patient_report where complete_status=1;'
# 本月人数
sqlMon = 'select count(id) from t_ht_patient_report where month(now())=month(update_time) and year(now())=year(update_time);'
# 今日人数
sqlToday = 'select count(id) from t_ht_patient_report where date(now())=date(update_time);'
# 实时人数
sqlByDay = 'select count(id),date(create_time) from t_ht_patient_report where is_del=0 group by date(create_time) order by date(create_time);'
# 性别分布
sqlSex = 'select count(re.id)  "性别分布" from t_ht_patient_report re inner join t_ht_patient pa on re.patient_idcard=pa.idcard and complete_status=1 group by sex;'
# 年龄分布
sqlAge0_18 = 'select count(id) "0-18岁" from t_ht_patient_report where patient_age between 0 and 18 and complete_status=1;'
sqlAge19_44 ='select count(id) "19-44" from t_ht_patient_report where patient_age between 19 and 44 and complete_status=1;'
sqlAge45_59 ='select count(id) "45-59" from t_ht_patient_report where patient_age between 45 and 59 and complete_status=1;'
sqlAge60_74 ='select count(id) "60-75" from t_ht_patient_report where patient_age between 60 and 74 and complete_status=1;'
sqlAge75_89 ='select count(id) "74-89" from t_ht_patient_report where patient_age between 75 and 89 and complete_status=1;'
sqlAge90_ ='select count(id) "90-"from t_ht_patient_report where patient_age >90 and complete_status=1;'
# 评测结果总体分布
sqlDigRes = "select clinical_diagnosis,count(clinical_diagnosis) from t_ht_patient_report where is_del=0 and complete_status=1 and clinical_diagnosis!='' group by clinical_diagnosis order by count(clinical_diagnosis) desc;"
#endregion

#region2、查询结果
# 总人数
accNum = qureyOne(sqlAcc)
print("总人数：",accNum)
# 本月人数
monNum = qureyOne(sqlMon)
print("本月人数：",monNum)
# 今日人数
todayNum = qureyOne(sqlToday)
print("今日人数：",todayNum)
# 实时人数
daysNum = qureyMuti(sqlByDay)
print('实时人数：',daysNum)
# 性别分布
sexDis = qureyMuti(sqlSex)
print("性别分布：",sexDis)
# 年龄分布
numAge0_18 = qureyOne(sqlAge0_18)
numAge19_44 = qureyOne(sqlAge19_44)
numAge45_59 = qureyOne(sqlAge45_59)
numAge60_74 = qureyOne(sqlAge60_74)
numAge75_89 = qureyOne(sqlAge75_89)
numAge90_ = qureyOne(sqlAge90_)
print('年龄分布：',numAge0_18,numAge19_44,numAge45_59,numAge60_74,numAge75_89,numAge90_)
# 评测结果总体分布
digResNum = qureyMuti(sqlDigRes)
print('评测结果总体分布：',digResNum)
#endregion

#3、绘图
# region实时人数
daysDis = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([i[1] for i in daysNum])
    .add_yaxis(
        series_name="诊断人数",
        y_axis=[i[0] for i in daysNum],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=1,
        is_smooth=True,
    )
    .set_global_opts(
        #标题
        title_opts=opts.TitleOpts(title="测评人数实时统计",pos_top='20',pos_left='80',
                                  title_textstyle_opts=opts.TextStyleOpts(color='#467897',
                                                                          )),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        legend_opts=opts.LegendOpts(is_show=False),
        #y轴
        yaxis_opts=opts.AxisOpts(
            type_="value",
            splitline_opts=opts.SplitLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=True)
        ),
        #x轴
        xaxis_opts=opts.AxisOpts(type_="category",boundary_gap=False),
        datazoom_opts=opts.DataZoomOpts(is_show=True,
                                        is_realtime=True,#是否实时更新，False则拖动完成后更新
                                        orient='horizontal',#横向展示拖动
                                        is_zoom_lock=False,#True:只能平移，不能缩放
                                        range_start=95,
                                        range_end=100
                                        )
    )
    .set_colors(['#467897'])
    .render("daysDis.html")
)

# endregion

# region性别、年龄分布
sexDisPic = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add(
        '性别',
        [list(z) for z in zip(['男','女'],[sexDis[0][0],sexDis[1][0]])],
        center=['25%','50%'],
        radius=["30%","75%"],
        rosetype='area',
    )
    .add(
        "年龄",
        [list(z) for z in zip(['0~18','19~44','45~59','60~74','75~89','90以上'],[numAge0_18,numAge19_44,numAge45_59,numAge60_74,numAge75_89,numAge90_])],
        center=['75%','50%'],
        radius='55%',
        rosetype='radius'
    )
    # 全局配置项
    .set_global_opts(
        #设置标题
        title_opts=opts.TitleOpts(title='性别、年龄分布',  #标题内容
                                  pos_right='center',    #左右位置
                                  pos_top="20",          #上下位置
                                  #标题文字设置
                                  title_textstyle_opts=opts.TextStyleOpts(color='#002FA7')
                                  ),
        #设置图列
        legend_opts=opts.LegendOpts(is_show=False))
    # 系列配置项
    .set_series_opts(
        #设置提示框
        tooltip_opts=opts.TooltipOpts(
            trigger='item',formatter='{a} <br/> {b}: {d}% <br/> 人数: {c}'
        ),
        #标签配置项
        label_opts=opts.LabelOpts(is_show=True,font_size=10),
        #视觉引导线设置
        labelLine = {'show':True,#是否展示
                     'length':1, #长度
                     #引导线样式
                     #'lineStyle':{'opacity','width','type','clolr'...详见csdn}
                     }
    )
    .set_colors(['#C99E8C','#465E65','#467897','#E7CD79','#DCD2C6','#800020'])
    .render("sexDis.html")
)
#endregion

# region评测结果总体分布
digResDis = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK,width='1000'))
    .add_xaxis([i[0] for i in digResNum[:50]])
    .add_yaxis("",[i[1] for i in digResNum[:50]])
    .set_global_opts(
        #设置标题
        title_opts=opts.TitleOpts(title="评测结果总体分布",pos_left='center',pos_top='20',
                                  title_textstyle_opts=opts.TextStyleOpts(color='#DCD2C6')),
        #设置x轴旋转，解决显示问题
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=62)),
        # 设置提示框
        tooltip_opts=opts.TooltipOpts(
            trigger='axis',# item数据项图形触发，主要在散点图，饼图等无类目轴的图标使用；axis坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表使用
            #formatter='{b} <br/>人数： {c}',  # '{a} <br/> {b}: {d}% <br/> 人数: {c}'
            trigger_on='mousemove|click',
            axis_pointer_type='shadow' #类型
        ),
        #设置展示
        datazoom_opts=opts.DataZoomOpts(type_='inside',range_start=0,range_end=100)#内部展示缩放
        #datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')] 既有内部缩放也有平移器：slider+inside!)
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_colors('#467897')
    .render("digResDis.html")
)

#endregion