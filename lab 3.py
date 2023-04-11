import datetime

import requests as requests


class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            print("Warning: Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class QueueOutOfRangeException(Exception):
    def __init__(self, message = "Queue is out of range"):
        self.message = message

    def __str__(self):
        return self.message


class QueueException(Queue):
    queues = []

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.items = []

    @classmethod
    def create_queue(cls, name, size):
        if cls.get_queue(name) is None:
            queue = QueueException(name, size)
            cls.queues.append(queue)
            return queue
        else:
            return cls.get_queue(name)

    @classmethod
    def get_queue(cls, name):
        for queue in cls.queues:
            if queue.name == name:
                return queue
        return None

    def insert(self, value):
        if len(self.items) < self.size:
            self.items.append(value)
        else:
            raise QueueOutOfRangeException

    def pop(self):
        if len(self.items) == 0:
            print("Warning: Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def save(self, name):
        file = open(name + ".txt", "w")
        for item in self.items:
            file.write(str(item) + "\n")
        file.close()

    def load(self, name):
        file = open(name + ".txt", "r")
        for line in file:
            self.items.append(int(line))
        file.close()


class Weather:
    def __init__(self, key):
        self.key = key

    def get_data(self, city, url="current", option=""):
        url = "http://api.weatherapi.com/v1/" + url + ".json?key=" + self.key + "&q=" + city + option
        response = requests.get(url)
        return response.json()

    def get_weather(self, city):
        data = self.get_data(city)
        return "temp_c: " + str(data['current']['temp_c']), "temp_f: " + str(data['current']['temp_f'])

    def get_temperature_after(self, city, days, hour=None):
        weather = self.get_data(city, "forecast", "&days=" + str(days))
        if hour is None:
            hour = 12
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        date = date.replace(hour=hour, minute=0, second=0, microsecond=0)
        for forecast in weather["forecast"]["forecastday"]:
            if forecast["date"] == date.strftime("%Y-%m-%d"):
                for hours in forecast["hour"]:
                    if hours["time"] == date.strftime("%Y-%m-%d %H:%M"):
                        return hours["temp_c"]
        return None

    def get_lat_and_long(self, city):
        location = self.get_data(city)
        return location['location']["lat"], location['location']["lon"]


# queue class
queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)
print(queue.pop())
print(queue.pop())
print(queue.is_empty())


# queueException
queueException = QueueException.create_queue("queue", 5)
queueException.insert(1)
queueException.insert(2)
queueException.insert(3)
queueException.insert(4)
print(queueException.pop())
print(queueException.pop())
print(queueException.is_empty())
queueException.save("test")
queueException.insert(3)
queueException.insert(3)
queueException.load("test")
print(queueException.items)
queueException2 = QueueException.create_queue("queue2", 5)
print(queueException2.items)
queueException3 = QueueException.create_queue("queue", 5)
print(queueException3.items)


weather_obj = Weather("3fcee3b81206453bbc5233241231004")
print(weather_obj.get_weather("London"))
print(weather_obj.get_temperature_after("London", 0))
print(weather_obj.get_lat_and_long("London"))

