def simple_calculator():
	while True:
		First_Number = int(input("Input your first number: "))
		Second_Number = int(input("Input your second Number: "))
		print("Choose the Calculation you want")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		Choice = int(input("Input 1-4: "))
		if Choice == 1:
			print(First_Number, "+", Second_Number, "=", First_Number + Second_Number)
		elif Choice == 2:
			print(First_Number, "-", Second_Number, "=", First_Number - Second_Number)
		elif Choice == 3: 
			print(First_Number, "*", Second_Number, "=", First_Number * Second_Number)
		elif Choice == 4:
			print(First_Number, "/", Second_Number, "=", First_Number / Second_Number)
		else: print("Invalid choice")
		print("Do you wish to make another calculation ?: ")
		print("1. Yes")
		print("2. No")
		answer = int(input(""))
		
		if answer == 1:
			simple_calculator()
		elif answer == 2: 
			break 
		else: print("Invalid choice")
		
simple_calculator()
			
			
			
			
		
		