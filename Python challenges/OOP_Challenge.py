#Oop challenge
#Question 1


class Assessment():
    def __init__(self,name, studentNo, subject, assignmentMark, testMark,
                 practicalMark, internalExamMark,final_mark,rating):
            self.name = name
            self.studentNo = studentNo
            self.subject = subject
            self.assignmentMark = assignmentMark
            self.testMark = testMark
            self.practicalMark = practicalMark
            self.internalExamMark = internalExamMark
            self.final_mark =  final_mark
            self.rating = rating


    def CalcFinalMark(self):
        if 100 >= self.internalExamMark >= 0:
            self.final_mark = (
                        self.assignmentMark * 0.1 + self.testMark * 0.1 + self.practicalMark * 0.2 + self.internalExamMark * 0.6)
            return self.final_mark
        else:
            print("Err... Mark range is not between 0 and 100")

    def DetermineRating(self):
        if self.final_mark < 50:
            self.rating = "Not Yet Compentent"
            return self.rating
        else :
            self.rating = "Competent"
            return self.rating
c1 = Assessment(-80,"english", -23,-46,-23,-43,0,"")

if 100 > c1.internalExamMark > 0:
        print(c1.CalcFinalMark(), c1.DetermineRating())

else:
    print("Err... Mark range is not between 0 and 100")
