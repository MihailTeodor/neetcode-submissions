class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cur_student = 0
        cur_sandwich = 0
        head_of_queue = 0
        ignore_head = True
        hungry_students = len(students)

        while True:

            if cur_student == head_of_queue:
                if ignore_head == False:
                    return hungry_students
                else:
                    ignore_head = False

            if students[cur_student] == sandwiches[cur_sandwich]:
                students[cur_student] = -1
                sandwiches[cur_sandwich] = -1
                hungry_students -= 1
                if hungry_students == 0:
                    return hungry_students

                while students[cur_student] == -1:
                    cur_student = (cur_student + 1) % len(students)
                
                head_of_queue = cur_student       
                ignore_head = True         

                while sandwiches[cur_sandwich] == -1:
                    cur_sandwich = (cur_sandwich + 1) % len(sandwiches)
            else:
                cur_student = (cur_student + 1) % len(students)
