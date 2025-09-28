from faker import Faker
import random
import datetime

NUMBER_OF_LINES = 100

fake = Faker(['en_US'])

with open("data_set.csv", "w") as f:
    f.write("NAME,DESCRIPTION,COMPLETED,PRIORITY,DUE_DATE,CREATION_DATE\n") 
    for i in range(NUMBER_OF_LINES):
        name = fake.text(max_nb_chars=20)[:-1]
        description = fake.text(max_nb_chars=60)[:-1]
        completed = bool(random.getrandbits(1))
        priority = random.randint(1, 5)
        due_date = fake.date_time().strftime("%m/%d/%y %I:%M %p")
        completed_date = fake.date_time().strftime("%m/%d/%y %I:%M %p")

        f.write(name + "," + description + "," + str(completed) + "," + str(priority) + "," + due_date + "," + completed_date + "\n") # [:-1] removes "." at the end of sentence