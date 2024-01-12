# Create first string variable
name = "Mike"
profession = "writer"

# Create variable containing integar
books_written = 6

#Concatenate and print out variables
output = name + " is a " + profession + " and he's written " + str(books_written) + " books. "
# This option below is the main way we will write our outputs.
output_2 = f"{name} is a {profession} and he's written {books_written} books."
print(output_2)