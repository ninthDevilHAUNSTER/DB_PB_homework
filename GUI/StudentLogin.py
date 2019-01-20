# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class StudentLogin
###########################################################################

class StudentLogin(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"系统登陆", pos=wx.DefaultPosition, size=wx.Size(375, 250),
                           style=wx.DEFAULT_DIALOG_STYLE, name=u"数据库登陆")

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1.SetMinSize(wx.Size(1, 2))
        self.spacer_do_not_delete = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.ST_ELLIPSIZE_MIDDLE)
        self.spacer_do_not_delete.Wrap(-1)

        bSizer1.Add(self.spacer_do_not_delete, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer4 = wx.GridSizer(0, 2, 1, 40)

        self.m_staticText_account = wx.StaticText(self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_account.Wrap(-1)

        self.m_staticText_account.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        gSizer4.Add(self.m_staticText_account, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_textCtrl_account = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl_account, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_password = wx.StaticText(self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_password.Wrap(-1)

        self.m_staticText_password.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        gSizer4.Add(self.m_staticText_password, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_textCtrl_password = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl_password, 0, wx.ALL, 5)

        self.m_button_login = wx.Button(self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.DefaultSize, 0)

        self.m_button_login.SetDefault()
        gSizer4.Add(self.m_button_login, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_button_return2index = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)

        self.m_button_return2index.SetDefault()
        gSizer4.Add(self.m_button_return2index, 0, wx.ALL, 5)

        bSizer1.Add(gSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_login.Bind(wx.EVT_BUTTON, self.LoginDialog_login_click)
        self.m_button_return2index.Bind(wx.EVT_BUTTON, self.StudentLogin_to_Index)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def LoginDialog_login_click(self, event):
        event.Skip()

    def StudentLogin_to_Index(self, event):
        event.Skip()
