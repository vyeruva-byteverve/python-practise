############# Print Function ###################
 
## The print() fnction is a built-in function. It prints/outputs a specified message to the screen/console window.
## Built-in functions, contrary to user-defined functions, are always available and don't have to be imported.
## Python Built-in function list https://docs.python.org/3/library/functions.html
## To call a function (Function Invocatin or Function Call), need to use the function name followed by parentheses.

print ()
print ("Hello World!.")

## Python strings are delimited with quotes 
#
# double quotes
print("I am a string.")
# single quotes
print ("I am a string, too")


# Positional Arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputeed after the second, etc.
# The print() function can take multiple values, separated by commas.
# We can pass arguments into function by placing then inside the parantheses and must seperate arguments with a comma.
# These values are called positional arguments because Python decides how to print them based on the position they appear in.
print("Hello", "world!")

# There is a space added automatically between "Hello" and "World". This space is added because they are two separate positional arguments


#In Python strings the backslash (\) is a special character has a different meaning.
#Ex: \n - the new line character, start a new output line
print("a\n","b")


# Keyword arguments are the ones whose meaning is dictated by thier location, but by a special keyword used to identify them.
# The "end" and "sep" parameters can be used for formatting the output of the print() function.

# end parameter
# The end parameter sepecifies what to print at the end of print statement
print("1","2","3")
print("1","2","3", end=" ")
print("4")

# sep parameter (seperator)
# The "sep" parameter specifies the seperator between the outputted arguments
print("1","2","3", sep="_")

print("1","2","3", sep="_", end="")
print("4",sep="_",end="")
print("a")



# ex: expected output Programming***Essentials***in...Python
print("Programming","Essentials","in",sep="***",end="...")
print ("python")

# print arrow
print("     *")
print("   *   *")
print("  *     *")
print(" *       *")
print("***     ***")
print("  *     * ")
print("  *     * ")
print("  *******")

# minimize no. of print() function
print("      *\n","   *   *\n","  *     *\n"," *       *\n","***     ***\n","  *     * \n","  *     * \n","  *******")

# The above code works, but it adds an extra space at the beginning of every line because of the way youwe're using commas inside print() (comma inserts a space automatically).
# To fix this and print the shape correctly with only one print(), use either triple-quoted string or string concatenation.

print("""
     *
   *   *
  *     *
 *       *
***     ***
  *     *
  *     *
  *******
""")


# Why do we use triple quotes (""")?
# Because triple-quoted strings allow multi-line text without needing: multiple print() statements, \n escape sequences, string concatenation

print (""" 
       The
        Triple quotes
         DO NOT
          create
           more
            print statements""")
# We still have ONE print(), inside it, we have a multiple line string and python prints it as is

