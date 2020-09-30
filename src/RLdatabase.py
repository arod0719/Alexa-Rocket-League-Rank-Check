import boto3
class Database:

    def __init__(self, amazonID):
        dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1') #initialize connection
        self.amazonID = amazonID
        self.noob = False #determines if new user
        if (amazonID != ''):
            try:
                table = dynamodb.create_table(
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
                ) #tries to make a new table, will succeed if new user
                table.meta.client.get_waiter('table_exists').wait(TableName=str(amazonID), WaiterConfig={'Delay': 2}) #checks ever 2 secs for 20 secs if table has been created
                self.noob = True #if table is created, new user
            except:
                pass #if returning user, don't create new table
            self.table = dynamodb.Table(str(amazonID))
            self.response = self.table.scan()
            self.database = {}
            for i in range (len(self.response['Items'])): #buts table into dict
                self.database[self.response['Items'][i]["name"]] = self.response['Items'][i]["user"]
            self.cleanup()

    def cleanup(self): #to delete entries in the database without a username (will occur if shut down in username creation)
        if (self.amazonID != ''):
            for element in self.database:
                if self.database[element] == 'null':
                    self.table.delete_item(Key={'name': element,'user': 'null'})
        return

    def freshname(self): #checks if name is new
        fresh = {}
        for element in self.database:
            if self.database[element] == 'null':
                fresh[element] = self.database[element]
        return fresh

    def get(self): #returns database
        return self.database

    def add(self, name, user): #add name and user to table
        self.table.put_item(Item={'name' : name , 'user' : user })
        return

    def delete(self, name): #delete name and user where name
        self.table.delete_item(Key={'name' : name, 'user': self.database[name]})
        return

    def listusers(self): #lists all users, create for debugging over voice
        self.cleanup()
        users = ''
        for element in self.database:
            users = users + element + " as " + self.database[element] + ", "
        return users

    def new(self): #checks if user is new or not
        return self.noob
