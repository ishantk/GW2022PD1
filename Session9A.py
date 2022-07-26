class GoogleTask:

    def __init__(self, title="", task="", dateTime=""):
        self.title = title
        self.task = task
        self.dateTime = dateTime


class GoogleTaskApp:

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)


task_app = GoogleTaskApp()
print(task_app, task_app.__dict__)


task1 = GoogleTask()
task2 = GoogleTask(title="Call My Mom", task="Call up at 7 PM IST", dateTime="26th July, 2022")

task3 = task1

print(task1, task1.__dict__)
print(task2, task2.__dict__)
print(task3, task3.__dict__)

task_app.add_task(task1)
task_app.add_task(task2)

print(task_app, task_app.__dict__)



