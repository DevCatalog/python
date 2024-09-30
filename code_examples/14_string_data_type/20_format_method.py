name = "Brian"
age = 25
print("{} is {} years old.".format(name, age))
# Using index positions
print("{0} is {1} years old.".format(name, age))

# Assign keywords to placeholders
x = 5
y = 10
text = "The sum of {x} and {y} is {sum}."
print(text.format(x=x, y=y, sum=x+y))
