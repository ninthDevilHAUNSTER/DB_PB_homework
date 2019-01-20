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


###########################################################################
## Class ScoreManageMent
###########################################################################

class ScoreManageMent(wx.Frame):

    def __init__(self, parent):
        self.col2teacher_dict = {}
        self.student2_score_list = [[0, 0]] * 6
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"成绩管理", pos=wx.DefaultPosition, size=wx.Size(600, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        gSizer6 = wx.GridSizer(2, 4, 0, 0)

        self.m_staticText_column_name_static = wx.StaticText(self, wx.ID_ANY, u"课程", wx.DefaultPosition, wx.DefaultSize,
                                                             0)
        self.m_staticText_column_name_static.Wrap(-1)

        self.m_staticText_column_name_static.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer6.Add(self.m_staticText_column_name_static, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticText_column_name_active = wx.StaticText(self, wx.ID_ANY, u"课程名称", wx.DefaultPosition,
                                                             wx.DefaultSize, 0)
        self.m_staticText_column_name_active.Wrap(-1)

        self.m_staticText_column_name_active.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        gSizer6.Add(self.m_staticText_column_name_active, 0, wx.ALL, 5)

        self.m_staticText_class_teacher_static = wx.StaticText(self, wx.ID_ANY, u"任课老师", wx.DefaultPosition,
                                                               wx.DefaultSize, 0)
        self.m_staticText_class_teacher_static.Wrap(-1)

        self.m_staticText_class_teacher_static.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer6.Add(self.m_staticText_class_teacher_static, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_staticText_class_teacher_active = wx.StaticText(self, wx.ID_ANY, u"老师姓名", wx.DefaultPosition,
                                                               wx.DefaultSize, 0)
        self.m_staticText_class_teacher_active.Wrap(-1)

        self.m_staticText_class_teacher_active.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        gSizer6.Add(self.m_staticText_class_teacher_active, 0, wx.ALL, 5)

        gSizer6.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer6, 0, wx.EXPAND, 5)

        gSizer11 = wx.GridSizer(1, 3, 0, 0)

        self.m_staticText50 = wx.StaticText(self, wx.ID_ANY, u"选择课程名称:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)

        self.m_staticText50.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer11.Add(self.m_staticText50, 0, wx.ALL, 5)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"已选修此课程的学生", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        self.m_staticText51.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        gSizer11.Add(self.m_staticText51, 0, wx.ALL, 5)

        gSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer11, 0, wx.EXPAND, 5)

        gSizer12 = wx.GridSizer(1, 3, 0, 0)

        self.m_choice_show_selectable_columnsChoices = [u"                            ", u"UK", u"UK", u"UK", u"UK",
                                                        u"UK",
                                                        u"UK", u"UK", u"UK", u"UK"]
        self.m_choice_show_selectable_columns = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                          self.m_choice_show_selectable_columnsChoices, 0)
        self.m_choice_show_selectable_columns.SetSelection(0)
        gSizer12.Add(self.m_choice_show_selectable_columns, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_grid_select_column_to_student = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_select_column_to_student.CreateGrid(6, 2)
        self.m_grid_select_column_to_student.EnableEditing(True)

        self.m_grid_select_column_to_student.EnableGridLines(True)
        self.m_grid_select_column_to_student.EnableDragGridSize(False)
        self.m_grid_select_column_to_student.SetMargins(0, 0)

        # Columns
        self.m_grid_select_column_to_student.EnableDragColMove(False)
        self.m_grid_select_column_to_student.EnableDragColSize(True)
        self.m_grid_select_column_to_student.SetColLabelSize(30)
        self.m_grid_select_column_to_student.SetColLabelValue(0, u"学号")
        self.m_grid_select_column_to_student.SetColLabelValue(1, u"成绩")
        self.m_grid_select_column_to_student.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid_select_column_to_student.SetRowSize(0, 23)
        self.m_grid_select_column_to_student.SetRowSize(1, 23)
        self.m_grid_select_column_to_student.SetRowSize(2, 23)
        self.m_grid_select_column_to_student.SetRowSize(3, 23)
        self.m_grid_select_column_to_student.SetRowSize(4, 23)
        self.m_grid_select_column_to_student.EnableDragRowSize(True)
        self.m_grid_select_column_to_student.SetRowLabelSize(0)
        self.m_grid_select_column_to_student.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid_select_column_to_student.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        gSizer12.Add(self.m_grid_select_column_to_student, 0, wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_search_for_sth = wx.Button(self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button_search_for_sth, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_input_score = wx.Button(self, wx.ID_ANY, u"输入成绩", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button_input_score, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_score_analyze = wx.Button(self, wx.ID_ANY, u"成绩分布", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button_score_analyze, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_return2index = wx.Button(self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button_return2index, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer12.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_choice_show_selectable_columns.Bind(wx.EVT_CHOICE, self.select_one_class)
        self.m_button_return2index.Bind(wx.EVT_BUTTON, self.ScoreManageMent_to_Index)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def select_one_class(self, event):
        index = event.GetEventObject().GetSelection()
        index2 = str(self.m_choice_show_selectable_columnsChoices[index])
        self.m_staticText_column_name_active.SetLabel(index2)
        self.m_staticText_class_teacher_active.SetLabel(self.col2teacher_dict[index2])
        # event.Skip()

    def ScoreManageMent_to_Index(self, event):
        event.Skip()
