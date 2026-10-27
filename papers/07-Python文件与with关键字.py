#文件基本使用
# file = open("test.txt", "w")
# file.write("hello world")
# file.close()
#使用with关键字
with open("test.txt", "w") as file:
    file.write("hello world")


#自定义上下文管理器
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False


# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))