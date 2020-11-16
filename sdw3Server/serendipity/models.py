from django.db import models

# Create your models here.

#Course Class
#ID uq NN UQ
#min credits
#max credits
#course description
#course title
#course prefix
#course code
class Course (models.Model):
    min_credits = models.PositiveSmallIntegerField()
    max_credits = models.PositiveSmallIntegerField()
    course_description = models.TextField()
    course_title = models.CharField(max_length=100)
    course_prefix = models.CharField(max_length=10)
    course_code = models.CharField(max_length=8)

#course req. 
#id pk
#req course id id of req course
#course id id of course that requires above course
class Course_requirements(models.Model):
    required_course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='required')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')

#Degree info class
#Do you need to know the specific degree code?
#Id pk nn uq ai
#degree NN UQ varchar 45
#degree Acronym varchar 10
#degree code?
class Degree(models.Model):
    degree_name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=10)


#Catalog Year Info
#catalog id pk nn ai
#degree NN fk refrences degree table id row
#year Year
class Catalog_year_info(models.Model):
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)


#Tracks
#id pk nn uq ai
#first Semester nn
#second semester 
class Tracks(models.Model):
    first_semester = models.CharField(max_length=10)
    second_semester = models.CharField(max_length=10)

#building
#id
#building name
#building Acronym
class Building(models.Model):
    building_name = models.CharField(max_length=80)
    building_acronym = models.CharField(max_length=25)


#table Arrangment
#id pk
#table arrangment : pods /Rows as first two values
class Table_Arrangment(models.Model):
    arrangment = models.CharField(max_length=25)

#rooms
#all info needed about rooms
#room id pk
#Room number
#building code dafaults: STC's ID
#max Capacity
#Table Arrangment
class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    building = models.ForeignKey(Building, models.RESTRICT)
    max_capacity = models.PositiveSmallIntegerField()
    table_arrangment = models.ForeignKey(Table_Arrangment, models.RESTRICT)




#sub program
#id
#sub program varchar 45
class Sub_Program(models.Model):
    sub_program = models.CharField(max_length=80)

#days
#Full name of each weekday
#id 
#day
class Days(models.Model):
    day = models.CharField(max_length=15)

#semester, only used for db validation
#id
#semester name, values are Spring Summer Fall Winter
class Semester(models.Model):
    semester_name = models.CharField(max_length=20)


#location
#id pk
#location (on-campus/online)
class Location(models.Model):
    location = models.CharField(max_length=50)

#faculty info
#id
#first name
#last name
#middle name
#location
class Faculty (models.Model):
    first_name = models.CharField(max_length=80)
    last_name= models.CharField(max_length=80)
    middle_name = models.CharField(blank=True,max_length=80,null=True)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)


#section info
#section id pk
#course id
#section num int tiny
#instructor id -> faculty(id)
#sub program id -> Subprogram(id)
#max registration - the maximum number of students that may register
#max waitlist- the max number of students on the waitlist
#waitlist - the number on the waitlist
#students registered - the number of students registered
#location id -> room(id)
#start time TIME
#end time TIME
#semester id
#year YEAR
class Section_info(models.Model):
    course_id = models.ForeignKey(Course, models.RESTRICT)
    section_num = models.PositiveSmallIntegerField()
    instructor_id = models.ForeignKey(Faculty, models.RESTRICT)
    max_registration = models.PositiveSmallIntegerField()
    max_waitlist = models.PositiveSmallIntegerField()
    students_registered = models.PositiveSmallIntegerField()
    waitlist = models.PositiveSmallIntegerField()
    students_registered = models.PositiveSmallIntegerField()
    location_id = models.ForeignKey(Room,on_delete=models.RESTRICT)
    start_time = models.TimeField()
    end_time = models.TimeField()
    semester_id = models.ForeignKey(Semester, on_delete=models.RESTRICT)
    year = models.DateField(auto_now=False, auto_now_add=False)
    sub_program_id = models.ForeignKey(Sub_Program, blank=True,null=True, on_delete=models.RESTRICT)


#day of week
#used for scheduling of on campus classes
#multiple days of week entries to each one section
#id pk
#day id -> days(id)
#section id -> section_info(id)
class DayOfTheWeek(models.Model):
    day_id = models.ForeignKey(Days, on_delete=models.RESTRICT)
    section_id = models.ForeignKey(Section_info, on_delete=models.RESTRICT)



#student year
#id
#student year: freshman, sophmore, junior, senior
class Student_Year(models.Model):
    student_year = models.CharField(max_length=20)

#enrollment data
#course section id -> section(id)
#student degree
#subprogram id -> subprogram(id)
#location (remote/on campus)
#student catalog year
#end of course status (percent with decimal) float
#student year id -student year(id)
#from waitlist? bool
#dropped bool
class Enrollment_Data(models.Model):
    course_section_id = models.ForeignKey(Section_info, on_delete=models.RESTRICT)
    student_degree = models.ForeignKey(Degree, on_delete=models.RESTRICT)
    sub_program = models.ForeignKey(Sub_Program, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    end_of_course_status = models.DecimalField(max_digits=7, decimal_places=4)
    student_year = models.ForeignKey(Student_Year, on_delete=models.RESTRICT)
    from_waitlist = models.BooleanField()
    dropped = models.BooleanField()

#faculty location info
#id
#location online/campus


#preferred Courses
#id
#faculty id
#course id
#weight
#semester id
#year
class Preferred_Courses(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)

#preferred credits
#id
#faculty id
#semester id
#year
#preferred credit amount
class Preferred_Credits(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)
    credit_amount = models.PositiveSmallIntegerField()

#pref. days
#id
#day fk
#faculty id fk
#semester fk
#year
class Preferred_Days(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)
    day = models.ForeignKey(Days, on_delete=models.CASCADE)

#pref. rooms
#id
#faculty id fk
#room id fk
#weight
#semester fk
#year
class Preferred_Rooms(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()


#pref. semester
#id
#preferred semester fk
#faculty id fk
#year
class Preferred_Semester(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)
    weight = models.PositiveSmallIntegerField()


#pref times
#preferred day id fk
#preferred time start the preferred time to start teaching courses
#preferred time stop the preferred time to stop teaching courses
class Preferred_Times(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False, auto_now_add=False)
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    time_start = models.TimeField()
    time_end = models.TimeField()

