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
## Class ClassDetailInputDialog
###########################################################################

class ClassDetailInputDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"请输入新的课程信息", pos=wx.DefaultPosition,
                           size=wx.Size(500, 250), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        gSizer19 = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText47 = wx.StaticText(self, wx.ID_ANY, u"课程号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)

        gSizer19.Add(self.m_staticText47, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_CNO = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_CNO, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText48 = wx.StaticText(self, wx.ID_ANY, u"课程名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)

        gSizer19.Add(self.m_staticText48, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_CNAME = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_CNAME, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText49 = wx.StaticText(self, wx.ID_ANY, u"学分数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)

        gSizer19.Add(self.m_staticText49, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl_CREDIT = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_CREDIT, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText50 = wx.StaticText(self, wx.ID_ANY, u"所在系", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)

        gSizer19.Add(self.m_staticText50, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl_CDEPT = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_CDEPT, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"任课老师", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        gSizer19.Add(self.m_staticText51, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_TNAME = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer19.Add(self.m_textCtrl_TNAME, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer19.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button29 = wx.Button(self, wx.ID_OK, u"提交", wx.Point(-1, -1), wx.Size(100, -1), 0)
        gSizer19.Add(self.m_button29, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer9.Add(gSizer19, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


    def GetInputValue(self):
        if self.m_textCtrl_CNO.GetValue() == "":
            MessageDialog_CANCEL("CNO 不可为空", "错误信息")
        return [
            self.m_textCtrl_CNO.GetValue(),
            self.m_textCtrl_CNAME.GetValue(),
            self.m_textCtrl_CREDIT.GetValue(),
            self.m_textCtrl_CDEPT.GetValue(),
            self.m_textCtrl_TNAME.GetValue(),
        ]
