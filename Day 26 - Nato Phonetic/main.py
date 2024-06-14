import random
import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row['letter']:row['code'] for (index,row) in data.iterrows()}

input_word = input("Please tell us the word for NATO Phoenetic: ")

# Create a list of codes corresponding to the input word
output_list = [phonetic_dict[char.upper()] for char in input_word if char.upper() in phonetic_dict]

print(output_list)


######---------Others----------------######
# numbers = [1,2,3]

# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# names = ['Alex','Beth','Caroline','Dave','Freddie','Eleanor','Gaurav']

# long_caps_name = [name.upper() for name in names if len(name)>5]

# print(long_caps_name)

# with open("file1.txt") as file1:
#   list1 = file1.readlines()
#   list1 = [item.rstrip('\n') for item in list1]
#   list1 = [int(item) for item in list1]

# with open("file2.txt") as file2:
#   list2 = file2.readlines()
#   list2 = [item.rstrip('\n') for item in list2]
#   list2 = [int(item) for item in list2]

# result = [item for item in list1 if (item in list2)]

# names = ['Alex','Beth','Caroline','Dave','Freddie','Eleanor','Gaurav']

# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# passed_students = {key:value for (key,value) in student_scores.items() if value > 60}
# print(passed_students)

# sentence = "This is a sample sentence."

# Split the sentence into a list of words
# words_list = sentence.split()

# result = {item:len(item) for item in words_list}

# print(result)  

##Reading the dataframe and loop through it
# passed_students = {
#     "student": ["Alex","Beth","Gaurav","Jeni"],
#     "scores": [80,67,93,45]
# }

# students_dataframe = pandas.DataFrame(passed_students)
# print(students_dataframe)

# for index,row in students_dataframe.iterrows():
#     print(row.scores)
    # if row.student == 'Gaurav':
    #     print(row.scores)