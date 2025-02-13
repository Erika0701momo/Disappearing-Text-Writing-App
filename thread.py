import threading
import ctypes


class CustomThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        """コンストラクタ"""
        super().__init__(*args, **kwargs)
        self._run = self.run
        self.run = self.set_id_and_run

    def set_id_and_run(self):
        """runメソッドをオーバーライド"""
        self.id = threading.get_native_id()
        self._run()

    def get_id(self):
        return self.id

    def raise_exception(self):
        """特定のスレッドにSystemExit例外を送信してスレッドを強制終了"""
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(self.get_id()),
            ctypes.py_object(SystemExit)
        )
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(
                ctypes.c_long(self.get_id()),
                0
            )
            print('Failure in raising exception')