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

    def single_user_data(self, ac, pwd):
        '''
        :param ac: 账号
        :param pwd: 密码
        :return: 第一条记录;不可能有Bug的
        '''
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute('SELECT * FROM S WHERE LOGN=\'{sno}\' AND PSWD=\'{pswd}\''.format(
            sno=ac, pswd=pwd
        ))
        for row in cursor:
            return row
        return False

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
        print(d_sc)
        return d_sc
