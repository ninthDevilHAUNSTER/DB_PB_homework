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
## Class Index
###########################################################################

class Index(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"功能选择界面", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        gSizer13 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText52 = wx.StaticText(self, wx.ID_ANY, u"    Hello !   ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)

        self.m_staticText52.SetFont(
            wx.Font(22, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Segoe Script"))

        gSizer13.Add(self.m_staticText52, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticText_index_username = wx.StaticText(self, wx.ID_ANY, u"请先登陆", wx.DefaultPosition, wx.DefaultSize,
                                                         0)
        self.m_staticText_index_username.Wrap(-1)

        self.m_staticText_index_username.SetFont(
            wx.Font(15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体"))

        gSizer13.Add(self.m_staticText_index_username, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer14.Add(gSizer13, 0, wx.EXPAND, 5)

        gSizer14 = wx.GridSizer(2, 2, 0, 0)

        self.m_button_Index2StudentLogin = wx.Button(self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.Size(120, 45), 0)
        self.m_button_Index2StudentLogin.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer14.Add(self.m_button_Index2StudentLogin, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button_Index2StudentChooseClass = wx.Button(self, wx.ID_ANY, u"学生选课", wx.DefaultPosition,
                                                           wx.Size(120, 45), 0)
        self.m_button_Index2StudentChooseClass.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer14.Add(self.m_button_Index2StudentChooseClass, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button_Index2StudentScoreList = wx.Button(self, wx.ID_ANY, u"学生成绩单", wx.DefaultPosition,
                                                         wx.Size(120, 45), 0)
        self.m_button_Index2StudentScoreList.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer14.Add(self.m_button_Index2StudentScoreList, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_Index2ScoreManageMent = wx.Button(self, wx.ID_ANY, u"成绩管理", wx.DefaultPosition, wx.Size(120, 45),
                                                        0)
        self.m_button_Index2ScoreManageMent.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer14.Add(self.m_button_Index2ScoreManageMent, 0, wx.ALL, 5)

        bSizer14.Add(gSizer14, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer14)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_Index2StudentLogin.Bind(wx.EVT_BUTTON, self.Index_to_StudentLogin)
        self.m_button_Index2StudentChooseClass.Bind(wx.EVT_BUTTON, self.Index_to_StudentChooseClass)
        self.m_button_Index2StudentScoreList.Bind(wx.EVT_BUTTON, self.Index_to_StudentScoreList)
        self.m_button_Index2ScoreManageMent.Bind(wx.EVT_BUTTON, self.Index_to_ScoreManageMent)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Index_to_StudentLogin(self, event):
        event.Skip()

    def Index_to_StudentChooseClass(self, event):
        event.Skip()

    def Index_to_StudentScoreList(self, event):
        event.Skip()

    def Index_to_ScoreManageMent(self, event):
        event.Skip()


# >class Frame1(wx.Frame):
# >   ....
# >   def UpdateLabel( self, value ):
# >       self.staticText1.SetLabel( value )
#
# >def Rpccallfunction(value):
# >  wx.CallAfter( frame.UpdateLabel, str(value) )
