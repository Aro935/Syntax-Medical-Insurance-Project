# Great job! In this project, you used control flow in your code – using if, elif, and else statements – to provide advice on how individuals can lower their medical insurance costs.

# As a data scientist, it’s important to have an understanding of control flow as you’ll eventually work with and build complex decision tree algorithms. You are now better equipped to move forward in your data science journey!

# If you’d like additional practice on control flow, here are some ways you might extend this project:

#    Use try and except statements to build error control into your code.
#    In your analyze_bmi() function, notify the individual how much they need to lower their BMI to bring it to a normal weight range.
#    Create a new function or code block that utilizes control flow in some way – feel free to experiment!

#Happy coding!

# Smoker function
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# BMI function
def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + " Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = "Keanu's", age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

your_insurance_cost = estimate_insurance_cost(name = 'Your', age = 27, sex = 1, bmi = 20, num_of_children = 1, smoker = 0)

rando_insurance_cost = estimate_insurance_cost(name = "Rando's", age = 18, sex = 1, bmi = 18.4, num_of_children = 0, smoker = 0)