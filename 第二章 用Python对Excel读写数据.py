# 2.4 读取工作簿、工作表信息
# import xlrd     #导入模块
# import xlrd as xl     #导入模块并取简称
# form xlrd import open_workbook     #直接导入库中的包
# wb=xlrd.open_workbook('办公楼外墙成本核算 210728 - 山墙改石材.xls')    #读取工作簿
# wsobj=wb.sheets()   #读取工作簿下所有工作表对象
# wsname=wb.sheet_names() #读取工作簿下所有工作表名称
# ws1=wb.sheet_by_name('成本分析')    #按指定名称读取工作表对象
# ws2=wb.sheet_by_index(1)    #按指定序号读取工作表对象
# ws3=wb.sheets()[1]      #按指定序号读取工作表对象
# print(wsobj)
# print(wsname)
# print(ws1)
# print(ws2)
# print(ws3)

# 2.5 读取Excel行、列、单元格信息
# import xlrd
# ws=xlrd.open_workbook('办公楼外墙成本核算 210728 - 山墙改石材.xls').sheet_by_name('成本分析') #获取工作表对象
# crow=ws.nrows #获取行号
# ccol=ws.ncols #获取列号
# row_data=ws.row_values(0) #获取指定行数据
# col_data=ws.col_values(0) #获取指定列数据
# cell_data_1=ws.cell(0,0)    #获取指定单元格数据
# cell_data_1=ws.cell(0,0)    #获取指定单元格数据(显示数据类型）
# cell_data_2=ws.cell_value(0,0)    #获取指定单元格数据(自动换行）
# cell_data_3=ws.cell(0,0).value    #获取指定单元格数据(另一种写法）
# print(crow)
# print(ccol)
# print(row_data)
# print(col_data)
# print(cell_data_1)
# print(cell_data_2)
# print(cell_data_3)

# 2.7 创建工作簿、工作表和写入单元格
# import xlwt     #引入模块
# nwb=xlwt.Workbook(encoding='uft-8')     #新建工作簿（指定编码）
# nws=nwb.add_sheet('表名')     #添加工作表
# nws.write(1,2,'%.2f'%10.123456)      #写入单元格(左右对齐无效）
# nws.write(0,1,'敬然')
# nws.write(2,3,'敬然'*3)
# nwb.save('簿名.xls')      #保存工作簿
# print('完成')

# 2.9 修改工作簿、工作表、单元格
# import xlrd #导入xlrd模块
# from xlutils.copy import copy   #导入xlutils中的复制模块
# wb=xlrd.open_workbook('簿名.xls')   #读取工作簿
# nwb=copy(wb)                       #复制工作簿
# nws1=nwb.add_sheet('表名1')         #新建工作表（重名工作表会出错）
# nws2=nwb.get_sheet(0)              #读取工作表（按指定序号）
# nws3=nwb.get_sheet('表名')          #读取工作表（按指定名称）
# nws1.write(2,3,'孙')               #写入数据（行,列,'值')
# nws3.write(2,3,'小然然')
# nwb.save('簿名.xls')               #同名覆盖，异名另存
