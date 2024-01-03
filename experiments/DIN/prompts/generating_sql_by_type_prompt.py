from .few_shot_example_schema import *

easy_prompt = """
# Use the the schema links to generate the SQL queries for each of the questions.
"""+ \
few_shot_example_schema + \
"""
{schema}

Q: "Find the buildings which have rooms with capacity more than 50."
Schema_links: [classroom.building,classroom.capacity,50]
SQL: SELECT DISTINCT building FROM classroom WHERE capacity  >  50

Q: "Find the room number of the rooms which can sit 50 to 100 students and their buildings."
Schema_links: [classroom.building,classroom.room_number,classroom.capacity,50,100]
SQL: SELECT building ,  room_number FROM classroom WHERE capacity BETWEEN 50 AND 100

Q: "Give the name of the student in the History department with the most credits."
Schema_links: [student.name,student.dept_name,student.tot_cred,History]
SQL: SELECT name FROM student WHERE dept_name  =  'History' ORDER BY tot_cred DESC FETCH FIRST 1 ROWS ONLY

Q: "Find the total budgets of the Marketing or Finance department."
Schema_links: [department.budget,department.dept_name,Marketing,Finance]
SQL: SELECT sum(budget) FROM department WHERE dept_name  =  'Marketing' OR dept_name  =  'Finance'

Q: "Find the department name of the instructor whose name contains 'Soisalon'."
Schema_links: [instructor.dept_name,instructor.name,Soisalon]
SQL: SELECT dept_name FROM instructor WHERE name LIKE '%Soisalon%'

Q: "What is the name of the department with the most credits?"
Schema_links: [course.dept_name,course.credits]
SQL: SELECT dept_name FROM course GROUP BY dept_name ORDER BY sum(credits) DESC FETCH FIRST 1 ROWS ONLY

Q: "How many instructors teach a course in the Spring of 2010?"
Schema_links: [teaches.ID,teaches.semester,teaches.YEAR,Spring,2010]
SQL: SELECT COUNT (DISTINCT ID) FROM teaches WHERE semester  =  'Spring' AND YEAR  =  2010

Q: "Find the name of the students and their department names sorted by their total credits in ascending order."
Schema_links: [student.name,student.dept_name,student.tot_cred]
SQL: SELECT name ,  dept_name FROM student ORDER BY tot_cred

Q: "Find the year which offers the largest number of courses."
Schema_links: [SECTION.YEAR,SECTION.*]
SQL: SELECT YEAR FROM SECTION GROUP BY YEAR ORDER BY count(*) DESC FETCH FIRST 1 ROWS ONLY

Q: "What are the names and average salaries for departments with average salary higher than 42000?"
Schema_links: [instructor.dept_name,instructor.salary,42000]
SQL: SELECT dept_name ,  AVG (salary) FROM instructor GROUP BY dept_name HAVING AVG (salary)  >  42000

Q: "How many rooms in each building have a capacity of over 50?"
Schema_links: [classroom.*,classroom.building,classroom.capacity,50]
SQL: SELECT count(*) ,  building FROM classroom WHERE capacity  >  50 GROUP BY building

Q: "Find the names of the top 3 departments that provide the largest amount of courses?"
Schema_links: [course.dept_name,course.*]
SQL: SELECT dept_name FROM course GROUP BY dept_name ORDER BY count(*) DESC FETCH FIRST 3 ROWS ONLY

Q: "Find the maximum and average capacity among rooms in each building."
Schema_links: [classroom.building,classroom.capacity]
SQL: SELECT max(capacity) ,  avg(capacity) ,  building FROM classroom GROUP BY building

Q: "Find the title of the course that is offered by more than one department."
Schema_links: [course.title]
SQL: SELECT title FROM course GROUP BY title HAVING count(*)  >  1

Q: {question}
Schema_links: {schema_links}
"""


