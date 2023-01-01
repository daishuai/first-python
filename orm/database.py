from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 以相对路径形式，在当前目录下创建数据库
engine = create_engine('sqlite:///foo.db?check_same_thread=False', echo=True)
# echo=Ture----echo默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印
# check_same_thread=False----sqlite默认建立的对象只能让建立该对象的线程使用，而sqlalchemy是多线程的所以我们需要指定check_same_thread=False来让建立的对象任意线程都可使用。

# 建立基本映射类，后面真正的映射类都要继承它
Base = declarative_base()

# 建立会话
Session = sessionmaker(bind=engine)

session = Session()
# 以绝对路径形式创建数据库
# Unix/Mac
# engine = create_engine('sqlite:////root/foo.db')
# Windows
# engine = create_engine('sqlite:///D:\\user\\foo.db')
# engine = create_engine(r'sqlite:///D:\user\foo.db')
