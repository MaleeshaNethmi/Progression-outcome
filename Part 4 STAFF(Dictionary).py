#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID:1953838
#Date :2022/11/18

credit={} #open dictionary
def main_program():
    student_ID = input("Enter student ID: ") #get student ID
    credit_range=range(0,140,20)
    def return_the_program(): 
        def get_input(user_input,input_error,invalid_value): 
            while True:
                try:
                    value = int(input(user_input))  #check if the values are entered as integer
                except ValueError:
                    print(input_error) #if not print the error
                    continue
                else:
                    if not value in credit_range: #check if the values entered are in the credit_range
                        print(invalid_value)
                        continue
                break
            return value
        
        pass_credits = get_input("Please enter your credits at pass: ","Integer required.","Out of range.") #get input data to the pass credits
        defer_credits = get_input("Please enter your credits at defer: ","Integer required.","Out of range.") #get input data to the defer credits
        fail = get_input("Please enter your credit at fail: ","Integer required.","Out of range.") #get input data to the fail


        total_credits = 0
        total_credits = pass_credits + defer_credits + fail #add input data to the list
        
        result= ""
        
        
        if total_credits != 120:  #check if the values entered are equal to 120
          print("Total incorrect.")
          return return_the_program()

        elif pass_credits == 120:#student's pass credits equal to 120 is Progress                                                                                                                                                
          print("Progress")
          result = " Progress - {0}, {1}, {2} ".format(pass_credits,defer_credits,fail) #format credits in to the placeholders
          
        elif pass_credits == 100:#student's pass credits equal to 100 is Progress(module trailer)
          print("Progress(module trailer)")
          result = " Progress(module trailer) - {0}, {1}, {2} ".format(pass_credits,defer_credits,fail)
        
        elif fail >= 80:#student's fail credits equal or greater than to 80 is Exclude
          print ("Exclude")
          result = " Exclude - {0}, {1}, {2} ".format(pass_credits,defer_credits,fail)
  
        else:
            print("Do not progress - module retriever")
            result = " Do not progress - module retriever - {0}, {1}, {2} ".format(pass_credits,defer_credits,fail)
        print()
        
        credit[student_ID] = result #add keys and values to the dictionary

        print("Would you like to enter another set of data?") 

        while True:
            choice = input("Enter 'y' for yes or'q' to quit and view results: ") #giving user the option of choosing to add another student records or choosing to display the dictionary

            print()
            if choice.lower() == "y" :
                main_program()
            elif choice.lower() == "q":
                for key, value in credit.items(): 
                    print(f"{key} :{value}",end = ' ') #print key and values in dictionary
            else:
                continue
            break
    return_the_program()
main_program()    

