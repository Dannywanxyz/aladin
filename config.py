# coding=utf-8


# 数据库配置

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': "",
    'db': 'cmdb'
}

page_config = {
    "brand_name": 'Aladin-CMDB',
    'title': 'Aladin',
    # "favicon":'https://pic1.zhimg.com/6d660dd4156c64bfad13ff97d79c2f98_l.jpg',
    "menu": [
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'user',
            "title": '用户管理',
            "data": [{
                "name": 'username',
                "title": '用户名'
            }, {
                "name": 'password',
                "title": '密码'
            }]
        },
        {
            "name": 'hardware',
            "title": '设备',
            "data": [{
                "name": "name",
                "title": '设备名'
            }]
        },
        {
            "name": "asset",
            "title": "固定资产登记表",
            "data": [{
                "name": "asset",
                "title": '设备名称',
                "type": 'select',
                "select_type": 'hardware'
            }, {
                'name': 'asset_no',
                'title': '设备编号'
            }, {
                "name": 'asset_type',
                "title": '设备型号',
                "type": 'select',
                "value": {0: '型号1', 1: '型号2'}
            }, {
                "name": 'amount',
                "title": '数量',
            }, {
                "name": 'purchase_time',
                "title": "采购日期",
                "type": 'date'
            }, {
                "name": 'purchase_department',
                "title": '采购单位',
                "type": 'select',
                "value": {0: '部门1', 1: '部门2',}
            }, {
                "name": 'configuration',
                "title": '配置',
            }, {
                "name": 'putintouse_time',
                "title": '投入使用时间',
                "type": 'date'
            }, {
                "name": 'applying_department',
                "title": '使用部门',
                "type": 'select',
                "value": {0: '部门1', 1: '部门2'}
            }, {
                "name": 'applying_employee',
                "title": '使用人'
            }, {
                "name": 'ups',
                "title": '是否开启',
                "type": 'select',
                "value": {0: '开启', 1: '关闭'}
            }]
        }
    ]
}





# ,{
#         "name": 'host',
#         "title": '服务器',
#         "data": [{
#             "name": 'cabinet',
#             "title": '机柜'
#         },{
#             "name":'hostname',
#             "title":'主机名'
#         }]
#     },{
#         "title": '业务',
#         "sub":[
#             {
#                 'name': 'product',
#                 'title': '业务线',
#                 'data': [{
#                     'name': 'service_name',
#                     'title': '服务名'
#                 },{
#                     'name':'module_letter',
#                     'title':'模块简称'
#                 },{
#                     'name':'dev_interface',
#                     'title':'开发者'
#                 },{
#                     'name':'op_interface',
#                     'title':'运维接口人'
#                 }]
#             },
#             {
#                 'name': 'raidtype',
#                 'title': 'Raid厂商',
#                 'data': [{
#                     'name': 'name',
#                     'title': 'Raid厂商'
#                 }]
#             }


#         ]
#     }