medium_prompt = """
# Use the the schema links and Intermediate_representation to generate the SQL queries for each of the questions.
"""+ \
few_shot_example_schema + \
few_shot_example_fk + \
"""
{schema}
Foreign_keys = {foreign_keys}

Q: "Find the total budgets of the Marketing or Finance department."
Schema_links: [department.budget,department.dept_name,Marketing,Finance]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = []. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: select sum(department.budget) from department  where  department.dept_name = \"Marketing\"  or  department.dept_name = \"Finance\"
SQL: SELECT sum(budget) FROM department WHERE dept_name  =  'Marketing' OR dept_name  =  'Finance'

Q: "Find the name and building of the department with the highest budget."
Schema_links: [department.budget,department.dept_name,department.building]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = []. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: select department.dept_name , department.building from department  order by department.budget desc limit 1
SQL: SELECT dept_name ,  building FROM department ORDER BY budget DESC FETCH FIRST 1 ROWS ONLY

Q: "What is the name and building of the departments whose budget is more than the average budget?"
Schema_links: [department.budget,department.dept_name,department.building]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = []. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation:  select department.dept_name , department.building from department  where  @.@ > avg ( department.budget ) 
SQL: SELECT dept_name ,  building FROM department WHERE budget  >  (SELECT avg(budget) FROM department)

Q: "Find the total number of students and total number of instructors for each department."
Schema_links: [department.dept_name = student.dept_name,student.id,department.dept_name = instructor.dept_name,instructor.id]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = [department,student,instructor]. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: "select count( distinct student.ID) , count( distinct instructor.ID) , department.dept_name from department  group by instructor.dept_name
SQL: SELECT count(DISTINCT T2.id) ,  count(DISTINCT T3.id) ,  T3.dept_name FROM department T1 JOIN student T2 ON T1.dept_name  =  T2.dept_name JOIN instructor AS T3 ON T1.dept_name  =  T3.dept_name GROUP BY T3.dept_name

Q: "Find the title of courses that have two prerequisites?"
Schema_links: [course.title,course.course_id = prereq.course_id]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = [course,prereq]. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: select course.title from course  where  count ( prereq.* )  = 2  group by prereq.course_id
SQL: SELECT T1.title FROM course T1 JOIN prereq T2 ON T1.course_id  =  T2.course_id GROUP BY T2.course_id HAVING count(*)  =  2

Q: "Find the name of students who took any class in the years of 2009 and 2010."
Schema_links: [student.name,student.id = takes.id,takes.YEAR,2009,2010]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = [student,takes]. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: select  distinct student.name from student  where  takes.year = 2009  or  takes.year = 2010
SQL: SELECT DISTINCT T1.name FROM student T1 JOIN takes T2 ON T1.id  =  T2.id WHERE T2.YEAR  =  2009 OR T2.YEAR  =  2010

Q: "list in alphabetic order all course names and their instructors' names in year 2008."
Schema_links: [course.title,course.course_id = teaches.course_id,teaches.id = instructor.id,instructor.name,teaches.year,2008]
A: Let’s think step by step. For creating the SQL for the given question, we need to join these tables = [course,teaches,instructor]. First, create an intermediate representation, then use it to construct the SQL query.
Intermediate_representation: select course.title , instructor.name from course  where  teaches.year = 2008  order by course.title asc
SQL: SELECT T1.title ,  T3.name FROM course T1 JOIN teaches T2 ON T1.course_id  =  T2.course_id JOIN instructor AS T3 ON T2.id  =  T3.id WHERE T2.YEAR  =  2008 ORDER BY T1.title

Q: {question}
Schema_links: {schema_links}
A: Let's think step by step. 
"""


