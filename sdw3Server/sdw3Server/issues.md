#1 BE + DB
Create Backend Models for every data point that needs to be stored or captured.

- [ ] Must follow relational db rules up to at least 2nd normal form.
- [ ] Must handle all data needed for storing every data point as listed below:

- [ ] Past/Current Semester Data:
  - [ ] Taught Courses
    - [ ] Max Number of students registered
    - [ ] Info of each student independent of PII(anonymous data capture)
      - [ ] Earned Grade
      - [ ] Dropped?
      - [ ] Added From waitlist?
      - [ ] Major
      - [ ] Sub-Program
      - [ ] Student Year (i.e freshmen)
      - [ ] Students Track
      - [ ] Catalog year/ Degree code
    - [ ] Room Taught in
    - [ ] Section num
    - [ ] Taught by
    - [ ] year
    - [ ] Semester
    - [ ] start time
    - [ ] end time
    - [ ] max waitlist
    - [ ] Course id
    - [ ] Online/Campus/Hybrid
    - [ ] sub program if a part of one
  - [ ] Info on preferences past and present:
    - [ ] Instructor name
    - [ ] preferred times taught per day
    - [ ] preferred days to teach
    - [ ] preferred courses to teach
    - [ ] preferred number of credits to teach
    - [ ] Semester for info
    - [ ] year for info
    - [ ] preferred room type
    - [ ] preferred rooms w/ weight
- [ ] A Table to store prereq relations

#2 BE+ DB
Backend serializers for the various models
each model may not need a serializer some models may be combined when converting to json
and others may need to be split up. We need to consult the frontend development to determine that.
We must get mockups for the various views needed for setting up scheduling: #1 https://github.com/BYUI-CIT-Internship/SDW3-client/issues/1
With the mock view in mind: https://docs.google.com/spreadsheets/d/10OM5KaCJ9Bh6zy6GX_a53J2qRkAKvkDPDP8xkO1pViA/edit?usp=sharing
Determine how to best send the serialized JSON to the Front end


#1 FE
Mock up views for scheduling application
Front end (visual) Requirments:
- [ ] must be sortable
- [ ] must dynamically update on the fly
- [ ] must be editable(with safeguards)
- [ ] must conform to mock views approved by stake holders
- [ ] must have be printable
  - [ ] may work out of box if printing webpage works w/o modification
- [ ] must be searchable
- [ ] 