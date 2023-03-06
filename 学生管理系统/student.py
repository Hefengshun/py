def main( ) :
    while True :
        menm( )
        num = int( input( "请选择" ) )
        if num in [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ] :
            if num == 0 :
                y = input( "您确定退出系统吗 y/n" )
                if y == "y" or y == "Y" :
                    input( "谢谢您的使用" )
                    break  # 退出系统
                else :
                    continue
            elif num == 1 :
                insert( )  # 录入学生信息
            elif num == 2 :
                search( )  # 查找
            elif num == 3 :
                delete( )  # 删除
            elif num == 4 :
                modify( )  # 修改
            elif num == 5 :
                sort( )  # 排序
            elif num == 6 :
                total( )  # 统计
            elif num == 7 :
                show( )  # 显示


def menm( ) :
    print( "-----------------------------学生管理系统---------------------------------" )
    print( "-----------------------------功能菜单---------------------------------" )
    print( "\t\t\t\t\t\t\t1.录入学生信息" )
    print( "\t\t\t\t\t\t\t2.查找学生信息" )
    print( "\t\t\t\t\t\t\t3.删除学生信息" )
    print( "\t\t\t\t\t\t\t4.修改学生信息" )
    print( "\t\t\t\t\t\t\t5.排序学生信息" )
    print( "\t\t\t\t\t\t\t6.统计学生信息" )
    print( "\t\t\t\t\t\t\t7.显示学生信息" )
    print( "\t\t\t\t\t\t\t0.退出" )


def insert( ) :
    stu_list = [ ]
    while True :
        id = input( "请输入学生id" )
        if not id :
            break
        name = input( "请输入姓名：" )
        if not name :
            break
        try :
            enblist = int( input( "请输入英语成绩" ) )
            python = int( input( "请输入py成绩" ) )
            java = int( input( "请输入java成绩" ) )
        except :
            print( "输入无效，不是整数类型" )
            continue
        # 将录入的学生信息录入到字典中
        studet = { "id" : id , "name" : name , "enblist" : enblist , "python" : python , "java" : java }
        # 将我们的学生信息添加到列表当中
        stu_list.append( studet )
        answer = input( "是否继续添加y/n\n" )
        if answer == "y" or answer == "Y" :
            continue
        else :
            break
    # 调用save()函数
    save( stu_list )
    print( "学生信息录入完毕" )


def save( list ) :
    try:
        stu

def search( ) :
    pass


def delete( ) :
    pass


def modify( ) :
    pass


def sort( ) :
    pass


def total( ) :
    pass


def show( ) :
    pass


if __name__ == '__main__' :
    main( )
