# system package import
import wx
import time
# GUI package import
from GUI.Index import Index
from GUI.ScoreManageMent import ScoreManageMent
from GUI.StudentChooseClass import StudentChooseClass
from GUI.StudentLogin import StudentLogin
from GUI.StudentScoreList import StudentScoreList
from GUI.MessageDialog import MessageDialog_CANCEL, MessageDialog_OK, MessageDialog_Yes_No
# DB package import
from Db.SchoolDbBaseClass import SchoolDbBaseClass
from Db.UserData import UserData


class MyApp(wx.App):
    def __init__(self):
        self.__current_active_frame = "Index"
        self.DBA = SchoolDbBaseClass()
        self.user = UserData()
        wx.App.__init__(self)

    def OnRefresh(self):
        try:
            if self.Index.IsShown():
                self.Index.m_staticText_index_username.SetLabel(self.user.SNAME)
            elif self.ScoreManageMent.IsShown():
                self.ScoreManageMent.m_staticText_class_teacher_active.SetLabel(self.user.SNAME)
                # self.ScoreManageMent.m_staticText_column_name_active.SetLabel()
                self.__refresh_StudentScoureList_data()
            elif self.StudentLogin.IsShown():
                pass
            elif self.StudentChooseClass.IsShown():
                self.StudentChooseClass.m_menuItem_current_user_sno.SetItemLabel(self.user.SNO)
                self.StudentChooseClass.m_menuItem_current_user_sname.SetItemLabel(self.user.SNAME)
                # TODO 刷新数据的操作
            elif self.StudentScoreList.IsShown():
                self.StudentScoreList.m_staticText_student_name.SetLabel(self.user.SNAME)
                self.StudentScoreList.m_staticText_student_id.SetLabel(self.user.SNO)
                self.StudentScoreList.m_staticText_current_time.SetLabel(
                    __import__('datetime').datetime.now().__str__().split('.')[0]
                    # 没错，这样写比较骚
                )
        except TypeError as e:
            print(e)

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
            self.Index.Close()
            self.StudentLogin.Close()
            self.StudentChooseClass.Close()
            self.StudentScoreList.Close()
            self.ScoreManageMent.Close()
            self.ExitMainLoop()

    def __refresh_StudentScoureList_data(self):
        print("刷新学生成绩表")
        data = self.DBA.get_d_student_score_report(sno=self.user.SNO)
        for row in range(data.__len__()):
            for col in range(data[data.__len__() - 1].__len__()):
                self.StudentScoreList.m_grid_student_score_grid.SetCellValue(
                    row=row, col=col, s=str(data[row][col])
                )
        avg = self.DBA.get_d_student_score_report_avg_score(sno=self.user.SNO)
        self.StudentScoreList.m_staticText_average_score_active.SetLabel(str(avg))

    def __bind_event(self):
        # Index Event Bind
        self.Index.Bind(wx.EVT_CLOSE, self.OnCloseWindow, self.Index)

        # ScoreManageMent Event Bind
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnScoreManageMent_selected(event, 'T1'),
                  self.ScoreManageMent.m_button_search_for_sth)

    def __bind_router(self):
        # Index Router
        # Add Router Here
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

        # StudentScoreList Router
        # Add Router Here
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.StudentScoreList.m_button_return2index)

        # self.Bind(wx.EVT_BUTTON,
        #           lambda event: self.OnRouter_change(event, 'Index'),
        #           self.StudentScoreList.button)

        # StudentChooseClass Router
        # Add Router Here
        self.Bind(wx.EVT_MENU,
                  lambda event: self.OnRouter_change(event, 'Index'),
                  self.StudentChooseClass.m_menuItem_StudentChooseClass_to_Index)

        self.Bind(wx.EVT_MENU,
                  lambda event: self.OnRouter_change(event, 'StudentLogin'),
                  self.StudentChooseClass.m_menuItem_StudentChooseClass_to_StudentLogin)

    def OnScoreManageMent_selected(self, event, args):
        for row in range(6):
            for col in range(2):
                self.ScoreManageMent.m_grid_select_column_to_student.SetCellValue(
                    row=row, col=col, s="")
        class_name = self.ScoreManageMent.m_staticText_column_name_active.GetLabel()
        data = self.DBA.get_d_xh_cj_by_classname(class_name)
        self.ScoreManageMent.student2_score_list = data + (6 - data.__len__()) * [0, 0]
        assert self.ScoreManageMent.student2_score_list.__len__() == 6
        for row in range(data.__len__()):
            for col in range(data[data.__len__() - 1].__len__()):
                self.ScoreManageMent.m_grid_select_column_to_student.SetCellValue(
                    row=row, col=col, s=str(data[row][col])
                    # TODO 明天继续写，把剩下的写完了
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
            self.OnRefresh()

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
                self.__refresh_StudentScoureList_data()
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
                self.ScoreManageMent.Show()
                self.SetTopWindow(self.ScoreManageMent)
        self.OnRefresh()


if __name__ == '__main__':
    MyApp().MainLoop()
    wx.Exit()
