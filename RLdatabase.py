import boto3
class Database:

    def __init__(self):
        dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
        self.table = dynamodb.Table('rocketleagueusers')
        self.response = self.table.scan()
        self.database = {}
        for i in range (len(self.response['Items'])):
            self.database[self.response['Items'][i]["name"]] = self.response['Items'][i]["user"]

    def cleanup(self):
        for element in self.database:
            if self.database[element] == 'null':
                self.delete(element)
        return

    def freshname(self):
        fresh = {}
        for element in self.database:
            if self.database[element] == 'null':
                fresh[element] = self.database[element]
        return fresh

    def get(self):
        return self.database

    def add(self, name, user):
        self.table.put_item(Item={'name' : name , 'user' : user })
        return

    def delete(self, name):
        self.table.delete_item(Key={'name' : name})
        return

    def listusers(self):
        self.cleanup()
        users = ''
        for element in self.database:
            users = users + " " + element + ","
        return users
