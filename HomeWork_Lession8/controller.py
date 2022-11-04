import view as view
import excellentStudent as exS
import femail as femail
import gradeAdd as addG
import noSubject as noS

def startProg():
    x = "HomeWork_Lession8\Students.json"
    y = "HomeWork_Lession8\AcademicP.json"
    z = "HomeWork_Lession8\Subject.json"
    action = view.user_input()
    if action == 1:
        exS.student(x, y, z)
    elif action == 2:
        femail.subject(x, y, z)
    elif action == 3:
        noS.subject(x, y, z)
    elif action == 4:
        newGrade = [view.addName()]
        addG.subject(x, y, z, newGrade)
