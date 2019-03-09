#%%

class NameSpace:
    a = "重名的属性"
    b = "类属性"
    def __init__(self):
        self.a = "实例中重名的属性"
        self.c = "实例属性"

    def get(self):
        print(
            self.a,
            self.b,
            self.c,
            sep="\n"
        )

    @classmethod
    def get_cls(cls):
        print(
            cls.a,
            cls.b,
            # cls.c,
            sep="\n"
        )

    @staticmethod
    def get_static(*args, **kwargs):
        print(
            *args,
            kwargs.items(),
            sep="\n"
        )

#%%

x = NameSpace()

#%%

x.get()

#%%

x.get_cls()

#%%

x.get_static(
    1, 2, 3, name=123
)
