import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hrms"
)

cursor = mydb.cursor()


def add_employee(E_Id,F_Name,M_Name,L_Name,DOB,Address,Email_Address,Contact_no,Joining_date,Designation,Department,Salary):
   
   # Inserting the Employee details
    sql = "INSERT into employees_details(E_Id,F_Name,M_Name,L_Name,DOB,Address,Email_Address,Contact_no,Joining_date,Designation,Department,Salary) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dob = datetime.strptime(DOB, "%Y-%m-%d").date()
    join = datetime.strptime(Joining_date, "%Y-%m-%d").date()
    val = (E_Id,F_Name,M_Name,L_Name,dob,Address,Email_Address,Contact_no,join,Designation,Department,Salary)
    cursor.execute(sql,val,)
    mydb.commit()
    print("\n -------------New Employee",F_Name,"Was Added.-------------")
    print("\n -------------",F_Name,M_Name,L_Name, "Id No. is", E_Id,"-------------" )

def view_employees(E_Id):
    # Fetching employee details
    look = "SELECT * FROM employees_details WHERE E_Id = %s"
    write = (E_Id,)
    cursor.execute(look,write)
    result = cursor.fetchone()
    if result:
        # Result is a tuple containing employee details
        print(f"\n E_Id: {result[0]},\n F_Name: {result[1]},\n M_Name: {result[2]},\n L_Name: {result[3]},"
              f"\n DOB: {result[4]},\n Address: {result[5]},\n Email_Address: {result[6]},"
              f"\n Contact_no: {result[7]},\n Joining_date: {result[8]},\n Designation: {result[9]},"
              f"\n Department: {result[10]},\n Salary: {result[11]}")
    else:
        # No data found for the given E_Id
        print("No employee found with the given ID.")

def attendance(F_name,L_Name,Date,Attendance):
    # Inserting attendance of the employees
    attend="INSERT INTO attendance(F_name,L_Name,Date,Attendance) Values(%s,%s,%s,%s)"
    do = datetime.strptime(Date, "%Y-%m-%d").date()
    mark = (F_name,L_Name,do,Attendance)
    cursor.execute(attend,mark)
    mydb.commit()
    print("\n-------------",F_name,L_Name,"is marked as", Attendance," on the date",Date,"-------------" )

def view_attendance(F_Name,L_Name):
    # Viewing attendance of the employees
    see = "SELECT * FROM attendance WHERE F_Name = %s and L_name = %s"
    check = (F_Name,L_Name)
    cursor.execute(see,check)
    checking = cursor.fetchmany()
    for x in checking:
        print(" \n------------- Attendance Report of",F_Name,L_Name,"-------------")
        print(f"\n------------- Date:{x[3]},Attendance:{x[4]}-------------")

def salary(F_name,L_Name,Payment_date,Amount):
    # Inserting the salary paid to employees
    sal = "INSERT INTO salary_record(F_name,L_Name,Payment_date,Amount) Values(%s,%s,%s,%s)"
    go = (F_name,L_Name,Payment_date,Amount)
    # Convert the date of birth input to a datetime object to ensure correct format
    try:
                dob = datetime.strptime(Payment_date, "%Y-%m-%d").date()
    except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                return
    cursor.execute(sal,go)
    mydb.commit()
    print("\n------------- Salary details were Recorded of",F_name,L_Name,"-------------")

def salary_view(F_name,L_Name):
    #  Checking the record of the salary
    record = "SELECT * FROM salary_record WHERE F_name = %s and L_Name = %s"
    start = (F_name,L_Name)
    cursor.execute(record,start)
    present = cursor.fetchmany()
    for y in present:
        print("\n------------- Salary Record of ", F_name, L_Name,"-------------")
        print(f"\n------------- Reciept_Id:{y[0]}, Payement_date : {y[3]}, Amount : {y[4]}-------------")

