# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

from Db.SchoolDbBaseClass import SchoolDbBaseClass
from GUI.ClassDetailInputDialog import ClassDetailInputDialog


###########################################################################
## Class ManageClassDetail
###########################################################################

class ManageClassDetail(wx.Frame):

    def __init__(self, parent):
        self.DBA = SchoolDbBaseClass()
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"课程信息", pos=wx.DefaultPosition, size=wx.Size(600, 280),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        gSizer10 = wx.GridSizer(1, 4, 0, 0)

        gSizer10.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText41 = wx.StaticText(self, wx.ID_ANY, u"记录总数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)

        self.m_staticText41.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer10.Add(self.m_staticText41, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticText_total_count = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                                      0)
        self.m_staticText_total_count.Wrap(-1)

        self.m_staticText_total_count.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer10.Add(self.m_staticText_total_count, 0, wx.ALL, 5)

        gSizer10.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer6.Add(gSizer10, 0, wx.EXPAND, 5)

        gSizer11 = wx.GridSizer(1, 4, 0, 0)

        self.m_grid_manage_class_detail = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(430, 200), 0)

        # Grid
        self.m_grid_manage_class_detail.CreateGrid(8, 5)
        self.m_grid_manage_class_detail.EnableEditing(True)
        self.m_grid_manage_class_detail.EnableGridLines(True)
        self.m_grid_manage_class_detail.EnableDragGridSize(False)
        self.m_grid_manage_class_detail.SetMargins(0, 0)

        # Columns
        self.m_grid_manage_class_detail.SetColSize(0, 52)
        self.m_grid_manage_class_detail.SetColSize(1, 106)
        self.m_grid_manage_class_detail.SetColSize(2, 57)
        self.m_grid_manage_class_detail.SetColSize(3, 110)
        self.m_grid_manage_class_detail.SetColSize(4, 88)
        # self.m_grid_manage_class_detail.SetColSize(5, 80)
        self.m_grid_manage_class_detail.EnableDragColMove(False)
        self.m_grid_manage_class_detail.EnableDragColSize(True)
        self.m_grid_manage_class_detail.SetColLabelSize(30)
        self.m_grid_manage_class_detail.SetColLabelValue(0, u"课程号")
        self.m_grid_manage_class_detail.SetColLabelValue(1, u"课程名")
        self.m_grid_manage_class_detail.SetColLabelValue(2, u"学分数")
        self.m_grid_manage_class_detail.SetColLabelValue(3, u"所在系")
        self.m_grid_manage_class_detail.SetColLabelValue(4, u"任课教师")
        self.m_grid_manage_class_detail.SetColLabelValue(5, wx.EmptyString)
        self.m_grid_manage_class_detail.SetColLabelValue(6, wx.EmptyString)
        self.m_grid_manage_class_detail.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid_manage_class_detail.EnableDragRowSize(True)
        self.m_grid_manage_class_detail.SetRowLabelSize(0)
        self.m_grid_manage_class_detail.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid_manage_class_detail.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        gSizer11.Add(self.m_grid_manage_class_detail, 0, wx.ALL, 5)

        gSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer12 = wx.GridSizer(4, 1, 0, 0)

        self.m_button_insert = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_insert.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gSizer12.Add(self.m_button_insert, 0, wx.ALL, 5)

        self.m_button_update = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_update.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gSizer12.Add(self.m_button_update, 0, wx.ALL, 5)

        self.m_button_delete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_delete.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gSizer12.Add(self.m_button_delete, 0, wx.ALL, 5)

        self.m_button_exit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_exit.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gSizer12.Add(self.m_button_exit, 0, wx.ALL, 5)

        gSizer11.Add(gSizer12, 1, wx.EXPAND, 5)

        bSizer6.Add(gSizer11, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        data = self.DBA.get_selectable_classes(arg=1)
        self.m_staticText_total_count.SetLabel(str(data.__len__()))

        for row in range(self.m_grid_manage_class_detail.GetNumberRows()):
            for col in range(self.m_grid_manage_class_detail.GetNumberCols()):
                try:
                    self.m_grid_manage_class_detail.SetCellValue(
                        row=row, col=col, s=data[row][col]
                    )
                except IndexError as e:
                    pass

        # Connect Events
        self.m_button_insert.Bind(wx.EVT_BUTTON, self.insert_action)
        self.m_button_update.Bind(wx.EVT_BUTTON, self.update_action)
        self.m_button_delete.Bind(wx.EVT_BUTTON, self.delete_action)
        self.m_button_exit.Bind(wx.EVT_BUTTON, self.return_action)

    def __del__(self):
        pass

    def OnRefresh_Data(self):
        data = self.DBA.m_manage_StudentDetail(ac=1)
        self.m_staticText_total_count.SetLabel(str(data.__len__()))

        # 表格大小自适应
        self.m_grid_manage_class_detail.ClearGrid()
        if self.m_grid_manage_class_detail.GetNumberRows() < data.__len__():
            self.m_grid_manage_class_detail.AppendRows(
                data.__len__() - self.m_grid_manage_class_detail.GetNumberRows())
        else:
            self.m_grid_manage_class_detail.DeleteRows(
                numRows=self.m_grid_manage_class_detail.GetNumberRows() - data.__len__())

        # 刷新数据
        for row in range(self.m_grid_manage_class_detail.GetNumberRows()):
            for col in range(self.m_grid_manage_class_detail.GetNumberCols()):
                try:
                    self.m_grid_manage_class_detail.SetCellValue(
                        row=row, col=col, s=data[row][col]
                    )
                except IndexError as e:
                    pass

    # Virtual event handlers, overide them in your derived class
    def insert_action(self, event):
        dlgtext = ClassDetailInputDialog(None)
        if dlgtext.ShowModal() == wx.ID_OK:
            insert_data = dlgtext.GetInputValue()
            if insert_data[0] == " ":
                return False
            else:
                self.DBA.manage_c_insert_data(insert_data)
                self.OnRefresh_Data()

    def update_action(self, event):
        if self.lock_for_grid == False:
            self.lock_for_grid = True
            self.m_button_insert.Disable()
            self.m_button_delete.Disable()
            self.m_button_exit.Disable()
            self.m_button_update.SetLabel("提交")
            self.m_grid_manage_class_detail.EnableEditing(True)
        else:
            # TODO DO UPDATES
            self.m_grid_manage_class_detail.EnableEditing(False)
            self.m_button_update.SetLabel("保存")
            self.m_button_insert.Enable()
            self.m_button_delete.Enable()
            self.m_button_exit.Enable()
            self.lock_for_grid = False
            self.OnRefresh_Data()

    def delete_action(self, event):
        dlgtext = wx.TextEntryDialog(
            self, '请输入删除的课程号号',
            '提示信息', 'C1')
        # dlgtext.SetValue("Python is the best!")
        if dlgtext.ShowModal() == wx.ID_OK:
            SNO = dlgtext.GetValue()
            self.DBA.manage_c_delete_data(SNO)
            # TODO DO DELETE
        dlgtext.Destroy()
        self.OnRefresh_Data()

    def return_action(self, event):
        event.Skip()
