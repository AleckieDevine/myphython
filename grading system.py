mark1=int(input("what did you score in the following units:programming in phython:"))
mark2=int(input("software engineering:"))
mark3=int(input("telecommunication and broadcasting systems:"))
mark4=int(input("computer and information systems security:"))

overallMark= mark1 + mark2+ mark3 + mark4
averageMark=overallMark/4
print("your average Marks:",averageMark)

if averageMark >=70 and averageMark <= 100:
    print("your mean grade is 'A'")
    elif averageMark>=60 and averageMark<=69:
        print("your mean grade is 'B'")
        elif averageMark >=50 and averageMark <=59:
            print("your mean grade is 'C'")
            elif averageMark >=40 and averageMark <=49:
                print("your mean grade is 'D'")
                else:print("your mean grade is 'E',you failed!")