def leave(F_Name,L_Name,Reason,From_date,To_date,Days):
    # Writing a leave 
    holiday = "INSERT into `leave`(F_Name,L_Name,Reason,From_date ,To_date,Days) Values(%s,%s,%s,%s,%s,%s)"
    from_date = datetime.strptime(From_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(To_date, "%Y-%m-%d").date()
    grant = (F_Name, L_Name, Reason, from_date, to_date, Days)
    cursor.execute(holiday,grant)
    mydb.commit()
    print("\n-------------",F_Name,L_Name,"your leave for ",Days,"days has been send to the HR .-------------")

def view_leave():
    #Fetching All the Leaves
    find = "SELECT * FROM `leave` "
    cursor.execute(find)
    view = cursor.fetchall()
    for v in view:
        print (f"\n L_Id : {v[0]},\n F_Name:{v[1]},\n L_Name:{v[2]},\n Reason:{v[3]},\n From_date:{v[4]},\n To_date:{v[5]},\n Days:{v[6]}" )    

def Update_leave(L_Id,Status):
    # Updating The leave
    marking = "Update `leave` SET Status = %s WHERE L_Id = %s "
    mark = (Status,L_Id)
    cursor.execute(marking,mark)
    mydb.commit()
    print(" -------------Status was updated successfully.-------------")

if __name__ : "__main__"
while True:
    print("-------------Human Resource Management System (HRMS)-----------------")
    print("\n Welcome !")
    print("\n If You Are New employee Please add your details Here by clicking \"Yes\"")
    print( "\n If already a Registered employee continue clicking \"No\" ")
    print("\n If you are a HR click \"HR\"")

    click = input("Continue Clicking Here :- ")

    if click == "Yes":
        print("-----------We warmily Welcome you in our Ntech Institute.-------")
        E_Id = input("Enter any Number :- ")
        F_Name = input ("Insert your First Name :-") 
        M_Name = input ("Insert your Middle Name :-") 
        L_Name = input ("Insert your Last Name :-")
        DOB    = input("Enter the date of birth (YYYY-MM-DD) :-")
        Address = input("Enter your Current Address :-")
        Email_Address = input("Enter the correct email address :-")
        Contact_no = input("Enter your Whatsapp number :-")
        Joining_date = input("Enter your date of joining:-")
        Designation = input("Enter your Designation:-")
        Department = input("Enter your Department:-")
        Salary = input("Enter your Salary for now:-")
        add_employee(E_Id,F_Name,M_Name,L_Name,DOB,Address,Email_Address,Contact_no,Joining_date,Designation,Department,Salary)

    elif click == "No":
        print(" --------------To write a new leave continue by writing \"New\"--------------.")
        print("-------------- To check the Status of the leave continue by writing \"Old\"--------------. ")

        Enter = input("Continue Clicking here :- ")
        if Enter == "New":
               F_Name = input("Enter your First Name :-")
               L_Name = input("Enter your Last Name:-")
               Reason = input("Enter your Reason for a leave:-")
               From_date = input("Starting Date of leave(YYYY-MM-DD) :-")
               To_date = input("Ending Day of Leave(YYYY-MM-DD) :-")
               Days = input("Calculate and enter the Days :-")
               leave(F_Name,L_Name,Reason,From_date,To_date,Days)

        elif Enter == "Old":
            view_leave()

        else:
            exit()

    elif click =="HR":
        print("--------------Enter your Username--------------.")
        Name = input("Enter your UserName :-")

        if Name == "Ronald":
            print("--------------Now Enter your Password --------------")
            Password = input("Write Password Here :-")
            if Password == "Dsouza":
             while True:
                print("\n For viewing employee Details Type 1 :-")
                print("For marking the Attendance Type 2 :-")
                print("To View Attendance record  Type 3 :-")
                print("To Insert Salary details which has been paid  Type 4 :-")
                print("To View Salary record which has been paid  Type 5 :-")
                print("To View Leave Request of employee Type 6 :-")
                print("To Update Leave Request Status Type 7 :-")
                print("To Exit Type 8 :-")

                type = int(input("Type here :- " ))

                if type == 1:
                    E_Id = input("Enter Employee Id :-")
                    view_employees(E_Id)

                elif type == 2 :
                    F_name = input("\n First Name :- ")
                    L_Name = input("\n Last Name :-")
                    Date = input("\n Date(YYYY-MM-DD) :-")
                    Attendance = input("\n ark P/A/L :-")
                    attendance(F_name,L_Name,Date,Attendance)

                elif type == 3 :
                    F_Name = input("First Name :- ")
                    L_Name = input("Last Name :-")
                    view_attendance(F_Name,L_Name)

                elif type == 4 :
                    F_name = input("First Name :- ")
                    L_Name = input("Last Name :-")
                    Payment_date = input("Date of payment(YYYY-MM-DD):-")
                    Amount = input("Salary amount:-")
                    salary(F_name,L_Name,Payment_date,Amount)

                elif type == 5 :
                    F_name = input("First Name :- ")
                    L_Name = input("Last Name :-")
                    salary_view(F_name,L_Name)

                elif type == 6 :
                    view_leave()

                elif type == 7 :
                   L_Id = input("Enter the leave id :-")
                   Status = input("Enter the status :-")
                   Update_leave(L_Id,Status)

                
                elif type == 8:
                        print("Returning to the main menu.")
                        break  # Exit the HR menu loop and return to the main menu

                else:
                        print("Invalid option. Please choose again.")
            else:
                print("Incorrect password. Returning to the main menu.")

        else:
            print("Unauthorized access. Returning to the main menu.")

    elif click.lower() == "exit":
        print("Exiting the program.")
        break  # Exit the main loop

    else:
        print("Invalid option. Please choose 'Yes', 'No', 'HR ', or 'Exit'.")                        
                 

                    

                    
                      


        
    

            




