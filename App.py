# system package import
import wx
import wx.grid
# GUI package import
from GUI.Index import Index
from GUI.ScoreManageMent import ScoreManageMent
from GUI.StudentChooseClass import StudentChooseClass
from GUI.StudentLogin import StudentLogin
from GUI.StudentScoreList import StudentScoreList
from GUI.MessageDialog import MessageDialog_CANCEL, MessageDialog_OK, MessageDialog_Yes_No
from GUI.ScoreAnalyze import ScoreAnalyze
# DB package import
from Db.SchoolDbBaseClass import SchoolDbBaseClass
# MISC package import
from MISC.UserData import UserData


class MyApp(wx.App):
    def __init__(self):
        self.__current_active_frame = "Index"
        self.DBA = SchoolDbBaseClass()
        self.user = UserData()
        wx.App.__init__(self)

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
        # Init Router
        self.__bind_router()
        self.__bind_event()

        # Show Index
        self.Index.Show(show=True)
        return True

    def OnCloseWindow(self, event):
        _ = MessageDialog_Yes_No("你确定要退出么", "提示信息")
        if _:
            self.Index.Hide()
            self.StudentLogin.Hide()
            self.StudentChooseClass.Hide()
            self.StudentScoreList.Hide()
            self.ScoreManageMent.Hide()
            self.ScoreAnalyze.Hide()
            self.ExitMainLoop()

    def __OnRefresh_StudentScoureList(self, event, arg):
        print("刷新学生成绩表")
        if self.user.SNO is not None:
            self.StudentScoreList.m_staticText_student_name.SetLabel(self.user.SNAME)
            self.StudentScoreList.m_staticText_student_id.SetLabel(self.user.SNO)
        self.StudentScoreList.m_staticText_current_time.SetLabel(
            __import__('datetime').datetime.now().__str__().split('.')[0]
            # 没错，这样写比较骚
        )
        data = self.DBA.get_d_student_score_report(sno=self.user.SNO)
        for row in range(data.__len__()):
            for col in range(data[data.__len__() - 1].__len__()):
                self.StudentScoreList.m_grid_student_score_grid.SetCellValue(
                    row=row, col=col, s=str(data[row][col])
                )
        avg = self.DBA.get_d_student_score_report_avg_score(sno=self.user.SNO)
        self.StudentScoreList.m_staticText_average_score_active.SetLabel(str(avg))

    def __OnRefresh_StudentChooseClass(self, event, arg):
        print("刷新选课表数据")
        # set menu value
        if self.user.SNO is not None:
            self.StudentChooseClass.m_menuItem_current_user_sno.SetItemLabel(self.user.SNO)
            self.StudentChooseClass.m_menuItem_current_user_sname.SetItemLabel(self.user.SNAME)

        # set 学生信息表 value
        single_user_data = self.DBA.single_user_data(ac=arg)
        self.StudentChooseClass.student_detail_grid.SetCellValue(
            0, 0, single_user_data['学号']
        )
        self.StudentChooseClass.student_detail_grid.SetCellValue(
            0, 1, single_user_data['姓名']
        )
        self.StudentChooseClass.student_detail_grid.SetCellValue(
            0, 2, single_user_data['年龄']
        )
        self.StudentChooseClass.student_detail_grid.SetCellValue(
            0, 3, single_user_data['性别']
        )
        self.StudentChooseClass.student_detail_grid.SetCellValue(
            0, 4, single_user_data['所在院系']
        )

        # set 学生成绩表value
        single_user_score = self.DBA.single_user_score(ac=arg)
        self.StudentChooseClass.passed_class_grid.ClearGrid()
        if self.StudentChooseClass.passed_class_grid.GetNumberRows() < single_user_score.__len__():
            self.StudentChooseClass.passed_class_grid.AppendRows(
                single_user_score.__len__() - self.StudentChooseClass.passed_class_grid.GetNumberRows())
        else:
            self.StudentChooseClass.passed_class_grid.DeleteRows(
                numRows=self.StudentChooseClass.passed_class_grid.GetNumberRows() - single_user_score.__len__())

        for row in range(self.StudentChooseClass.passed_class_grid.GetNumberRows()):
            for col in range(self.StudentChooseClass.passed_class_grid.GetNumberCols()):
                self.StudentChooseClass.passed_class_grid.SetCellValue(row, col, single_user_score[row][col])

        selectable_column_list = self.DBA.get_selectable_classes(arg=1)
        self.StudentChooseClass.selectable_class_grid.ClearGrid()
        if self.StudentChooseClass.selectable_class_grid.GetNumberRows() < selectable_column_list.__len__():
            self.StudentChooseClass.selectable_class_grid.AppendRows(
                selectable_column_list.__len__() - self.StudentChooseClass.selectable_class_grid.GetNumberRows())
        else:
            self.StudentChooseClass.selectable_class_grid.DeleteRows(
                numRows=self.StudentChooseClass.selectable_class_grid.GetNumberRows() - selectable_column_list.__len__())

        for row in range(self.StudentChooseClass.selectable_class_grid.GetNumberRows()):
            for col in range(self.StudentChooseClass.selectable_class_grid.GetNumberCols()):
                self.StudentChooseClass.selectable_class_grid.SetCellValue(row, col, selectable_column_list[row][col])

        if self.StudentChooseClass.selected_class_grid.GetNumberRows() > 0:
            self.StudentChooseClass.selected_class_grid.DeleteRows(
                numRows=self.StudentChooseClass.selected_class_grid.GetNumberCols()
            )

    def __OnRefresh_ScoreManageMent(self, event, arg):
        print("刷新成绩管理页面数据")
        if self.user.SNO is not None:
            self.ScoreManageMent.m_staticText_class_teacher_active.SetLabel(self.user.SNAME)

    def __OnRefresh_Index(self, event, arg):
        print("刷新首页数据")
        if self.user.SNO is not None:
            self.Index.m_staticText_index_username.SetLabel(self.user.SNAME)

    def __OnRefresh_StudentLogin(self, event, arg):
        print("刷新登陆页面数据")
        # event.Skip()

    def __bind_event(self):
        # Index Event Bind
        self.Index.Bind(wx.EVT_SHOW,
                        lambda event: self.__OnRefresh_Index(event, '1'),
                        self.Index)

        # ScoreManageMent Event Bind
        self.ScoreManageMent.Bind(wx.EVT_SHOW,
                                  lambda event: self.__OnRefresh_ScoreManageMent(event, '1'),
                                  self.ScoreManageMent)
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnScoreManageMent_selected(event, 'T1'),
                  self.ScoreManageMent.m_button_search_for_sth)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnInputLock_ScoreManageMent(event, '1'),
                  self.ScoreManageMent.m_button_input_score)
        self.ScoreManageMent.m_button_score_analyze.Bind(wx.EVT_BUTTON,
                                                         lambda event: self.OnRouter_change(event, 'ScoreAnalyze'))

        # StudentScoreList Event Bind
        self.StudentScoreList.Bind(wx.EVT_SHOW,
                                   lambda event: self.__OnRefresh_StudentScoureList(event, '1'),
                                   self.StudentScoreList)

        # StudentLogin Event Bind
        self.StudentLogin.Bind(wx.EVT_SHOW,
                               lambda event: self.__OnRefresh_StudentLogin(event, '1'),
                               self.StudentLogin)

        # StudentChooseClass Event Bind
        self.StudentChooseClass.Bind(wx.EVT_SHOW,
                                     lambda event: self.__OnRefresh_StudentChooseClass(event, self.user.SNO),
                                     self.StudentChooseClass)
        self.StudentChooseClass.passed_class_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,
                                                       lambda event: self.OnRouter_change(event,
                                                                                          value='StudentScoreList'))
        self.StudentChooseClass.passed_class_grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,
                                                       lambda event: self.OnRouter_change(event,
                                                                                          value='StudentScoreList'))
        self.StudentChooseClass.drop_class_button.Bind(wx.EVT_BUTTON,
                                                       self.OnDropSelectedClass_StudentChooseClass)
        self.StudentChooseClass.update_class_button.Bind(wx.EVT_BUTTON,
                                                         self.OnUpdateSelectedClass_StudentChooseClass)

        # ScoreAnalyze Event Bind
        self.ScoreAnalyze.Bind(wx.EVT_SHOW,
                               self.ScoreAnalyze.draw_event, self.ScoreAnalyze)

    def OnDropSelectedClass_StudentChooseClass(self, event):
        CNO = self.StudentChooseClass.m_textCtrl5.GetValue().strip()
        print(CNO)
        index = -1
        for i in range(self.StudentChooseClass.selected_class_grid.GetNumberRows()):
            if CNO == self.StudentChooseClass.selected_class_grid.GetCellValue(row=i, col=0):
                index = i
        if index == -1:
            MessageDialog_OK('查无该课程号，无法选该课程', '提示信息')
            return False
        else:
            selected_class_rownum = self.StudentChooseClass.selectable_class_grid.GetNumberRows()
            self.StudentChooseClass.selectable_class_grid.AppendRows(1)
            for col in range(self.StudentChooseClass.selectable_class_grid.GetNumberCols()):
                self.StudentChooseClass.selectable_class_grid.SetCellValue(
                    row=selected_class_rownum, col=col,
                    s=self.StudentChooseClass.selected_class_grid.GetCellValue(row=index, col=col)
                )

            self.StudentChooseClass.selected_class_grid.DeleteRows(pos=index, numRows=1)

    def OnUpdateSelectedClass_StudentChooseClass(self, event):
        CNO = self.StudentChooseClass.m_textCtrl5.GetValue().strip()
        print(CNO)
        index = -1
        for i in range(self.StudentChooseClass.selectable_class_grid.GetNumberRows()):
            if CNO == self.StudentChooseClass.selectable_class_grid.GetCellValue(row=i, col=0):
                index = i
        if index == -1:
            MessageDialog_OK('查无该课程号，无法选该课程', '提示信息')
            return False
        else:
            selected_class_rownum = self.StudentChooseClass.selected_class_grid.GetNumberRows()
            self.StudentChooseClass.selected_class_grid.AppendRows(1)
            for col in range(self.StudentChooseClass.selected_class_grid.GetNumberCols()):
                self.StudentChooseClass.selected_class_grid.SetCellValue(
                    row=selected_class_rownum, col=col,
                    s=self.StudentChooseClass.selectable_class_grid.GetCellValue(row=index, col=col)
                )

            self.StudentChooseClass.selectable_class_grid.DeleteRows(pos=index, numRows=1)

    def __bind_router(self):
        # Index Router
        # Add Router Here
        self.Index.Bind(wx.EVT_CLOSE, self.OnCloseWindow, self.Index)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'StudentLogin'),
                  self.Index.m_button_Index2StudentLogin)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'ScoreManageMent'),
                  self.Index.m_button_Index2ScoreManageMent)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'StudentChooseClass'),
                  self.Index.m_button_Index2StudentChooseClass)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'StudentScoreList'),
                  self.Index.m_button_Index2StudentScoreList)

        # StudentLogin Router
        # Add Router Here
        self.StudentLogin.Bind(wx.EVT_CLOSE,
                               lambda event: self.OnRouter_change(event, 'Index'),
                               self.StudentLogin)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.StudentLogin.m_button_return2index)

        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnAccount_login(event,
                                                     account=self.StudentLogin.m_textCtrl_account.GetValue(),
                                                     password=self.StudentLogin.m_textCtrl_password.GetValue()),
                  self.StudentLogin.m_button_login)

        # ScoreManageMent Router
        # Add Router Here
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.ScoreManageMent.m_button_return2index)
        self.ScoreManageMent.Bind(wx.EVT_CLOSE,
                                  lambda event: self.OnRouter_change(event, 'Index'),
                                  self.ScoreManageMent)

        # StudentScoreList Router
        # Add Router Here
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.StudentScoreList.m_button_return2index)
        self.StudentScoreList.Bind(wx.EVT_CLOSE,
                                   lambda event: self.OnRouter_change(event, 'Index'),
                                   self.StudentScoreList)

        # StudentChooseClass Router
        # Add Router Here
        self.Bind(wx.EVT_MENU,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.StudentChooseClass.m_menuItem_StudentChooseClass_to_Index)

        self.Bind(wx.EVT_MENU,
                  lambda event: self.OnRouter_change(event, 'StudentLogin'),
                  self.StudentChooseClass.m_menuItem_StudentChooseClass_to_StudentLogin)
        self.StudentChooseClass.Bind(wx.EVT_CLOSE,
                                     lambda event: self.OnRouter_change(event, 'Index'),
                                     self.StudentChooseClass)

        # ScoreAnalyze Router
        # Add Router Here
        self.ScoreAnalyze.Bind(wx.EVT_CLOSE,
                               lambda event: self.OnRouter_change(event, 'ScoreManageMent'),
                               self.ScoreAnalyze)

    def OnScoreManageMent_selected(self, event, args):
        for row in range(6):
            for col in range(2):
                self.ScoreManageMent.m_grid_select_column_to_student.SetCellValue(
                    row=row, col=col, s="")
        class_name = self.ScoreManageMent.m_staticText_column_name_active.GetLabel()
        data = self.DBA.get_d_xh_cj_by_classname(class_name)
        self.ScoreManageMent.student2_score_list = data + (6 - data.__len__()) * [['', '']]
        assert self.ScoreManageMent.student2_score_list.__len__() == 6
        for row in range(data.__len__()):
            for col in range(data[data.__len__() - 1].__len__()):
                self.ScoreManageMent.m_grid_select_column_to_student.SetCellValue(
                    row=row, col=col, s=str(data[row][col])
                )

    def OnAccount_login(self, event, account="", password=""):
        print("[*]  ACC :: {}".format(account))
        print("[*]  PWD :: {}".format(password))
        result = self.DBA.login(ac=account, pwd=password)
        if result == False:
            MessageDialog_OK('数据库认证失败，请重试', '错误信息')
            return False
        if result != False:
            self.user.SNO = result['SNO']
            self.user.SNAME = result['SNAME']
            self.user.is_teacher = True if result['is_T'] else False
            # self.OnRouter_change_without_event(value="Index")
            self.__current_active_frame = "Index"
            self.StudentLogin.Hide()
            self.Index.Show()

    def UpdateData_ScoreManageMent(self, arg=None):
        current_cell_value = []
        for row in range(6):
            current_cell_value.append([
                self.ScoreManageMent.m_grid_select_column_to_student.GetCellValue(row, 0),
                self.ScoreManageMent.m_grid_select_column_to_student.GetCellValue(row, 1)
            ])
        print(current_cell_value)
        print(self.ScoreManageMent.student2_score_list)

    def OnInputLock_ScoreManageMent(self, event, arg):
        if not self.ScoreManageMent.lock_for_grid:
            print("锁定数据")
            self.ScoreManageMent.m_grid_select_column_to_student.EnableEditing(True)
            self.ScoreManageMent.m_button_search_for_sth.Disable()
            self.ScoreManageMent.m_button_return2index.Disable()
            self.ScoreManageMent.m_button_score_analyze.Disable()
            self.ScoreManageMent.m_button_input_score.SetLabel('保存')
            self.ScoreManageMent.lock_for_grid = True
        else:
            print("解锁数据")
            self.UpdateData_ScoreManageMent()
            # TODO 把这个函数写了,好像写崩了...
            self.ScoreManageMent.m_grid_select_column_to_student.EnableEditing(False)
            self.ScoreManageMent.m_button_search_for_sth.Enable()
            self.ScoreManageMent.m_button_return2index.Enable()
            self.ScoreManageMent.m_button_score_analyze.Enable()
            self.ScoreManageMent.m_button_input_score.SetLabel('输入成绩')
            self.ScoreManageMent.lock_for_grid = False

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


        elif self.__current_active_frame == "StudentChooseClass":
            if self.user.SNO is None:
                print("not login")
                MessageDialog_CANCEL('请先登陆', '提示信息')
            elif self.user.is_teacher:
                print("no student")
                MessageDialog_CANCEL('只有学生身份才能查看成绩单', '提示信息')
            else:
                self.Index.Hide()
                self.StudentLogin.Hide()
                self.StudentChooseClass.Show()
                self.StudentScoreList.Hide()
                self.ScoreManageMent.Hide()
                self.SetTopWindow(self.StudentChooseClass)

        elif self.__current_active_frame == "StudentScoreList":
            if self.user.SNO is None:
                print("not login")
                MessageDialog_CANCEL('请先登陆', '提示信息')
            elif self.user.is_teacher:
                print("no student")
                MessageDialog_CANCEL('只有学生身份才能查看成绩单', '提示信息')
            else:
                self.Index.Hide()
                self.StudentLogin.Hide()
                self.StudentChooseClass.Hide()
                self.StudentScoreList.Show()
                self.ScoreManageMent.Hide()
                self.SetTopWindow(self.StudentScoreList)

        elif self.__current_active_frame == "ScoreManageMent":
            if not self.user.is_teacher:
                print("not teacher")
                MessageDialog_CANCEL('只有老师身份才能管理成绩', '提示信息')
            else:
                self.Index.Hide()
                self.StudentLogin.Hide()
                self.StudentChooseClass.Hide()
                self.StudentScoreList.Hide()
                self.ScoreAnalyze.Hide()
                self.ScoreManageMent.Show()
                self.SetTopWindow(self.ScoreManageMent)
        elif self.__current_active_frame == "ScoreAnalyze":
            self.ScoreAnalyze.Show()
            self.ScoreManageMent.Hide()
            self.SetTopWindow(self.ScoreAnalyze)


if __name__ == '__main__':
    MyApp().MainLoop()
    wx.Exit()
