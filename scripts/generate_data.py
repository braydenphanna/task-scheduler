from faker import Faker
import random
import datetime

def generate():
    NUMBER_OF_LINES = 1000

    fake = Faker(['en_US'])

    # fixed task list - can add more
    tasks_list = [
        "Check emails",
        "Join meeting",
        "Work on project",
        "Call client",
        "Submit assignment",
        "Team brainstorming",
        "Review report",
        "Update documentation",
        "Plan schedule",
        "Code review"
    ]

    with open("data_set.csv", "w") as f:
        f.write("ID,NAME,DESCRIPTION,COMPLETED,PRIORITY,DUE_DATE,CREATION_DATE\n")
        for i in range(NUMBER_OF_LINES):
            # pick a task from the fixed list
            name = random.choice(tasks_list)

            # description can still be random text
            description = fake.text(max_nb_chars=60)[:-1]

            # priority based on task type
            if name in ["Submit assignment", "Work on project"]:
                priority = random.randint(3, 5)  # high
            elif name in ["Join meeting", "Call client"]:
                priority = random.randint(1, 4)
            else:
                priority = random.randint(1, 3)  # low

            # completion probability based on priority
            if priority >= 4:
                completed = bool(random.random() < 0.85)
            elif priority >= 2:
                completed = bool(random.random() < 0.7)
            else:
                completed = bool(random.random() < 0.5)

            # Random due and creation dates
            creation_date = fake.past_datetime().strftime("%m/%d/%y %I:%M %p")
            due_date = fake.date_time_between_dates(datetime_start='now', datetime_end='+1yr').strftime("%m/%d/%y %I:%M %p")

            f.write(
                f"{i},{name},{description},{completed},{priority},{due_date},{creation_date}\n")

generate()