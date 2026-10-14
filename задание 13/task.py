import time
class Timer():
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.finish = time.perf_counter()
        itog = self.finish - self.start
        print(itog, "Секунд")
        pass
def test_func():
    print("Начало")
    time.sleep(3)
    print("Конец")
with Timer():
    test_func()
