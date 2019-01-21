# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from GUI.MessageDialog import MessageDialog_CANCEL


###########################################################################
## Class StudentDetailInputDialog
###########################################################################

class StudentDetailInputDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"请输入新的学生信息", pos=wx.DefaultPosition,
                           size=wx.Size(500, 250), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        gSizer19 = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText47 = wx.StaticText(self, wx.ID_ANY, u"学号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)

        gSizer19.Add(self.m_staticText47, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_SNO = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_SNO, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText48 = wx.StaticText(self, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)

        gSizer19.Add(self.m_staticText48, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_SNAME = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_SNAME, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText49 = wx.StaticText(self, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)

        gSizer19.Add(self.m_staticText49, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl_SEX = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_SEX, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText50 = wx.StaticText(self, wx.ID_ANY, u"年龄", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)

        gSizer19.Add(self.m_staticText50, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl_AGE = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_AGE, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"所在系", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        gSizer19.Add(self.m_staticText51, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_SDEPT = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_SDEPT, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText52 = wx.StaticText(self, wx.ID_ANY, u"登录名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)

        gSizer19.Add(self.m_staticText52, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_LOGN = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_LOGN, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText54 = wx.StaticText(self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)

        gSizer19.Add(self.m_staticText54, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_PSWD = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_PSWD, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer19.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button29 = wx.Button(self, wx.ID_OK, u"提交更新数据", wx.Point(-1, -1), wx.Size(100, -1), 0)
        gSizer19.Add(self.m_button29, 0, wx.ALL, 5)

        bSizer9.Add(gSizer19, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

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

    def __del__(self):
        pass
