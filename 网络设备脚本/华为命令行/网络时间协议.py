from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
class C服务器(设备.I网络时间协议服务器, 模式.C同级模式):
	def __init__(self, a):
		设备.I网络时间协议服务器.__init__(self, a)
	def f开关(self, a):
		v命令 = 命令.C命令("ntp-server refclock-master")
class C客户端(设备.I网络时间协议客户端, 模式.C同级模式):
	def __init__(self, a):
		设备.I网络时间协议客户端.__init__(self, a)
	def f添加服务器地址(self, a地址):
		v命令 = 命令.C命令("ntp-service unicast-server")
		v命令.f添加(a地址)
		self.f切换到当前模式()
		self.m设备.f执行命令(v命令)
	def f删除服务器地址(self, a地址):
		v命令 = 命令.C命令("undo ntp-service unicast-server")
		v命令.f添加(a地址)
		self.f切换到当前模式()
		self.m设备.f执行命令(v命令)
	def f显示_同步信息(self):
		v命令 = 命令.C命令("display ntp status")
		self.m设备.f执行显示命令(v命令)