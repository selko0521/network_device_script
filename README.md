# 网络设备脚本
此库从[乘风龙王的代码库(python)](https://github.com/cflw/cflw_py)拆分而来。**网络设备脚本**只能应用于某一行业，具备极强的专业性，而**代码库**注重于编写任何场景都能使用通用代码，考虑之后决定拆分。

为了确保**网络设备脚本**的良好发展，目前正在重构，不开发新功能，**代码库**原有内容暂时保留。等重构完成，将从**代码库**删除网络设备脚本相关内容。

项目依赖项：
* [乘风龙王的代码库(python)](https://github.com/cflw/cflw_py)

### 文章
* [用python编写控制网络设备的自动化脚本1：框架设计](https://zhuanlan.zhihu.com/p/53641620) \[知乎\]
* [用python编写控制网络设备的自动化脚本2：显示](https://zhuanlan.zhihu.com/p/56108138) \[知乎\]
* [用python编写控制网络设备的自动化脚本3：启动](https://zhuanlan.zhihu.com/p/56833809) \[知乎\]
* [用python编写控制网络设备的自动化脚本4：接口](https://zhuanlan.zhihu.com/p/59428605) \[知乎\]
* [用python编写控制网络设备的自动化脚本5：访问控制列表](https://zhuanlan.zhihu.com/p/63076652) \[知乎\]

## 内容包含

对外公开
* **cflw网络设备**：提供统一的接口、类、结构，对各种网络设备进行控制。
* **cflw网络设备_(品牌)**：控制不同品牌的网络设备
	* 已支持：思科（Cisco）、华为（Huawei）、华三（H3C）、中兴（ZTE）、锐捷（Ruijie）、迈普（Maipu），博达（BDCOM）
	* 对不同品牌不同型号设备的支持程度取决于有没有模拟器或者我能否拿到真机做实验。有时候没法做实验，很多代码写出来没法验证是否可用。

设备层分类，按连接层与网络设备交互方式划分
* **命令行**：仿人工输入命令来控制网络设备
	* 可以使用命令行的连接类（协议）：网络终端（Telnet）、安全外壳（SSH）、串口（Serial）、命名管道（Named-Pipe）
* **网页**（计划中）
* **网络配置协议（NETCONF）**（计划中）
* ~~简单网络管理协议（SNMP）~~（不考虑）

模式层分类，按功能划分