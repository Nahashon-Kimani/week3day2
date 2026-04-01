from locust import HttpUser, task

class User(HttpUser):
    @task
    def home(self):
        self.client.get("/")