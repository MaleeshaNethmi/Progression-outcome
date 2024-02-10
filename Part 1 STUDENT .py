#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID:1953838
#Date :2022/11/18

student_id=(input("Enter your StudentID : "))
def main_program():   
    def get_input(user_input,input_error,invalid_value):
        credit_range=range(0,140,20) 
        while True:
            try:
                value = int(input(user_input))#check if the values are entered as integer
            except ValueError:
                print(input_error)#if not print the error 
                continue
            else:
                if not value in credit_range:#check if the values entered are in the credit_range
                    print(invalid_value) 
                    continue
            break
        return value

    pass_credits = get_input("Please enter your credits at pass: ","Integer required.","Out of range.")#get input data to the pass credits
    defer_credits = get_input("Please enter your credits at defer: ","Integer required.","Out of range.")#get input data to the defer credits
    fail = get_input("Please enter your credit at fail: ","Integer required.","Out of range.")#get input data to the fail


    total_credits = 0
    total_credits = pass_credits + defer_credits + fail#calculate the total
 

    if total_credits != 120:#check if the values entered are equal to 120
      print("Total incorrect.")
      return main_program()#if not user has to input again

    elif pass_credits == 120:#student's pass credits equal to 120 is Progress:                                                                                                                                               
      print("Progress") 

    elif pass_credits == 100:#student's pass credits equal to 100 is Progress(module trailer)
      print("Progress(module trailer)")

    elif fail >= 80:#student's fail credits equal or greater than to 80 is Exclude
      print ("Exclude")

    else:
        print("Do not progress - module retriever")

main_program()    


