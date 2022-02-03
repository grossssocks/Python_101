#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.
#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2 
combined_name_lowercase = combined_name.lower()

t = combined_name_lowercase.count("t")
r = combined_name_lowercase.count("r")
u = combined_name_lowercase.count("u")
e = combined_name_lowercase.count("e")
true = t + r + u + e

l = combined_name_lowercase.count("l")
o = combined_name_lowercase.count("o")
v = combined_name_lowercase.count("v")
e = combined_name_lowercase.count("e")
love = l + o + v + e

score = str(true) + str(love) #is able to concatinate the variables together we need to apply str() 
score_as_int = int(score) #for avoiding str( and int())
if (score_as_int < 10) or (score_as_int > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score_as_int >= 40) and (score_as_int <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")
