# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       excelUtil
   Description:
   Author:     bowen
   date:        1/24/19
-------------------------------------------------
"""

def excel_table_byname(file= 'file.xls', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #??
    colnames =  table.row_values(colnameindex) #?????
    list =[]
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

