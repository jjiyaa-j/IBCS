def seq_search(student,students,grades):
    index = 0

    while index < len(students):
        if students[index] == student:
            return grades[index]
        index += 1

    return -1

students = ['Alissa','Ben','Charlie','Dianna']
grades = ['B','D','B','A']
print (seq_search('Dianna',students,grades))