# 数据库原理1 期末大作业

## 连接 SQL Server方法

### SQL Server 设置外部链接

参考了网上的方法，过程如下

1.设置SQLSERVER混合模式(SQL Server 身份验证和Windows 身份验证)

2.启用SQL服务TCP/IP，启用协议与IP地址

3.启用SQL服务SQLSERVER Browser /Sql Server(实例名)

4.CMD命令输入：netstat -a   如果找到有“0.0.0.0:1433”，就说明SqlServer在监听了

5.防火墙应用通过window防火墙进行通信，添加应用
```sql
C:\Program Files\Microsoft SQLServer\MSSQL10.MSSQLSERVER\MSSQL\Binn\sqlservr.exe
```
6.防火墙-高级设置，添加入站规则1433端口

### 利用Python链接SQL Server

使用python连接的方法很简单。利用`pymssql`库就可以轻松连接，方法如下

```python
self.conn = pymssql.connect(MSSQL_HOST, MSSQL_USER,
                                MSSQL_PASSWORD, MSSQL_DATABASE)
```
其中包括了一些超参数，比如地址，用户，密码和DB名字，我的设置如下（我的数据库在虚拟机里，所以是192.168的IP地址)
```python
MSSQL_HOST = "192.168.25.134"
MSSQL_USER = "shaobao"
MSSQL_PASSWORD = "toor"
MSSQL_DATABASE = "newdb"
```

## 学生选课成绩管理系统开发过程说明

### 项目分类和应用

面对这样一个问题，我们最主要的任务是分清楚我们需要哪些界面。其实详细划分一下的话，也不是很困难。

我主要用的是WXpython来建立的GUI程序。根据题目要求，我需要很多的子窗口以及一个主窗口，我命名这些窗口分别如下所示。父子类别用\t来分隔开

```python
Index.py
        主界面
MessageDialog.py
        辅助提示框
StudentLogin.py
        登陆界面
StudentChooseClass.py
        学生选课界面
StudentScoreList.py
        学生成绩界面
ScoreManageMent.py
        管理界面
    ScoreAnalyze.py
            成绩分析界面
    ManageClassDetail.py
            课程管理界面
        ClassDetailInputDialog.py
                添加课程界面
    ManageStudentDetail.py
            学生管理界面
        StudentDetailInputDialog.py
                添加学生信息界面
```

此外，我们将在最外层的Mian_frame中绑定这些页面并添加事件。大致的代码如下所示
```python
    def OnInit(self):
        # Init All frames
        self.Index = Index(parent=None)
        self.ScoreManageMent = ScoreManageMent(parent=None)
        self.ScoreManageMent.col2teacher_dict = self.DBA.get_c()
        self.ScoreManageMent.m_choice_show_selectable_columnsChoices \
            = list(self.ScoreManageMent.col2teacher_dict.keys())
        self.ScoreManageMent.m_choice_show_selectable_columns.SetItems(
            self.ScoreManageMent.m_choice_show_selectable_columnsChoices
        )
        self.StudentChooseClass = StudentChooseClass(parent=None)
        self.StudentLogin = StudentLogin(parent=None)
        self.StudentScoreList = StudentScoreList(parent=None)
        self.ScoreAnalyze = ScoreAnalyze(parent=None)
        self.ManageClassDetail = ManageClassDetail(parent=None)
        self.ManageStudentDetail = ManageStudentDetail(parent=None)
        # Init Router
        self.__bind_router()
        self.__bind_event()
        # Show Index
        self.Index.Show(show=True)
        return True
```

### 绑定路由与添加事件

#### 问题描述：需要保持当前打开的窗体为一个

#### 问题分析：添加路由函数

很显然，原生的WXpython并没有路由方法，甚至Wxpython对于单界面的GUI有着更好的支持。要保持当前打开的窗体为一个，需要定义一些函数，比如某个窗体关闭，某个窗体会打开。对此，我们需要自定义一些事件。我参照了网络后端架构的后端的路由函数。将一些事件固定得绑定到这个函数，就可以实现这样子的功能。具体的方法如下所示

```python
    def OnRouter_change(self, event, value='Index'):
        self.__current_active_frame = value
        if self.__current_active_frame == "Index":
            self.Index.Show()
            self.StudentLogin.Hide()
            self.StudentChooseClass.Hide()
            self.StudentScoreList.Hide()
            self.ScoreManageMent.Hide()
            self.SetTopWindow(self.Index)

        elif self.__current_active_frame == "StudentLogin":
            self.Index.Hide()
            self.StudentLogin.Show()
            self.StudentChooseClass.Hide()
            self.StudentScoreList.Hide()
            self.ScoreManageMent.Hide()
            self.SetTopWindow(self.StudentLogin)
        ...
```

很显然，我将会判断传入OnRouter_change事件的传入值。通过传入值来判断，让哪些页面Hide。让哪一个页面Show。

