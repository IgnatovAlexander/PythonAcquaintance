import BD as BD
import view as view


def subject(a, b, c, newGrade):
    BD_student = BD.load(a)
    BD_academic = BD.load(b)
    BD_subject = BD.load(c)
    subjectlist = []
    gradelist = []
    for i in BD_academic:
        gradelist.append(i)
    a = len(gradelist) + 1
    BD_academic[a] = newGrade
    BD.save(BD_academic, b)
    print("Элемент добавлен")


# subject()
