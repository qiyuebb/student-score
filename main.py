# teacher_module.py
class Teacher:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_course(self, course_id, course_name):
        """
        教师录入课程信息：
        修复问题：防止重复课程编号、空课程名导致异常。
        """
        if not course_name.strip():
            raise ValueError("课程名称不能为空")

        if course_id in self.courses:
            raise ValueError(f"课程编号 {course_id} 已存在，请检查输入。")

        self.courses[course_id] = course_name
        print(f"✅ {self.name} 成功录入课程：{course_name}（编号：{course_id}）")
        return True


if __name__ == "__main__":
    teacher = Teacher("张11sss老师")
    try:
        teacher.add_course("C001", "Python程序设计")
        teacher.add_course("C001", "数据库系统")  # 故意重复，触发异常
    except ValueError as e:
        print("❌ 录入失败，原因：", e)