#### 遇上的难题：如何给wxpython传值
然而，在wxpython的原声实现中，并不支持给事件传值。因为事件绑定的是一个函数名而传参。形如这样的形式
```python
        self.StudentChooseClass.drop_class_button.Bind(wx.EVT_BUTTON,self.OnDropSelectedClass_StudentChooseClass)
```
#### 问题解决：lambda方法
最后，我在wxpython advancer 文档中查阅到，如果需要给事件传递参数，需要用到lambda方法，并且附上默认得event参数。
解决方案如下
```python
self.Bind(wx.EVT_BUTTON,
          lambda event: self.OnRouter_change(event, 'StudentLogin'),
          self.Index.m_button_Index2StudentLogin)
```

### 问题3 学生成绩分析页面

#### 问题描述：如何将直方图嵌入到wxpython中

#### 问题分析：利用 matplotlib

在这个页面中。我们需要将每门课的成绩输出一个平均分，做成一个纵向的直方图。我想到我能够利用`matplotlib`库的作图工具来完成这个操作。生成一个平均分的纵向直方图诚然不难。原生的代码如下

```python
        label_list, data_list = self.DBA.get_avg_s_group_by_class()
        width = 0.4
        ind = np.linspace(1.5, 7.5, data_list.__len__())
        for i in range(data_list.__len__()):
            self.axes.barh(ind[i] - width / 2, data_list[i],
                           width,
                           color=self.color_list[i % self.color_list.__len__()],
                           label=data_list[i])
        self.axes.set_yticks(ind)
        self.axes.set_yticklabels(label_list)
        self.axes.set_ylabel('课程名称')
        self.axes.set_xlabel('平均成绩')
        self.axes.set_title('成绩分布')
        self.axes.legend()
```

#### 遇上的难题1：如何把图片放到GUI界面？
然而，图片是图片，GUI是GUI。如果把图片保存到本地，用GUI再次读取，也是个不错的方法，但是这样一点也不geek。应该如何把连个结合起来呢？

#### 问题解决1： 利用WXAgg后端
实际上，matplotlib已经为我们想到了方法，其实matplotlib可以用一个后端，叫做WXAgg。该后端完美支持了全平台的wxGUI框架。python自然也不例外。只需要在包引入上动些脑经就可以了
```python
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class ScoreAnalyze(wx.Frame):

    def __init__(self, parent):
        ...
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
```

这样，axes就会调用我们生成图像的句柄，将图像返回到GUI界面中并打应出来。

#### 遇上的难题2：中文乱码
实际上，在matplotlib中对于非西文字体的支持非常差，动不动就乱码。实际上这也是在matplotlib库利用中非常头大的问题。用英文自然也可以，但是这样就无法达到老师的要求了。

#### 问题解决2：确认plt的字体文件

比较简单的方法，是定义plt的字体。将字体设置为SimHei来让中文不乱码。需要每次引用的时候都写一遍，虽然绝非一劳永逸，但是也能缓解这样的问题。
```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
```
还有直接修改源文件的方法，再次不多赘述。

最终图片就能顺利打印出来了
![TIM图片20190307220350.png-38.4kB][1]

### 数据管理页面

#### 问题描述：如何通过表格更改实现DML语句

DML语句，包括了增删改查。查自然是没什么问题。重要的就是增删改，毕竟wxpython不是PB。前端的修改必须通过SQL语句返回后端去，如何实现这些方法呢？
![TIM图片20190307220611.png-75.3kB][2]

#### 问题分析：分开处理

行吧，毕竟我们没有PB这么好用的数据窗口，那就多加几个键分开处理。因此，我增加了新增，保存，删除和退出键。把增删改给分开来

#### 遇上的难题1 ：删除键

删除键，就是点了删除该咋办呢？如何生成SQL语句呢？

#### 问题解决1 ：通过弹出框输入主键删除

讲道理，应该是需要做一个弹出框，让用户输入主键后删除，并且设置为NOT NULL的主键，不应该允许用户在插入的时候将其清空。对此，我们需要用到之前弹出框文件中自定义的一种弹出框。

对此我新建立了一个临时的弹出框，让用户输入主键，随后返回给DB类，让它生成delete语句

```python
    def delete_action(self, event):
        dlgtext = wx.TextEntryDialog(
            self, '请输入删除的课程号号',
            '提示信息', 'C1')
        # dlgtext.SetValue("Python is the best!")
        if dlgtext.ShowModal() == wx.ID_OK:
            SNO = dlgtext.GetValue()
            self.DBA.manage_c_delete_data(SNO)
        dlgtext.Destroy()
        self.OnRefresh_Data()

    def manage_c_delete_data(self, CNO):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("DELETE FROM C WHERE  CNO = '{}'".format(CNO))
```
这样就能做到删除了

#### 遇上的难题2：新增键
新增也是一个头大的东西，如果让用户在前端的表格中输入东西并返回语句的话，做一些数据的检查很困难。
#### 问题解决2

