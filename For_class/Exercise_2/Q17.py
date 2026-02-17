'''7. Grading of Steel
A certain grade of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are assigned as follows:
• Grade 10: All three conditions are satisfied
• Grade 9: Conditions (i) and (ii) are satisfied
• Grade 8: Conditions (ii) and (iii) are satisfied
• Grade 7: Conditions (i) and (iii) are satisfied
• Grade 6: Only one condition is satisfied
• Grade 5: None of the conditions are satisfied
Write a program that takes as input the hardness, carbon content, and tensile strength of
the steel and prints the grade of the steel.'''

hardness = int(input("Enter the hardness of the Steel"))
carbon_content = float(input("Enter the Carbon content of the Steel"))
tensile_strength = int(input("Enter the tensile_strength of the Steel"))
if hardness > 50 and carbon_content < 0.7 and tensile_strength > 5600:
    print("Grade 10")
elif hardness > 50 and carbon_content < 0.7:
    print("Grade 9")
elif carbon_content < 0.7 and tensile_strength > 5600:
    print("Grade 8")
elif hardness > 50 and tensile_strength > 5600:
    print("Grade 7")
elif hardness > 50 or carbon_content < 0.7 or tensile_strength > 5600:
    print("Grade 6")
else:
    print("Grade 5")