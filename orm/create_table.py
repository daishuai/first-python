from orm.database import Base, engine
from orm.models import User

# 查看映射对应的表
var = User.__table__

# 创建数据表。一方面通过engine来连接数据库，另一方面根据哪些类继承了Base来决定创建哪些表
# checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
Base.metadata.create_all(engine, checkfirst=True)

# 上边的写法会在engine对应的数据库中创建所有继承Base的类对应的表，但很多时候很多只是用来则试的或是其他库的
# 此时可以通过tables参数指定方式，指示仅创建哪些表
# Base.metadata.create_all(engine,tables=[Base.metadata.tables['users']],checkfirst=True)
# 在项目中由于model经常在别的文件定义，没主动加载时上边的写法可能写导致报错，可使用下边这种更明确的写法
# User.__table__.create(engine, checkfirst=True)

# 另外我们说这一步的作用是创建表，当我们已经确定表已经在数据库中存在时，我完可以跳过这一步
# 针对已存放有关键数据的表，或大家共用的表，直接不写这创建代码更让人心里踏实
