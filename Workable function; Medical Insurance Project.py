# Failed task 13: Congratulations! In this project, you created a useful function that calculates medical insurance costs based on the values passed into the function. Great job!

# As a data scientist, you should always strive to make your code more clean and modular. Using functions to avoid repetitive code is a great way to do just that.

# Now it’s your turn! If you’d like extra practice with Python functions, here are some suggestions to get you started:

# Modify the calculate_insurance_cost() function so that it returns two values – the output message and the estimated cost.

# Create a second function to calculate the difference between the insurance costs (given as inputs) of any two individuals and print a statement saying: "The difference in insurance cost is xxx dollars."

# Happy coding!

 

# Create calculate_insurance_cost() function below:

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):

  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

  print("The esitmated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")

  return estimated_cost

 

# Insurance cost difference

def calculate_diff_insurance_cost(person1, person2):

  #list must be in this order: name, age, sex, bmi, children, smoker

  estimated_cost_p1 = 250*person1[1] - 128*person1[2] + 370*person1[3] + 425*person1[4] + 24000*person1[5] - 12500

  estimated_cost_p2 = 250*person2[1] - 128*person2[2] + 370*person2[3] + 425*person2[4] + 24000*person2[5] - 12500

  diff_cost = estimated_cost_p2 - estimated_cost_p1

  print("The difference in insurance cost is " + str(diff_cost) + " dollars.")

  return diff_cost

 

# Estimate Maria's insurance cost

maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

 

# Estimate Omar's insurance cost

omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

 

# My estimate

your_insurance_cost = calculate_insurance_cost(name = "you", age = 27, sex = 1, bmi = 22.2, num_of_children = 1, smoker = 0)

 
omar = ['omar', 35, 1, 22.2, 0, 1]
 
you=['you',27,1,22.2,1,0]

maria=['maria',28,0,26.2,3,0]

print(calculate_diff_insurance_cost(you, maria))
print(calculate_diff_insurance_cost(maria, omar))
print(calculate_diff_insurance_cost(you, omar))