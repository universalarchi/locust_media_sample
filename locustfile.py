from locust import HttpLocust, TaskSet, task
import random,time

class UserBehavior(TaskSet):

    @task
    def index(self):
        url = self.init_random_line()
        response = self.client.get(url, name=(url[:url.find("?")]))
        print(response.content)
        time.sleep(1.0)

    def on_start(self):
        print("on_start")

    def init_random_line(self):
        filesize = 89  # size of the really big file
        offset = random.randrange(filesize)
        f = open('test.csv')
        f.seek(offset)  # go to random position
        f.readline()  # discard - bound to be partial line
        random_line = f.readline()  # bingo!

        # extra to handle last/first line edge cases
        if len(random_line) == 0:  # we have hit the end
            f.seek(0)
            random_line = f.readline()  # so we'll grab the first line instead

        return random_line.splitlines()[0]


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://192.168.0.4:8080'
    min_wait = 0
    max_wait = 2000

if __name__ == '__main__':
    WebsiteUser().run()