# entry point to the app

def main():
    # to collect and save student details 
    students = []
    status = True
    while status:
        print('======MENU======')
        print('1. Add student')
        print('2. Add Scholarship Student')
        print('3. Add view all Student')
        print('4. Exit')

        user_choice = input("Enter your choice: ")

        if(user_choice =='1'):
            ## methods to add student
            print("Student added successfully")
        elif (user_choice =='2'):
            ## method to add scholarship students
            print("Scholarship Student added successfully")
        elif(user_choice =='3'):
            ## display entries i 'students'
            print("***************")
        elif(user_choice =='4'):
            status=False
            print("bye")
            break       # used to break a loop(for or while)
        else:
            print('please select a valid choice')


 

# initialize python project
if __name__ == '__main__':
    main()