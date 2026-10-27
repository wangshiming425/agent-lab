# 定义一个类(Human)
class Human:
    # 对象创建调用
    def __init__(self, name: str, age: int, gender: str):
        self.name = name,
        self.age = age,
        self.gender = gender

    # 私有属性
    __varible = "私有变量"
    varible = "共有变量"

    # 打印调用
    def __str__(self) -> str:
        return f"Human(name={self.name}, age={self.age}, gender={self.gender})"


human = Human("张三", 23, "男")
print(human)
print(human.varible)
# 访问私有属性  对象._类名__私有属性名
print(human._Human__varible)


# 继承:可以有多继承
class Student():
    def __init__(self, name: str, age: int, gender: str, student_id: str):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def __str__(self) -> str:
        return f"Student(name={self.name}, age={self.age}, gender={self.gender}, student_id={self.student_id})"


class LargeStudent(Student, Human):
    def __init__(self, name: str, age: int, gender: str, student_id: str, large_id: str):
        super().__init__(name, age, gender, student_id)
        self.large_id = large_id

    def __str__(self) -> str:
        return f"LargeStudent(name={self.name}, age={self.age}, gender={self.gender}, student_id={self.student_id}, large_id={self.large_id})"

large_student = LargeStudent("张三", 23, "男", "123456", "789012")
print(large_student)
print(LargeStudent.mro())

#多态:鸭子类型,只要你会游泳,你就是一只鸭子,也就是你只要有对应的方法,你就可以被当作正确的参数
#区别于Java的多态,有严格的继承或实现关系才能传入

