

def create_outline():
    outline = {"Introduction to Python", "Tools of the Trade", "How to make decisions",  "How to repeat code", "How to structure data", "Functions", "Modules"}
    problems = {"Introduction to Python": ('Problem 1', 'Problem 2', 'Problem 3'),
    "Tools of the Trade": ('Problem 1', 'Problem 2', 'Problem 3'), 
    "How to make decisions" : ('Problem 1', 'Problem 2', 'Problem 3'),
    "How to repeat code": ('Problem 1', 'Problem 2', 'Problem 3'),
    "How to structure data": ('Problem 1', 'Problem 2', 'Problem 3'),
    "Functions": ('Problem 1', 'Problem 2', 'Problem 3'),
    "Modules": ('Problem 1', 'Problem 2', 'Problem 3'),}
    
    olist = sorted(outline)
    x = 1
    for elements in olist:
        print('Course Topics:\n' * x + '* ' + elements)
        x = x -1
    x = 1
    for course in problems:
        print("Problems:\n" * x  + '* ' + course + " : " + problems[course][0] + ", " + problems[course][1] + ", " + problems[course][2])
        x = x - 1
    x = 1
    print("Student Progress:")
    status_list = ["STARTED", "GRADED", "COMPLETED"]
    student_1 = ("1.", "Fluffy","Tools of the trade", "Problem 2", status_list[0])
    student_2 = ("2.", "Weasel", "Modules", "Problem 3", status_list[2])
    student_3 = ("3.", "Jenkins", "Functions", "Problem 1", status_list[1])
    student_4 = ("4.", "Hoops", "Functions", "Problem 1", status_list[2])
    student_5 = ("5.", "Potatoe", "How to repeat code", "Problem 2", status_list[0])
    student_list = [student_1, student_2, student_3, student_4, student_5]
    student_list.sort(key=lambda e: e[4], reverse=True)
    for number, name, topic, problem, status in student_list:
        print("{} {} - {} - {} [{}]".format(number, name, topic, problem, status))
    return
if __name__ == "__main__":
    create_outline()
