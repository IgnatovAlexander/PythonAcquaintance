import BD as BD
import view as view


def subject(a, b, c):
    BD_student = BD.load(a)
    BD_academic = BD.load(b)
    BD_subject = BD.load(c)
    subjectlist = []
    for i in BD_subject:
        subj = BD_subject[i]
        for j in BD_academic:
            grade = BD_academic[j]
            for y in BD_student:
                name = BD_student[y]
                if (
                    i == grade[1]
                    and name[2] == "жен."
                    and y == grade[0]
                    and subj[0] not in subjectlist
                ):
                    subjectlist.append(subj[0])
    print(", ".join(subjectlist))


# subject()
