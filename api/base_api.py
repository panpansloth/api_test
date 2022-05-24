import threading


# 单例模式
class Singleton:
    _instance_lock = threading.Lock()
    _is_init = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton._instance

    def __init__(self):
        if not self._is_init:
            self._is_init = True
            self.a = 1
            self.b = 2
            print(self.a, self.b)

    def get_common(self):
        return {"a": self.a, "b": self.b}


single1 = Singleton()
single2 = Singleton()
print(id(single1) == id(single2))

