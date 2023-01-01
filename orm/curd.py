from orm.database import session
from orm.models import User


# 新增用户
def add_user(user):
    # 将实例插入到user表中
    session.add(user)

    # 当前更改只是在session中，需要使用commit确认更改才会写入数据库
    session.commit()


def query_user_by_name(name):
    return session.query(User).filter_by(name=name).first()


admin = User(name='admin', full_name='super-admin', password='helloworld')

add_user(admin)
cur_user = query_user_by_name('admin')

# 要修改需要先将记录查出来
mod_user = session.query(User).filter_by(name='ed').first()

# 将ed用户的密码修改为modify_paswd
mod_user.password = 'modify_passwd'

# 确认修改
session.commit()

# 但是上边的操作，先查询再修改相当于执行了两条语句，和我们印象中的update不一致
# 可直接使用下边的写法，传给服务端的就是update语句
# session.query(User).filter_by(name='ed').update({User.password: 'modify_passwd'})
# session.commit()
# 以同schema的一张表更新另一张表的写法
# 在跨表的update/delete等函数中指定synchronize_session='fetch'表示先进行一次查询再更新/删除，synchronize_session=Fale表示直接更新/删# 而且，比如update table_name where id = 10, 并不是先查一下where id = 10，而是把表中所有的id值遍历查一轮，这导致当记录数以十万百万计时update会非常慢，暂不能理解其精髓建议update都直接synchronize_session=False
# 一定要指定，不然报错Specify 'fetch' or False for the synchronize_session parameter
# session.query(User).filter_by(User.name=User1.name).update({User.password: User2.password}, synchronize_session=False)
# 以一schema的表更新另一schema的表的写法
# 写法与同一schema的一样，只是定义model时需要使用__table_args__ = {'schema': 'test_database'}等形式指定表对应的schema


# 只获取指定字段
# 但要注意如果只获取部分字段，那么返回的就是元组而不是对象了
# session.query(User.name).filter_by(name='ed').all()
# like查询
# session.query(User).filter(User.name.like("ed%")).all()
# 正则查询
# session.query(User).filter(User.name.op("regexp")("^ed")).all()
# 统计数量
# session.query(User).filter(User.name.like("ed%")).count()
# 调用数据库内置函数
# 以count()为例，都是直接func.func_name()这种格式，func_name与数据库内的写法保持一致
# from sqlalchemy import func
# session.query(func.count(User3.name)).one()
# 字段名为字符串形式
# column_name = "name"
# session.query(User).filter(User3.__table__.columns[column_name].like("ed%")).all()
# 获取执行的sql语句
# 获取记录数的方法有all()/one()/first()等几个方法，如果没加这些方法，得到的只是一个将要执行的sql对象，并没真正提交执行
# from sqlalchemy.dialects import mysql
# sql_obj = session.query(User).filter_by(name='ed')
# sql_command = sql_obj.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True})
# sql_result = sql_obj.all()
