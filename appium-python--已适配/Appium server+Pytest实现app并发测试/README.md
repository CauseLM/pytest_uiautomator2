## 一、文件目录结构

```
allure0					allure结果存放目录
allure0_report			allure报告存放目录
Common		
	base				存放 基础功能文件
	drivers				获取app driver
Config					存放 根目录文件绝对地址
Locators				存放 设备和app定位相关信息
Output					存放 日志、截图
PageObject				存放 app页面操作函数
TestCases				存放 测试用例
TestDatas				存放 测试数据
```

## 二、环境搭建

#### 1、安装 nodejs

下载地址：https://nodejs.org/en/download/

#### 2、安装 Appium 

终端安装appium server --三种安装方式
**直接在终端输入命令：**

npm install -g appium  
**通过国内镜像安装：**

npm install -g appium -registry http://registry.cnpmjs.org
**通过 cnpm 安装：**

npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install -g Appium

另一种方法：安装appium-desktop

下载地址：https://github.com/appium/appium-desktop/releases

#### 3、安装 Appium-doctor

npm install -g appium-doctor

#### 4、安装 Android SDK

下载地址：https://android-sdk.en.softonic.com/?ex=MOB-593.7

#### 5、安装 JAVA JDK

下载地址：http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

## 三、配置环境变量

### 1、在系统环境变量添加 ANDROID_HOME

##### 			变量名：ANDROID_HOME		值：D:\android-sdk

##### 			其中D:\android-sdk  为android-sdk的安装路径

![image-20220430103459220](D:\自动化测试框架\Appium server+Pytest实现app并发测试\z-md-img\image-20220430103459220.png)

### 2、在系统环境变量添加 JAVA_HOME

##### 			变量名： JAVA_HOME		值： C:\Program Files\Java\jdk1.8.0_191

##### 			其中 C:\Program Files\Java\jdk1.8.0_191 为java-jdk的安装路径

![image-20220430103819589](D:\自动化测试框架\Appium server+Pytest实现app并发测试\z-md-img\image-20220430103819589.png)

### 3、在path中添加以下四条

```cmd
	D:\android-sdk\tools				uiautomatorviewer.bat 工具可以用来查看 app
										的元素信息					
​	D:\android-sdk\platform-tools		adb.exe   此工具用来连接手机
​	D:\android-sdk\build-tools\25.0.0	aapt.exe  可以获取 app 的包名和启
										动名
​	%JAVA_HOME%							使得系统可以在任何路径下识别java命令
```

![image-20220430104704963](D:\自动化测试框架\Appium server+Pytest实现app并发测试\z-md-img\image-20220430104704963.png)

## 四、项目目的

该项目主要适用于可以连接多台设备的 APP 自动化测试。

该项目可以使用2中appium连接手机设备方式：

**一通过appium server连接：**通过该方式需要使用drivers中的 app_driver_auto_server.py 获取app驱动，该方法自动启动appium server，前提是在run_case.py中配置好appium server相关信息，然后通过该文件运行项目。

**二是通过appium gui 连接：**通过该方式需要使用drivers中的 app_driver.py 获取app驱动，该方法需要手动启动appium gui，然后通过run_case.py运行项目。



