from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
# 1. College of Sciences
# 2. College of Engineering
# 3. College of Education
# 4. College of Business
# 5. College of Arts and Humanities
# 6. College of Nursing
# 7. College of Technology
# 8. College of Agriculture
admin.site.register(Program)
# 1. Bachelor of Science in Computer Science
# 2. Bachelor of Science in Information Technology
# 3. Bachelor of Science in Mathematics
# 4. Bachelor of Science in Civil Engineering
# 5. Bachelor of Science in Electrical Engineering
# 6. Bachelor of Elementary Education
# 7. Bachelor of Secondary Education
# 8. Bachelor of Science in Business Administration
# 9. Bachelor of Science in Nursing
# 10. Bachelor of Science in Agriculture
admin.site.register(Organization)
# 1. ACS
# 2. SITE
admin.site.register(Student)
# Example Student 1:
# Student ID: 202280080
# Last Name: Apilan
# First Name: Mary Mae
# Middle Name: M.
#
# Example Student 2:
# Student ID: 202330198
# Last Name: Bendanillo
# First Name: Irene
# Middle Name: c.
admin.site.register(OrgMember)
# Mary Mae Apilan -> ACS
# Irene Bendanillo -> SITE