## medic-system

I've decided to create same project in different languages so i could figure out which one i like the most and the less.
The project is a simple health care REST API but with some minimum rules to make it looks like a real world project.


## languages

- java
- typescript
- python
- elixir


## requirement

- Must have JWT authentication
- Must be deployed somewhere
- Must have tests
- Must use the respective ORM of language's framework


## entities 

- patients
- doctors
- users
- exams


## Diagram

![diagram](https://github.com/TaylonSopeletto/medic-system/blob/main/images/diagram.jpg)


## business logic

- 1 to 1 relationship: user/doctor and user/patient.
- Many to many relationship: patient/doctor.
- Doctor users can change patient informations but patient users cant change doctor's information.

Created by TaylonSopeletto