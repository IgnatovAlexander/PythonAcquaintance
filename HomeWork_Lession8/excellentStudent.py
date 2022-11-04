import BD as BD
import view as view


def student(a, b, c):
    BD_student = BD.load(a)
    BD_academic = BD.load(b)
    studenlist = []
    for i in BD_student:
        name = BD_student[i]
        for j in BD_academic:
            grade = BD_academic[j]
            if grade[0] == i and grade[2] != "5" and name[0] in studenlist:
                studenlist.remove(name[0])
            if grade[0] == i and grade[2] == "5" and name[0] not in studenlist:
                studenlist.append(name[0])
    print(", ".join(studenlist))


# student()
