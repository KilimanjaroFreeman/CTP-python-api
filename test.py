# -*- encoding: utf-8
"""
Created on 2019/03/15
@author: Freeman
python封装CTP的接口，本项目主要由VNPY的ctp接口更改而成，
提供给大家交流和学习,这里是行情和交易api的使用示例

"""

import sys
from time import sleep
import datetime
from PyQt4 import QtGui
from ctp_api import CtpGateway

brokerID = "9999"                                 #经纪商代码
mdAddress = 'tcp://180.168.146.187:10011'         #行情服务器地址
tdAddress = "tcp://180.168.146.187:10001"         #交易服务器地址
userID = "124538"                                 #期货账号
password = "123456abc"                            #密码
#初始化与连接
api = CtpGateway(userID, password, brokerID, tdAddress, mdAddress)
api.connect()

symbol = 'rb1905'
price = 3753
volume = 1

#-------------------------------------------------------
"""每秒钟会返回2个tick数据，返回数据时会调用onTick函数，这里接收到数据后马上打印合约号"""
# 行情打印
# 创建Qt应用对象，用于事件循环
app = QtGui.QApplication(sys.argv)
# 订阅合约，测试通过
api.subscribe(symbol)
# 连续运行，用于输出行情
app.exec_()

#-------------------------------------------------------
# 开多
api.buy(symbol, price, volume)
# 开空
api.short(symbol, price, volume)
# 平多
api.sell(symbol, price, volume)
# 平空
api.cover(symbol, price, volume)
# 撤销所有未成交的订单
api.cancelAllOrder()
# 查询账户持仓情况
api.qryPosition()
# 查询账户资金
api.qryAccount()
