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
## Class StudentScoreList
###########################################################################

class StudentScoreList ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"学生成绩单", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )

		fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer4 = wx.GridSizer( 1, 4, 0, 0 )

		self.m_staticText_student_id = wx.StaticText( self, wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_student_id.Wrap( -1 )

		self.m_staticText_student_id.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

		gSizer4.Add( self.m_staticText_student_id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText_student_name = wx.StaticText( self, wx.ID_ANY, u"<姓名>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_student_name.Wrap( -1 )

		self.m_staticText_student_name.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

		gSizer4.Add( self.m_staticText_student_name, 0, wx.ALL, 5 )

		self.m_staticText_student_score_list = wx.StaticText( self, wx.ID_ANY, u"学生成绩单", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_student_score_list.Wrap( -1 )

		self.m_staticText_student_score_list.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

		gSizer4.Add( self.m_staticText_student_score_list, 0, wx.ALL, 5 )

		self.m_staticText_current_time = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_current_time.Wrap( -1 )

		self.m_staticText_current_time.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		gSizer4.Add( self.m_staticText_current_time, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		fgSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

		self.m_grid_student_score_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid_student_score_grid.CreateGrid( 5, 5 )
		self.m_grid_student_score_grid.EnableEditing( False )
		self.m_grid_student_score_grid.EnableGridLines( False )
		self.m_grid_student_score_grid.EnableDragGridSize( False )
		self.m_grid_student_score_grid.SetMargins( 0, 0 )

		# Columns
		self.m_grid_student_score_grid.SetColSize( 0, 66 )
		self.m_grid_student_score_grid.SetColSize( 1, 137 )
		self.m_grid_student_score_grid.SetColSize( 2, 80 )
		self.m_grid_student_score_grid.SetColSize( 3, 80 )
		self.m_grid_student_score_grid.SetColSize( 4, 80 )
		self.m_grid_student_score_grid.EnableDragColMove( False )
		self.m_grid_student_score_grid.EnableDragColSize( True )
		self.m_grid_student_score_grid.SetColLabelSize( 30 )
		self.m_grid_student_score_grid.SetColLabelValue( 0, u"课程号" )
		self.m_grid_student_score_grid.SetColLabelValue( 1, u"课程名" )
		self.m_grid_student_score_grid.SetColLabelValue( 2, u"成绩" )
		self.m_grid_student_score_grid.SetColLabelValue( 3, u"学分" )
		self.m_grid_student_score_grid.SetColLabelValue( 4, u"教师" )
		self.m_grid_student_score_grid.SetColLabelValue( 5, u"课程名" )
		self.m_grid_student_score_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_student_score_grid.EnableDragRowSize( True )
		self.m_grid_student_score_grid.SetRowLabelSize( 0 )
		self.m_grid_student_score_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid_student_score_grid.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		# Cell Defaults
		self.m_grid_student_score_grid.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		fgSizer1.Add( self.m_grid_student_score_grid, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 1, 3, 10, 10 )

		self.m_staticText_average_score_static = wx.StaticText( self, wx.ID_ANY, u"平均成绩", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_average_score_static.Wrap( -1 )

		self.m_staticText_average_score_static.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		gSizer5.Add( self.m_staticText_average_score_static, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText_average_score_active = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_average_score_active.Wrap( -1 )

		self.m_staticText_average_score_active.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		gSizer5.Add( self.m_staticText_average_score_active, 0, wx.ALL, 5 )

		self.m_button_return2index = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_return2index.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		gSizer5.Add( self.m_button_return2index, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_return2index.Bind( wx.EVT_BUTTON, self.StudentScoreList_to_Index )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def StudentScoreList_to_Index( self, event ):
		event.Skip()


