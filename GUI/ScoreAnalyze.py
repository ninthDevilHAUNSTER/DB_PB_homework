# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from numpy import arange, sin, pi
import matplotlib

matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

import numpy as np

import wx
import wx.xrc
from Db.SchoolDbBaseClass import SchoolDbBaseClass


###########################################################################
## Class ScoreAnalyze
###########################################################################

class ScoreAnalyze(wx.Frame):

    def __init__(self, parent):
        self.DBA = SchoolDbBaseClass()
        self.color_list = [
            'darkgreen',
            'navy',
            'brown',
            'purple',
            'red'
            # 'brown'
        ]
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(700, 520), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer9 = wx.GridSizer(3, 1, 0, 0)

        gSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        gSizer9.Add(self.canvas, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        self.SetSizer(gSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

    def draw(self):
        self.axes.clear()
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

    def draw_event(self, event):
        self.axes.clear()
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

    def __del__(self):
        pass
