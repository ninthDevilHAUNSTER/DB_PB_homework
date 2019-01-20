# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan  9 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

current_user_id = 1000
current_user_name = 1001


###########################################################################
## Class StudentChooseClass
###########################################################################

class StudentChooseClass(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"学生选课", pos=wx.DefaultPosition, size=wx.Size(800, 635),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu_exent_menu = wx.Menu()
        self.m_menuItem_current_user_sno = wx.MenuItem(self.m_menu_exent_menu, current_user_id, u"MyMenuItem",
                                                       wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_exent_menu.Append(self.m_menuItem_current_user_sno)

        self.m_menuItem_current_user_sname = wx.MenuItem(self.m_menu_exent_menu, current_user_name, u"MyMenuItem",
                                                         wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_exent_menu.Append(self.m_menuItem_current_user_sname)

        self.m_menu_exent_menu.AppendSeparator()

        self.m_menuItem_StudentChooseClass_to_StudentLogin = wx.MenuItem(self.m_menu_exent_menu, wx.ID_ANY, u"切换用户",
                                                                         wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_exent_menu.Append(self.m_menuItem_StudentChooseClass_to_StudentLogin)

        self.m_menuItem_StudentChooseClass_to_Index = wx.MenuItem(self.m_menu_exent_menu, wx.ID_ANY, u"返回",
                                                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_exent_menu.Append(self.m_menuItem_StudentChooseClass_to_Index)

        self.m_menubar2.Append(self.m_menu_exent_menu, u"当前用户")

        self.SetMenuBar(self.m_menubar2)

        self.student_detail_text = wx.StaticText(self, wx.ID_ANY, u"\n学生详细信息", wx.DefaultPosition, wx.DefaultSize, 0)
        self.student_detail_text.Wrap(-1)

        self.student_detail_text.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.student_detail_text.SetBackgroundColour(wx.Colour(224, 224, 224))

        self.m_mgr.AddPane(self.student_detail_text,
                           wx.aui.AuiPaneInfo().Top().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Dock().Resizable().FloatingSize(wx.Size(80, 68)).Row(0).Layer(99))

        self.selectable_class_text = wx.StaticText(self, wx.ID_ANY, u"\n可选课程", wx.DefaultPosition, wx.DefaultSize, 0)
        self.selectable_class_text.Wrap(-1)

        self.selectable_class_text.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.selectable_class_text.SetBackgroundColour(wx.Colour(224, 224, 224))

        self.m_mgr.AddPane(self.selectable_class_text,
                           wx.aui.AuiPaneInfo().Top().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Dock().Resizable().FloatingSize(wx.Size(80, 68)).Row(0).Position(0).Layer(99))

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"\n       请输入课程号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.m_staticText7.SetBackgroundColour(wx.Colour(224, 224, 224))

        self.m_mgr.AddPane(self.m_staticText7,
                           wx.aui.AuiPaneInfo().Top().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Dock().Resizable().FloatingSize(wx.Size(80, 68)).Row(0).Layer(100))

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_CENTER)
        self.m_textCtrl5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.m_textCtrl5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        self.m_mgr.AddPane(self.m_textCtrl5, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(125, 71)).BottomDockable(False).TopDockable(
            False).RightDockable(False).Layer(100))

        self.class_number_refresh_button = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self.class_number_refresh_button, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(100, 47)).Layer(100))

        self.student_detail_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.student_detail_grid.CreateGrid(1, 5)
        self.student_detail_grid.EnableEditing(True)
        self.student_detail_grid.EnableGridLines(True)
        self.student_detail_grid.EnableDragGridSize(False)
        self.student_detail_grid.SetMargins(0, 0)

        # Columns
        self.student_detail_grid.EnableDragColMove(False)
        self.student_detail_grid.EnableDragColSize(True)
        self.student_detail_grid.SetColLabelSize(30)
        self.student_detail_grid.SetColLabelValue(0, u"学生")
        self.student_detail_grid.SetColLabelValue(1, u"姓名")
        self.student_detail_grid.SetColLabelValue(2, u"年龄")
        self.student_detail_grid.SetColLabelValue(3, u"性别")
        self.student_detail_grid.SetColLabelValue(4, u"所在院系")
        self.student_detail_grid.SetColLabelValue(5, u"学费")
        self.student_detail_grid.SetColLabelValue(6, wx.EmptyString)
        self.student_detail_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.student_detail_grid.EnableDragRowSize(True)
        self.student_detail_grid.SetRowLabelSize(0)
        self.student_detail_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance
        self.student_detail_grid.SetLabelFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体"))

        # Cell Defaults
        self.student_detail_grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        self.student_detail_grid.SetFont(
            wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体"))

        self.m_mgr.AddPane(self.student_detail_grid, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(79, 58)).BestSize(wx.Size(-1, 300)).MinSize(
            wx.Size(-1, 200)).MaxSize(wx.Size(-1, 400)).Layer(98))

        self.selectable_class_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.selectable_class_grid.CreateGrid(5, 5)
        self.selectable_class_grid.EnableEditing(True)
        self.selectable_class_grid.EnableGridLines(True)
        self.selectable_class_grid.EnableDragGridSize(False)
        self.selectable_class_grid.SetMargins(0, 0)

        # Columns
        self.selectable_class_grid.SetColSize(0, 67)
        self.selectable_class_grid.SetColSize(1, 97)
        self.selectable_class_grid.SetColSize(2, 59)
        self.selectable_class_grid.SetColSize(3, 80)
        self.selectable_class_grid.SetColSize(4, 80)
        self.selectable_class_grid.EnableDragColMove(False)
        self.selectable_class_grid.EnableDragColSize(True)
        self.selectable_class_grid.SetColLabelSize(30)
        self.selectable_class_grid.SetColLabelValue(0, u"课程号")
        self.selectable_class_grid.SetColLabelValue(1, u"课程名")
        self.selectable_class_grid.SetColLabelValue(2, u"学分")
        self.selectable_class_grid.SetColLabelValue(3, u"所在院系")
        self.selectable_class_grid.SetColLabelValue(4, u"任课老师")
        self.selectable_class_grid.SetColLabelValue(5, wx.EmptyString)
        self.selectable_class_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.selectable_class_grid.EnableDragRowSize(True)
        self.selectable_class_grid.SetRowLabelSize(0)
        self.selectable_class_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance
        self.selectable_class_grid.SetLabelFont(
            wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体"))

        # Cell Defaults
        self.selectable_class_grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        self.selectable_class_grid.SetFont(
            wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体"))

        self.m_mgr.AddPane(self.selectable_class_grid, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(79, 58)).BestSize(wx.Size(-1, 300)).MinSize(
            wx.Size(-1, 200)).MaxSize(wx.Size(-1, 400)).Layer(98))

        self.passed_class_text = wx.StaticText(self, wx.ID_ANY, u"\n已修课程成绩", wx.DefaultPosition, wx.DefaultSize, 0)
        self.passed_class_text.Wrap(-1)

        self.passed_class_text.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.passed_class_text.SetBackgroundColour(wx.Colour(224, 224, 224))

        self.m_mgr.AddPane(self.passed_class_text,
                           wx.aui.AuiPaneInfo().Top().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Dock().Resizable().FloatingSize(wx.Size(80, 68)).Row(0).Position(0).Layer(91))

        self.selected_class_text = wx.StaticText(self, wx.ID_ANY, u"\n已选课程", wx.DefaultPosition, wx.DefaultSize, 0)
        self.selected_class_text.Wrap(-1)

        self.selected_class_text.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.selected_class_text.SetBackgroundColour(wx.Colour(224, 224, 224))

        self.m_mgr.AddPane(self.selected_class_text,
                           wx.aui.AuiPaneInfo().Top().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Dock().Resizable().FloatingSize(wx.Size(80, 68)).Row(0).Layer(91))

        self.passed_class_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.passed_class_grid.CreateGrid(5, 5)
        self.passed_class_grid.EnableEditing(True)
        self.passed_class_grid.EnableGridLines(True)
        self.passed_class_grid.EnableDragGridSize(False)
        self.passed_class_grid.SetMargins(0, 0)

        # Columns
        self.passed_class_grid.EnableDragColMove(False)
        self.passed_class_grid.EnableDragColSize(True)
        self.passed_class_grid.SetColLabelSize(30)
        self.passed_class_grid.SetColLabelValue(0, u"课程号")
        self.passed_class_grid.SetColLabelValue(1, u"课程名称")
        self.passed_class_grid.SetColLabelValue(2, u"平时成绩")
        self.passed_class_grid.SetColLabelValue(3, u"考试成绩")
        self.passed_class_grid.SetColLabelValue(4, u"总评成绩")
        self.passed_class_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.passed_class_grid.EnableDragRowSize(True)
        self.passed_class_grid.SetRowLabelSize(0)
        self.passed_class_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.passed_class_grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        self.m_mgr.AddPane(self.passed_class_grid, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(79, 58)).Row(2).BestSize(wx.Size(-1, 300)).MinSize(
            wx.Size(-1, 200)).MaxSize(wx.Size(-1, 400)).Layer(90))

        self.selected_class_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.selected_class_grid.CreateGrid(5, 5)
        self.selected_class_grid.EnableEditing(True)
        self.selected_class_grid.EnableGridLines(True)
        self.selected_class_grid.EnableDragGridSize(False)
        self.selected_class_grid.SetMargins(0, 0)

        # Columns
        self.selected_class_grid.EnableDragColMove(False)
        self.selected_class_grid.EnableDragColSize(True)
        self.selected_class_grid.SetColLabelSize(30)
        self.selected_class_grid.SetColLabelValue(0, u"课程号")
        self.selected_class_grid.SetColLabelValue(1, u"课程名")
        self.selected_class_grid.SetColLabelValue(2, u"学分")
        self.selected_class_grid.SetColLabelValue(3, u"所在院系")
        self.selected_class_grid.SetColLabelValue(4, u"任课老师")
        self.selected_class_grid.SetColLabelValue(5, wx.EmptyString)
        self.selected_class_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.selected_class_grid.EnableDragRowSize(True)
        self.selected_class_grid.SetRowLabelSize(0)
        self.selected_class_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.selected_class_grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_TOP)
        self.m_mgr.AddPane(self.selected_class_grid, wx.aui.AuiPaneInfo().Top().CaptionVisible(False).PinButton(
            True).Dock().Resizable().FloatingSize(wx.Size(79, 58)).Row(2).Layer(90))

        self.update_class_button = wx.Button(self, wx.ID_ANY, u"选课", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self.update_class_button,
                           wx.aui.AuiPaneInfo().Bottom().CaptionVisible(False).CloseButton(False).PinButton(
                               True).Dock().Resizable().FloatingSize(wx.Size(131, 82)).BottomDockable(
                               False).TopDockable(False).LeftDockable(False).RightDockable(False).Floatable(
                               False).Layer(80))

        self.drop_class_button = wx.Button(self, wx.ID_ANY, u"退课", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self.drop_class_button,
                           wx.aui.AuiPaneInfo().Bottom().CaptionVisible(False).CloseButton(False).PinButton(
                               True).Dock().Resizable().FloatingSize(wx.Size(131, 82)).BottomDockable(
                               False).TopDockable(False).LeftDockable(False).RightDockable(False).Floatable(
                               False).Layer(80))

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.StudentChooseClass_to_StudentLogin,
                  id=self.m_menuItem_StudentChooseClass_to_StudentLogin.GetId())
        self.Bind(wx.EVT_MENU, self.StudentChooseClass_to_Index, id=self.m_menuItem_StudentChooseClass_to_Index.GetId())

    def __del__(self):
        self.m_mgr.UnInit()

    # Virtual event handlers, overide them in your derived class
    def StudentChooseClass_to_StudentLogin(self, event):
        event.Skip()

    def StudentChooseClass_to_Index(self, event):
        event.Skip()
