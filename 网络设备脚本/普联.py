import enum
class E型号(enum.IntEnum):
	wdr5620 = 5620
def f创建设备(a连接, a型号, a版本 = 0):
	v类名 = str(a连接.__class__)
	if "selenium" in v类名:
		from .普联网页 import 设备
		return 设备.C设备(a连接, a型号, a版本)
	raise ValueError("不支持的连接")