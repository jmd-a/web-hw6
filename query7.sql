SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE subjects.name = '{subject_name}' AND groups.name = '{group_name}';
