#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID:1953838
#Date :2022/11/18

Progress = []
Trailer = []
Retriever = []
Excluded = []
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

    def calculate_module_outcome():
        pass_credits = get_input("Please enter your credits at pass: ","Integer required.","Out of range.")#get input data to the pass credits
        defer_credits = get_input("Please enter your credits at defer: ","Integer required.","Out of range.")#get input data to the defer credits
        fail = get_input("Please enter your credit at fail: ","Integer required.","Out of range.")#get input data to the fail


        total_credits = 0
        total_credits = pass_credits + defer_credits + fail #calculate the total credits
     
        credit_data = [pass_credits, defer_credits, fail]#add input data to the list

        if total_credits != 120:#check if the values entered are equal to 120 
          print("Total incorrect.")
        elif pass_credits == 120:#student's pass credits equal to 120 is Progress                                                                                                                                              
          print("Progress")
          Progress.append(credit_data)#add data to the Progress
        elif pass_credits == 100:#student's pass credits equal to 100 is Progress(module trailer)
          print("Progress(module trailer)")
          Trailer.append(credit_data)#add data to the Trailer
        elif fail >= 80:#student's fail credits equal or greater than to 80 is Exclude
          print ("Exclude")
          Excluded.append(credit_data)#add data to the Exclude
        else:
            print("Do not progress - module retriever")
            Retriever.append(credit_data)#add data to the Retriever
        print()
        
    def print_histogram():#printing the histogram
        print("----------------------------------------------------------------------")
        print("Histogram")
        print("Progress",len(Progress)," :", "*" * len(Progress))
        print("Trailer",len(Trailer),"  :", "*" * len(Trailer))
        print("Retriever",len(Retriever),":", "*" * len(Retriever))
        print("Excluded",len(Excluded)," :", "*" * len(Excluded))
        print()
        total_outcomes = len(Progress) + len(Trailer) + len(Retriever) + len(Excluded)#total outcomes is calculated from the length of the lists
        print(total_outcomes, "outcomes in total.")
        print("----------------------------------------------------------------------")
   
    def print_module_data(list_name,list):   
        for item in list:
            pass_credit = item[0]
            defer_credit = item[1]
            fail = item[2]
            print(list_name,"-",pass_credit,",",defer_credit,",",fail)
            
    def print_data_list():
        print_module_data("Progress", Progress)#calling the print_module_data user defined function
        print_module_data("Progress (module trailer)", Trailer)
        print_module_data("Module retriever", Retriever)
        print_module_data("Exclude", Excluded)

    def write_module_data(list_name,list,file):  
        for item in list:
            pass_credit = str(item[0])
            defer_credit = str(item[1])
            fail = str(item[2])
            file_data = list_name + "-" + pass_credit + "," + defer_credit + "," + fail
            file.write("%s\n" % file_data )#writing file data to the text file
            
    def generate_text_file(): 
        print()
        name = input("you can create a file to save your progerssion data,\nEnter a name for the file:  ")#get file name
        file_name = (name+'.txt')#creat text file
        file = open(file_name, 'w')#open file in write mode
        file = open(file_name, 'a')#open file in append mode
        write_module_data("Progress", Progress,file)#calling write_module_data user defined function
        write_module_data("Progress (module trailer)", Trailer, file)
        write_module_data("Module retriever", Retriever, file)
        write_module_data("Excluded", Excluded, file)
        
        file.close()#file close
        print("Your data has been saved to the file.Thank You!")

    calculate_module_outcome()    
    print("Would you like to enter another set of data?")#asking for another set of data
    
    while True:
        choice = input("Enter 'y' for yes or'q' to quit and view results: ")#asking user input only for choice of 'y'to continue or 'q' to quit
        print()
        if choice.lower() == "y" :#giving user the option of choosing to add another student records
            main_program()
        elif choice.lower() == "q":#giving user the option of choosing to display histogram,list and create text file
            print_histogram()        
            print_data_list()#calling the user defined functions
            generate_text_file()     
        else:
            continue
        break
#main program 
main_program()    


