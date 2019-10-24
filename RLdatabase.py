import boto3
import time
class Database:

    def __init__(self, amazonID):
        dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1') #connect to US dynamodb servers
        self.amazonID = amazonID
        if (amazonID != ''):
            try:
                table = dynamodb.create_table( #if first time login, create new unique table
                TableName=str(amazonID),
                KeySchema=[
                    {
                        'AttributeName': 'name',
                        'KeyType': 'HASH'  #Partition key
                    },
                    {
                        'AttributeName': 'user',
                        'KeyType': 'RANGE'  #Sort key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'user',
                        'AttributeType': 'S'
                    },
            
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                    }
                )
                time.sleep(10)  #wait for table to be created, better than get_waiter because it defaults to 20 secs 
                self.table = dynamodb.Table(str(amazonID))
            except:
                pass
            self.table = dynamodb.Table(str(amazonID))
            self.response = self.table.scan()
            self.database = {}
            for i in range (len(self.response['Items'])): #add every item in db to class
                self.database[self.response['Items'][i]["name"]] = self.response['Items'][i]["user"]
            self.cleanup() #remove potential broken usernames (would occur if app crashes)

    def cleanup(self):
        if (self.amazonID != ''): #insures table exists
            for element in self.database:
                if self.database[element] == 'null': #checks if username is blank
                    self.table.delete_item(Key={'name': element,'user': 'null'})#if so, delete
        return

    def freshname(self):
        fresh = {}
        for element in self.database:
            if self.database[element] == 'null': 
                fresh[element] = self.database[element] #creates a dic of blank usernames (should only be 1 to add username)
        return fresh

    def get(self):
        return self.database #return Database instance

    def add(self, name, user):
        self.table.put_item(Item={'name' : name , 'user' : user }) #add name/user to database
        return

    def delete(self, name):
        self.table.delete_item(Key={'name' : name, 'user': self.database[name]}) #delete name and name's key value pair from database
        return

    def listusers(self):
        self.cleanup() #removes broken name/users
        users = ''
        for element in self.database:
            users = users + element + " as " + self.database[element] + ", " #return all functional name/users in database
        return users
