age = 30
is_student = False
has_experience = True
is_eligible = (age >= 25) and (not is_student or has_experience)
print("Eligibility =", is_eligible)
