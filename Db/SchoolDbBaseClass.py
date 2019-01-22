import pymssql

from config import MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, MSSQL_DATABASE


# dataWindow without param
# d_c 课程表
# d_s 学生表
# d_score_dis 成绩分布表

class SchoolDbBaseClass(object):
    '''
    别和我说什么sql注入，老子就是一把梭！
    '''

    def __init__(self):
        self.conn = self.conn = pymssql.connect(MSSQL_HOST, MSSQL_USER,
                                                MSSQL_PASSWORD, MSSQL_DATABASE)

        # cursor = conn.cursor(as_dict=True)

    def connect(self):

        if not self.conn.cursor():
            self.conn = pymssql.connect(MSSQL_HOST, MSSQL_USER,
                                        MSSQL_PASSWORD, MSSQL_DATABASE)

    def single_user_data(self, ac):
        '''
        :param ac: 账号
        :param pwd: 密码
        :return: 第一条记录;不可能有Bug的
        '''
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute('SELECT SNO AS 学号, SNAME AS 姓名, AGE AS 年龄,SEX AS 性别, SDEPT AS 所在院系'
                       ' FROM S WHERE LOGN=\'{sno}\''.format(
            sno=ac
        ))
        for row in cursor:
            return row
        return False

    def single_user_score(self, ac):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute('SELECT C2.CNO AS 课程号 , GRADE AS 平时成绩 , PGRADE AS 考试成绩 , EGRADE AS 总评成绩 , C2.CNAME AS 课程名称'
                       ' FROM SC LEFT JOIN C C2 on SC.CNO = C2.CNO'
                       ' WHERE SC.SNO = \'{SNO}\''.format(SNO=ac)
                       )
        s_u_score = []
        for row in cursor:
            if row['课程号'] is not None:
                s_u_score.append([row['课程号'].strip(" "),
                                  row['课程名称'].strip(" "),
                                  str(row['平时成绩']).strip(" "),
                                  str(row['考试成绩']).strip(" "),
                                  str(row['总评成绩']).strip(" ")])
        return s_u_score

    def login(self, ac, pwd):
        cursor = self.conn.cursor(as_dict=True)
        print(ac)
        cursor.execute(
            '''
            SELECT CASE 
            WHEN (SELECT COUNT(*) FROM S WHERE SNO=\'{}\')=1 THEN 1
            WHEN (SELECT COUNT(*) FROM T WHERE TNO=\'{}\')=1 THEN -1
            ELSE 0 END as T;
            '''.format(ac, ac))
        for i in cursor:
            s_or_t = i['T']
            if s_or_t == 1:
                cursor.execute('SELECT * FROM S WHERE LOGN=\'{sno}\' AND PSWD=\'{pswd}\''.format(
                    sno=ac, pswd=pwd
                ))
                for row in cursor:
                    row['is_T'] = False
                    return row
                return False
            elif s_or_t == -1 and ac == pwd:
                cursor.execute('SELECT TNO AS SNO,TNAME AS SNAME FROM T WHERE TNO=\'{sno}\''.format(
                    sno=ac
                ))
                for row in cursor:
                    row['is_T'] = True
                    return row
                return False
            else:
                return False

    def get_c(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT CNAME AS 课程,TNAME AS 任课教师 FROM C'
        )
        d_c = {}
        for row in cursor:
            if row['课程'] is not None:
                d_c[row['课程'].strip(" ")] = row['任课教师'].strip(" ") if row['任课教师'] is not None else "???"
        return d_c

    def get_d_student_score_report(self, sno):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT C2.CNO AS 课程号,C2.CNAME AS 课程名 , EGRADE AS 成绩, CREDIT AS 学分,TNAME AS 教师 '
            'FROM SC AS SC1 '
            'LEFT JOIN C C2 on SC1.CNO = C2.CNO '
            'LEFT JOIN TC T on C2.CNO = T.CNO '
            'WHERE SC1.SNO = \'{}\''.format(sno)
        )
        d_student_score_report = []
        for row in cursor:
            d_student_score_report.append([row['课程号'].strip(" "),
                                           row['课程名'].strip(" "),
                                           row['成绩'],
                                           row['学分'],
                                           row['教师'].strip(" ")], )
        return d_student_score_report

    def get_d_student_score_report_avg_score(self, sno):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT AVG(EGRADE) AS 平均分 FROM SC WHERE SNO=\'{}\''.format(sno)
        )
        for row in cursor:
            return row['平均分']

    def get_d_xh_cj_by_classname(self, classname):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            "SELECT SNO AS 学号,EGRADE AS 成绩 FROM SC LEFT JOIN C C2 on SC.CNO = C2.CNO WHERE C2.CNAME=\'{}\'".format(
                classname)
        )
        d_sc = []
        for row in cursor:
            if row['学号'] is not None:
                d_sc.append([row['学号'].strip(" "), str(row['成绩']).strip(" ")])
        # print(d_sc)
        return d_sc

    def get_selectable_classes(self, arg):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT  CNO AS 课程号, CNAME AS 课程名 ,CREDIT AS 学分, TNAME AS 任课教师,CDEPT AS 开课系 FROM C'
        )
        c = []
        for row in cursor:
            if row['任课教师'] is not None:
                c.append([row['课程号'].strip(" "),
                          row['课程名'].strip(" "),
                          str(row['学分']),
                          row['开课系'].strip(" "),
                          row['任课教师'].strip(" ")], )
        return c

    def get_avg_s_group_by_class(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT C2.CNAME AS 课程名,AVG(GRADE) AS 平均成绩 FROM SC LEFT JOIN C C2 on SC.CNO = C2.CNO GROUP BY C2.CNAME'
        )
        label_list = []
        data_list = []
        # for row in cursor:
        #     avg_s_g_by_class.append([
        #         row['课程名'].strip(" "),
        #         str(row['平均成绩'])
        #     ])
        for row in cursor:
            label_list.append(
                row['课程名'].strip(" ")
            )
            data_list.append(
                row['平均成绩']
            )
        return label_list, data_list

    def m_manage_StudentDetail(self, ac):
        '''
        :param ac: 账号
        :param pwd: 密码
        :return: 第一条记录;不可能有Bug的
        '''
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT SNO AS 学号, SNAME AS 姓名, AGE AS 年龄,SEX AS 性别, SDEPT AS 所在院系,LOGN AS 登录名,PSWD AS 密码 FROM S')
        m_sd = []

        for row in cursor:
            if row['学号'] is not None:
                m_sd.append([row['学号'].strip(" "),
                             row['姓名'].strip(" "),
                             str(row['年龄']),
                             row['性别'].strip(" "),
                             row['所在院系'].strip(" "),
                             row['登录名'].strip(" "),
                             row['密码'].strip(" "),
                             ])
        return m_sd

    def manage_s_insert_data(self, insert_data):
        assert insert_data.__len__() == 8
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute('INSERT INTO S VALUES'
                       '(\'{SNO}\',\'{SNAME}\',\'{SEX}\',{AGE},\'{SDEPT}\',{FEES},\'{LOGN}\',\'{PSWD}\')'.format(
            SNO=insert_data[0],
            SNAME=insert_data[1],
            SEX=insert_data[2],
            AGE=insert_data[3],
            SDEPT=insert_data[4],
            FEES=insert_data[5],
            LOGN=insert_data[6],
            PSWD=insert_data[7]
        ))

    def manage_s_update_data(self, insert_data):
        pass

    def manage_s_delete_data(self, SNO):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute('DELETE FROM S WHERE  SNO  = \'{}\''.format(SNO))

    def manage_c_insert_data(self, insert_data):
        assert insert_data.__len__() == 5
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("INSERT INTO C VALUES "
                       "('{CNO}','{CNAME}',{CREDIT},'{CDEPT}','{TNAME}')".format(
            CNO=insert_data[0],
            CNAME=insert_data[1],
            CREDIT=insert_data[2],
            CDEPT=insert_data[3],
            TNAME=insert_data[4]
        ))

    def manage_c_update_data(self, data):
        pass

    def manage_c_delete_data(self, CNO):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("DELETE FROM C WHERE  CNO = '{}'".format(CNO))

# def m_manage_ClassDetail(self):
#     cursor = self.conn.cursor(as_dict=True)
#     cursor.execute('SELECT  CNO 课程号, CNAME 课程名, CREDIT 学分数, CDEPT 所在系 ,TNAME 任课教师  FROM C')
#     m_cd = []
#     for row in cursor:
#         if row['任课教师'] is not None:
#             m_cd.append([row['课程号'].strip(" "),
#                       row['课程名'].strip(" "),
#                       str(row['学分数']),
#                       row['所在系'].strip(" "),
#                       row['任课教师'].strip(" ")], )
#     return m_cd
