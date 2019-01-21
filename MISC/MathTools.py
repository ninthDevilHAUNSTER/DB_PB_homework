import math
from  binascii import hexlify


def sxor(s1, s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return b''.join(bytes(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def list_similarity_alg(changed_list, raw_list):
    '''
    列相似度算法
    复杂度 O(n^2)
        XOR 两列表中的元素
            如果为 0  相似
            如果为 changed_list 则代表为 Insert
            如果为 raw_list 则代表为 Delete
            如果为 别的 则代表为 Update
    :param list1:
    :param list2:
    :return:
    '''
    assert changed_list.__len__() == raw_list.__len__()
    assert changed_list[0].__len__() == raw_list[0].__len__()
    update_exec = "UPDATE SC SET EGRADE = {} " \
                  "WHERE SNO=\'{SNO}\'  " \
                  "AND CNO=(" \
                  "SELECT CNO FROM C WHERE CNAME=\'{CNAME}\'" \
                  ")"
    delete_exec = "DELETE FROM SC " \
                  "WHERE SNO=\'{SNO}\'  " \
                  "AND CNO=(" \
                  "SELECT CNO FROM C WHERE CNAME=\'{CNAME}\'" \
                  ")"
    insert_exec = "INSERT INTO SC(SNO,CNO,EGRADE)" \
                  " VALUES (\'{SNO}\',(SELECT CNO FROM C WHERE  CNAME = \'{CNAME}\'),{EGRADE})"
    result_list = []
    for row in range(changed_list.__len__()):

        # print(sxor(changed_list[row][0], raw_list[row][0]),end='   ')
        # print(sxor(changed_list[row][1], raw_list[row][1]))



if __name__ == '__main__':
    list_similarity_alg([['S1', '60'], ['S2', '76'], ['S3', '86'], ['S4', '69'], ['S5', '69'], ['S6', '80']],
                        [['S1', '60'], ['S2', '76'], ['S3', '86'], ['S4', '69'], ['S5', '69'], ['S6', '79']])
    print('##')
    list_similarity_alg([['S4', '78'], ['S5', '79'], ['', ''], ['', ''], ['', ''], ['', '']],
                        [['S4', '78'], ['', ''], ['', ''], ['', ''], ['', ''], ['', '']])
