class BaseConfig:
    DEBUG = True
    # DATABASE_URL = "localhost://..."


# 开发环境
class DevConfig(BaseConfig):
    pass


# 测试环境
class TestConfig(BaseConfig):
    #DATABASE_URL = "172.25.36.12://..."
    pass


# 生产环境
class ProConfig(BaseConfig):
    DEBUG = False
    # DATABASE_URL = "192.56.36.10://..."
