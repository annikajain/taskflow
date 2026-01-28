from datetime import datetime

class Task:
    def __init__(self, name, deadline, importance):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.importance = importance

    def priority_score(self):
        days_left = (self.deadline - datetime.now()).days
        return self.importance * max(1, 10 - days_left)

tasks = []

def add_task(name, deadline, importance):
    tasks.append(Task(name, deadline, importance))

add_task("Finish math homework", "2026-02-05", 4)
add_task("Prepare debate speech", "2026-02-02", 5)

tasks.sort(key=lambda t: t.priority_score(), reverse=True)

for task in tasks:
    print(task.name, "-", task.priority_score())
