class Base:
    host = "192.168.110.8"
    port = 3306
    user = "root"
    password = "123456"
    database = "booksystem1"


class Dev(Base):
    host = "192.168.10.8"


class Pro(Base):
    pass
