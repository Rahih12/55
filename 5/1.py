class Student:
    def __init__(self, id, f_n, v, g):
        self.id = id
        self.f_n = f_n
        self.v = v
        self.g = g

    def print(self):
        print(f"| {self.id:<2}  | {self.f_n:<40} | {self.v:<8} | {self.g:<7} |")

f = open('12.txt', 'r', encoding="utf-8")

ss = []

for l_n, s_str in enumerate(f, start=1):
    s = s_str.strip().split(";")
    if len(s) >= 4:
        id, name, gender, var = s[:4]
        student = Student(id, name, gender, var)
        ss.append(student)
    else:
        print(f"не то {l_n}: {s_str}")

f.close()

print("-----------------------------------------------------------------------")
print("| ID | ФИО                                       | ВАРИАНТ  | ГЕНДЕР  |")
print("-----------------------------------------------------------------------")

for sn in ss:
    sn.print()

print("-----------------------------------------------------------------------")
