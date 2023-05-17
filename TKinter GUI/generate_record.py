import csv

headers = ["Student Name", "Anxiety / Depression Score", "Enthusiasm Score", "Optimism Score"]
student_list = [["Student1","50"], ["Student2","30"], ["Student3","90"],
                ["Student4","60"]]

with open("student_record.csv", "w") as stud:
    student = csv.writer(stud)
    student.writerow(headers)
    student.writerows(student_list)