对此，我需要自定义一个弹出框，让用户来输入东西。
就像这个样子
![TIM截图20190307221703.png-18.8kB][3]

由于窗体代码非常复杂，所以不贴了。具体会在后文的github下载链接中查看。

点击提交后，会出发这样一个函数，主要就是检查主键是否为空。`MessageDialog_CANCEL`是我们编写的一个通用提示框类。
```python
    def GetInputValue(self):
        if self.m_textCtrl_SNO.GetValue() == "":
            MessageDialog_CANCEL("SNO 不可为空", "错误信息")
        return [
            self.m_textCtrl_SNO.GetValue(),
            self.m_textCtrl_SNAME.GetValue(),
            self.m_textCtrl_SEX.GetValue(),
            self.m_textCtrl_AGE.GetValue(),
            self.m_textCtrl_SDEPT.GetValue(),
            str(__import__("random").randint(80, 760)),
            self.m_textCtrl_LOGN.GetValue(),
            self.m_textCtrl_PSWD.GetValue()
        ]
```
在审核通过后，会通过一个句柄传递给DBA的数据库控制类。生成INSERT 语句并执行。
```python
    def insert_action(self, event):
        dlgtext = StudentDetailInputDialog(None)
        if dlgtext.ShowModal() == wx.ID_OK:
            insert_data = dlgtext.GetInputValue()
            if insert_data[0] == " ":
                return False
            else:
                self.DBA.manage_s_insert_data(insert_data)
                self.OnRefresh_Data()
```

#### 遇上的难题3：改键
修改数据可能是最为困难的了。需要判断哪些列被修改，并返回SQL语句

#### 问题解决3

这个和之前在修改成绩的时候的方法很类似，修改成绩也是这么实现的。

- 首先，用户点击修改后，会锁住返回的按钮。
- 之后，会保存原表中的列到一个临时变量
- 用户点击保存按钮，将当前的新表和原表传递给numpy.argwhere()函数，该函数会判断哪列被修改了，返回一个元组列表，该列表的每一项是被修改列下标组成的元组(x,y)
- 解除锁定
```python
    def update_action(self, event):
        if self.lock_for_grid == False:
            self.lock_for_grid = True
            self.m_button_insert.Disable()
            self.m_button_delete.Disable()
            self.m_button_exit.Disable()
            self.m_button_update.SetLabel("提交")
            self.m_grid_manage_student_detail.EnableEditing(True)
            self.renew_raw_list_value()
        else:
            self.DBA.manage_s_update_data(numpy.argwhere(changed_list!=raw_list),self.column_value)
            self.m_grid_manage_student_detail.EnableEditing(False)
            self.m_button_update.SetLabel("保存")
            self.m_button_insert.Enable()
            self.m_button_delete.Enable()
            self.m_button_exit.Enable()
            self.lock_for_grid = False
            self.OnRefresh_Data()
```

## 程序运行部分结果截屏

![此处输入图片的描述][4]

## 代码地址

https://github.com/ninthDevilHAUNSTER/DB_PB_homework

## 认识;体会;建议;意见

这次PB实验，实际上我是用的WXPYTHON做的。我学会了如何用可视化工具来编写自己的GUI窗口，而不是之前那样子直接开局一个记事本，代码全靠敲。尽管用GUI界面建立了窗口，但是还是要写很多的事件绑定代码。其中，我写了主窗体以及路由函数，小组里余下三位同学写了登陆，选课和成绩分布。我写了管理界面，并整合了他们的代码。将小组的代码绑定路由并修改了一番。

获益还是很多的，比如说我们组加起来的总代码量超过了**<big>2229</big>**行。
```python
github.com/AlDanial/cloc v 1.80  T=0.50 s (74.0 files/s, 11786.0 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          28            771            377           2229
```

再比如说我们一共写了**10**个主窗体...嗯没错，GUI都是我画的。

最后，我觉得这个实验还是很有趣的，毕竟全程用python写就很有挑战性。实际上在`改`这个功能上，我本来想用`sqlmap`的页面相似度算法，但是发现自己需要判断非常多的东西。最终还是放弃了异或运算。转向了numpy的怀抱，发现这个东西非常好用。





  [1]: http://static.zybuluo.com/shaobaobaoer/ew327q330w61rtu9fc4y61ap/TIM%E5%9B%BE%E7%89%8720190307220350.png
  [2]: http://static.zybuluo.com/shaobaobaoer/566sy59w8oysy7m26s2esci1/TIM%E5%9B%BE%E7%89%8720190307220611.png
  [3]: http://static.zybuluo.com/shaobaobaoer/3pnebf15htqdh7a2bbgn26ok/TIM%E6%88%AA%E5%9B%BE20190307221703.png
  [4]: https://raw.githubusercontent.com/ninthDevilHAUNSTER/DB_PB_homework/master/demo/V%200.1%E6%95%88%E6%9E%9C%E5%9B%BE.gif
