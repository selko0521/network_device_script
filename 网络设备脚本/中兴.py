import enum
import cflw代码库py.cflw网络连接 as 连接
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	zxr10_m6000 = 46000
def f创建设备(a连接, a型号, a版本 = 0):
	if a连接.c连接特性 & 连接.E连接特性.e命令行:
		from .中兴命令行 import 设备
		return 设备.C设备(a连接, a型号, a版本)
	else:
		raise ValueError("参数错误")