hard_prompt = """
# Use the the schema links and Intermediate_representation to generate the SQL queries for each of the questions.
"""+ \
few_shot_example_schema + \
few_shot_example_fk + \
"""
{schema}
Foreign_keys = {foreign_keys}

Q: "Find the title of courses that have two prerequisites?"
Schema_links: [course.title,course.course_id = prereq.course_id]
A: Let's think step by step. "Find the title of courses that have two prerequisites?" can be solved by knowing the answer to the following sub-question "What are the titles for courses with two prerequisites?".
The SQL query for the sub-question "What are the titles for courses with two prerequisites?" is SELECT T1.title FROM course T1 JOIN prereq T2 ON T1.course_id  =  T2.course_id GROUP BY T2.course_id HAVING count(*)  =  2
So, the answer to the question "Find the title of courses that have two prerequisites?" is =
Intermediate_representation: select course.title from course  where  count ( prereq.* )  = 2  group by prereq.course_id
SQL: SELECT T1.title FROM course T1 JOIN prereq T2 ON T1.course_id  =  T2.course_id GROUP BY T2.course_id HAVING count(*)  =  2

Q: "Find the name and building of the department with the highest budget."
Schema_links: [department.dept_name,department.building,department.budget]
A: Let's think step by step. "Find the name and building of the department with the highest budget." can be solved by knowing the answer to the following sub-question "What is the department name and corresponding building for the department with the greatest budget?".
The SQL query for the sub-question "What is the department name and corresponding building for the department with the greatest budget?" is SELECT dept_name ,  building FROM department ORDER BY budget DESC FETCH FIRST 1 ROWS ONLY
So, the answer to the question "Find the name and building of the department with the highest budget." is =
Intermediate_representation: select department.dept_name , department.building from department  order by department.budget desc limit 1
SQL: SELECT dept_name ,  building FROM department ORDER BY budget DESC FETCH FIRST 1 ROWS ONLY

Q: "Find the title, credit, and department name of courses that have more than one prerequisites?"
Schema_links: [course.title,course.credits,course.dept_name,course.course_id = prereq.course_id]
A: Let's think step by step. "Find the title, credit, and department name of courses that have more than one prerequisites?" can be solved by knowing the answer to the following sub-question "What is the title, credit value, and department name for courses with more than one prerequisite?".
The SQL query for the sub-question "What is the title, credit value, and department name for courses with more than one prerequisite?" is SELECT T1.title ,  T1.credits , T1.dept_name FROM course T1 JOIN prereq T2 ON T1.course_id  =  T2.course_id GROUP BY T2.course_id HAVING count(*)  >  1
So, the answer to the question "Find the name and building of the department with the highest budget." is =
Intermediate_representation: select course.title , course.credits , course.dept_name from course  where  count ( prereq.* )  > 1  group by prereq.course_id 
SQL: SELECT T1.title ,  T1.credits , T1.dept_name FROM course T1 JOIN prereq T2 ON T1.course_id  =  T2.course_id GROUP BY T2.course_id HAVING count(*)  >  1

Q: "Give the name and building of the departments with greater than average budget."
Schema_links: [department.dept_name,department.building,department.budget]
A: Let's think step by step. "Give the name and building of the departments with greater than average budget." can be solved by knowing the answer to the following sub-question "What is the average budget of departments?".
The SQL query for the sub-question "What is the average budget of departments?" is SELECT avg(budget) FROM department
So, the answer to the question "Give the name and building of the departments with greater than average budget." is =
Intermediate_representation: select department.dept_name , department.building from department  where  @.@ > avg ( department.budget )
SQL: SELECT dept_name ,  building FROM department WHERE budget  >  (SELECT avg(budget) FROM department)

Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
Schema_links: [teaches.id,teaches.semester,teaches.YEAR,Fall,2009,Spring,2010]
A: Let's think step by step. "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010." can be solved by knowing the answer to the following sub-question "Find the id of instructors who taught a class in Spring 2010".
The SQL query for the sub-question "Find the id of instructors who taught a class in Spring 2010" is SELECT id FROM teaches WHERE semester  =  'Spring' AND YEAR  =  2010
So, the answer to the question "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010." is = 
Intermediate_representation: select teaches.ID from teaches  where  teaches.semester = \"Fall\"  and  teaches.year = 2009  and  teaches.semester != \"Spring\"  and  teaches.year = 2010 
SQL: SELECT id FROM teaches WHERE semester  =  'Fall' AND YEAR  =  2009 EXCEPT SELECT id FROM teaches WHERE semester  =  'Spring' AND YEAR  =  2010

Q: "Find the name of the courses that do not have any prerequisite?"
Schema_links: [course.title,course.course_id]
A: Let's think step by step. "Find the name of the courses that do not have any prerequisite?" can be solved by knowing the answer to the following sub-question "What are the courses that have any prerequisite?".
The SQL query for the sub-question "What are the courses that have any prerequisite?" is SELECT course_id FROM prereq
So, the answer to the question "Find the name of the courses that do not have any prerequisite?" is =
Intermediate_representation: select course.title from course  where  @.@ not in prereq.course_id 
SQL: SELECT title FROM course WHERE course_id NOT IN (SELECT course_id FROM prereq)

Q: "Find the salaries of all distinct instructors that are less than the largest salary."
Schema_links: [instructor.salary]
A: Let's think step by step. "Find the salaries of all distinct instructors that are less than the largest salary." can be solved by knowing the answer to the following sub-question "What is the largest salary of instructors".
The SQL query for the sub-question "What is the largest salary of instructors" is SELECT max(salary) FROM instructor
So, the answer to the question "Find the salaries of all distinct instructors that are less than the largest salary." is =
Intermediate_representation: select  distinct instructor.salary from instructor  where  @.@ < max ( instructor.salary )
SQL: SELECT DISTINCT salary FROM instructor WHERE salary  <  (SELECT max(salary) FROM instructor)

Q: "Find the names of students who have taken any course in the fall semester of year 2003."
Schema_links: [student.id,student.name,takes.id,takes.semester,fall,2003]
A: Let's think step by step. "Find the names of students who have taken any course in the fall semester of year 2003." can be solved by knowing the answer to the following sub-question "Find the students who have taken any course in the fall semester of year 2003.".
The SQL query for the sub-question "Find the students who have taken any course in the fall semester of year 2003." is SELECT id FROM takes WHERE semester  =  'Fall' AND YEAR  =  2003
So, the answer to the question "Find the names of students who have taken any course in the fall semester of year 2003." is =
Intermediate_representation: select student.name from student  where  takes.semester = \"Fall\"  and  takes.year = 2003
SQL: SELECT name FROM student WHERE id IN (SELECT id FROM takes WHERE semester  =  'Fall' AND YEAR  =  2003)

Q: "Find the minimum salary for the departments whose average salary is above the average payment of all instructors."
Schema_links: [instructor.salary,instructor.dept_name]
A: Let's think step by step. "Find the minimum salary for the departments whose average salary is above the average payment of all instructors." can be solved by knowing the answer to the following sub-question "What is the average payment of all instructors.".
The SQL query for the sub-question "What is the average payment of all instructors." is SELECT avg(salary) FROM instructor
So, the answer to the question "Find the minimum salary for the departments whose average salary is above the average payment of all instructors." is =
Intermediate_representation: select min(instructor.salary) , instructor.dept_name from instructor  where  avg ( instructor.salary )  > avg ( instructor.salary )   group by instructor.dept_name
SQL: SELECT min(salary) ,  dept_name FROM instructor GROUP BY dept_name HAVING avg(salary)  >  (SELECT avg(salary) FROM instructor)

Q: "What is the course title of the prerequisite of course Mobile Computing?"
Schema_links: [course.title,course.course_id = prereq.course_id,prereq.prereq_id,course.title,Mobile Computing]
A: Let's think step by step. "What is the course title of the prerequisite of course Mobile Computing?" can be solved by knowing the answer to the following sub-question "What are the ids of the prerequisite of course Mobile Computing?".
The SQL query for the sub-question "What are the ids of the prerequisite of course Mobile Computing?" is SSELECT T1.prereq_id FROM prereq T1 JOIN course T2 ON T1.course_id  =  T2.course_id WHERE T2.title  =  'Mobile Computing'
So, the answer to the question "What is the course title of the prerequisite of course Mobile Computing?" is =
Intermediate_representation: select course.title from course  where  @.@ in prereq.*  and  course.title = \"Mobile Computing\"
SQL: SELECT title FROM course WHERE course_id IN (SELECT T1.prereq_id FROM prereq T1 JOIN course T2 ON T1.course_id  =  T2.course_id WHERE T2.title  =  'Mobile Computing')

Q: "Give the title and credits for the course that is taught in the classroom with the greatest capacity."
Schema_links: [classroom.capacity,classroom.building = SECTION.building,classroom.room_number = SECTION.room_number,course.title,course.credits,course.course_id = SECTION.course_id]
A: Let's think step by step. "Give the title and credits for the course that is taught in the classroom with the greatest capacity." can be solved by knowing the answer to the following sub-question "What is the capacity of the largest room?".
The SQL query for the sub-question "What is the capacity of the largest room?" is (SELECT max(capacity) FROM classroom)
So, the answer to the question "Give the title and credits for the course that is taught in the classroom with the greatest capacity." is =
Intermediate_representation: select course.title , course.credits from classroom  order by classroom.capacity desc limit 1"
SQL: SELECT T3.title ,  T3.credits FROM classroom T1 JOIN SECTION T2 ON T1.building  =  T2.building AND T1.room_number  =  T2.room_number JOIN course AS T3 ON T2.course_id  =  T3.course_id WHERE T1.capacity  =  (SELECT max(capacity) FROM classroom)

Q: {question}
Schema_links: {schema_links}
A: Let's think step by step. {question} can be solved by knowing the answer to the following sub-question "{sub_questions}".
The SQL query for the sub-question"""

