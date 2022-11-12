import BD as BD

def subject(a, b, c):
    BD_student = BD.load(a)
    BD_academic = BD.load(b)
    BD_subject = BD.load(c)
    subjectlist = []
    gradelist = []
    for i in BD_academic:
        grade = BD_academic[i]
        gradelist.append(grade[1])
    for j in BD_subject:
        subj = BD_subject[j]
        if j not in gradelist:
            subjectlist.append(subj[0])
    return subjectlist
