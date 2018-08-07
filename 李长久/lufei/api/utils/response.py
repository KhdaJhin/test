
class BaseResponse:

    def __init__(self):
        self.code = 100
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__

    def get_error(self):
        self.error = '获取数据失败'
        self.code = 50
