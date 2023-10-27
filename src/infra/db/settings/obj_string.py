class Obj_conn:

    def __init__(self):
        self.name_conn = "mysql+pymysql"
        self.username = "root"
        self.password = "surftesk8"
        self.host = "localhost"
        self.database = "arch_clean"
        self.str_conn = self.__init_Obj_conn()

    def __init_Obj_conn(self):
        return f"{self.name_conn}://{self.username}:{self.password}@{self.host}/{self.database}"

    def __repr__(self):
        return f'{self.str_conn}'