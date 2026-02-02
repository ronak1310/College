print("Grading System")
sub1=int(input("ENTER MARKS OF SUBJECT 1:"))
sub2=int(input("ENTER MARKS OF SUBJECT 2:"))
sub3=int(input("ENTER MARKS OF SUBJECT 3:"))
sub4=int(input("ENTER MARKS OF SUBJECT 4:"))
sub5=int(input("ENTER MARKS OF SUBJECT 5:"))
total=sub1+sub2+sub3+sub4+sub5
per=total/5
if(per>=75):
    print("Grade A")
elif(per<75 and per>=65):
    print("Grade B")
elif(per<65 and per>=45):
    print("Grade C")
elif(per<45 and per>=35):
    print("Grade D")
else:
    print("Fail")
