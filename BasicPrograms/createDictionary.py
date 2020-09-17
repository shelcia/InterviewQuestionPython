# TO CREATE DICTIONARY

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

stud_names = {0: "sara"}
stud_names[1] = "kokila"
stud_names[2] = "shellu"
print(stud_names)
del stud_names[1]
print(stud_names)
print("length %d" % len(stud_names))
stud_names[1] = "kokila"
stud_names[3] = "bala"
stud_names[4] = "mouse"
print(stud_names)
print("length %d" % len(stud_names))
print(sorted(stud_names))
