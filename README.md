[python-自动化-游戏脚本思路_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1EW4y1k7Cc/?spm_id_from=333.999.0.0&vd_source=3e2d4e4db5253dfa63e698c242348e20)

## 问题一

-   [python pycharm 无法import win32api、win32con、win32com、win32gui 问题一次解决！方法合集 - 简书](https://www.jianshu.com/p/e15082f67318) 

最近写项目发现python pycharm 导入 win32api、win32con、win32com、win32gui 等win32相关的包都会出现或多或少问题，Google一大堆不靠谱的方法试了个遍。
  特此记录一下解决办法
## 判断你的python版本

-   出现以上相关报错一般是 python 版本过高或者 python 版本与库不兼容导致。
-   同时自2017年底以来，win32gui 似乎被称为/已经成为 pywin32
-   所以一般 python 版本大于 3.6 后就会出现类似报错
-   解决办法
-   降低您的python 版本或者寻找与版本兼容的库版本（麻烦，下下策）
-   尝试安装 #pywin32 库 `pip install pywin32`

## pywin32 补充说明

> pywin32 它直接接包装了几乎所有的 Windows API ,可以方便地从 Python 直接调用
因此它也理所应当的包括 win32api、win32con、win32com、win32gui 等win32相关的 Windows API，直接安装pywin32即可，安转完重新导入索引即可解决问题

## 其他情况
-   pypiwin32
- 如果你安装的pywin32版本高于223，那就要同时安装 #Pypiwin32,才能确保所有模块能正常工作
`pip install pypiwin32` `


## 问题二

运行错误提示未安装 #opencv 解决办法

-   [(Python使用pyautogui.locateOnScreen(‘xx.png‘, confidence=0.9) 语句时提示未安装opencv解决办法n](https://blog.csdn.net/mcw_720624/article/details/116700717)

-   在Python中安装并import导入 [pyautogui](https://so.csdn.net/so/search?q=pyautogui&spm=1001.2101.3001.7020)
-   模块后，可以很方便来控制鼠标和键盘实现自动化操作，再不也不用什么按健精灵之类的小儿科东东了。
-  pyautogui有一个 #locateOnScreen(） 方法，可以在屏幕上查找图片，如果找到则返回左上角和右下角的坐标位置。默认情况下，查找精确度为1.0，即百分之百精准匹配——这其实很不方便，实际我们把精确度设为0.9更科学，既能保证不会找错对象，又不会因为默认的精确度太苛刻，明明对象存在代码却找不到而返回None。这时我们需要增加一个参数 confidence=0.9，例子如下：
```python
pyautogui.locateOnScreen('xx.png', confidence=0.9)
```
   
-   这是因为没有安装opencv包，解决办法如下（以Pycharm为例）：
![[Pasted image 20221029114047.png]]
-   安装好后，就可以正常使用confidence参数了。


## 问题三
选中目标后无法鼠标右键攻击目标
解决办法:先把右键攻击改为[按键](https://blog.csdn.net/weixin_45668674/article/details/107738485)1攻击
```python
def hit(self, path, confi, hit_time):  
    p1 = pyautogui.locateCenterOnScreen(path, confidence=confi)  
    sleep(1)  
    pyautogui.click(p1.x, p1.y)  
    print("找到假人了,等待攻击")  
    sleep(1)  
    #pyautogui.mouseDown(buttom='right')  
    #pyautogui.mouseUp(buttom='right')    pyautogui.press('1')  
    sleep(hit_time)
```