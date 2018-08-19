from locust import HttpLocust, TaskSet, task
import random,time

class UserBehavior(TaskSet):

    @task
    def index(self):
        response = self.client.get("/")
        print(response.content)



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'https://www.google.co.kr'
    min_wait = 0
    max_wait = 2000

if __name__ == '__main__':
    WebsiteUser().run()