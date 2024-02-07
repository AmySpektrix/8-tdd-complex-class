# BIRTHDAY BESTIES

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card
# what counts as soon?

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays
# in what way upcoming?

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._


info to store:
- Name - string 
- Birthday - date object
- Has birthday card been sent for this year? - boolian - resetting to zero 

info to update:
- update - name
- update - birthday
- Has birthday card been sent for this year? - boolian

info to return?
- birthday coming up - list of names of who to send card with their birthdays
- age coming up - int

Database =
{name:{birthdate:datetimeobject, cardsent:boolian},
 name2:{birthdate:datetimeobject2, cardsent:boolian2},}


```python

class BirthdayReminder:
    # User-facing properties: none

    def __init__(self):
        #Parameters: None
        #side effect: 
        #   creates a dictionary container
        pass

    def add_birthday(self,name,birthdate):
        #Parameters:
        #   name: string
        #   birthdate: iso format YYYY-MM-DD
        #Side Effects:
        #   create the cardsent key and sets the value to 0/False 
        #   adds a dictionary to the initial database

    def update_name(self,old_name,new_name):
        #Parameters:
        #   old_name: string
        #   new_name: string
        #Side Effects:
        #   changes the key value of old_name to new_name
        
    def update_birthdate(self,name,new_birthdate):
        #Parameters:
        #   name: string
        #   new_birthdate: datetime iso format YYYY-MM-DD
        #Side Effects:
        #   changes the value of birthdate to new_birthdate for the dictionary item "name"

    def age_and_birthdays_next_30_days(self)
        #Parameters:
        #  vibes
        #Returns:
        #   List of upcoming Names, Birthdays and Age at next birthday - format "Name Birthday:DD MM Age: upcomingage" excluding cardsent = True
    
    def mark_card_send(self,name):
         #Parameters:
        #  name: String
        #Returns:
        #   nothing
        # Side effect:
        # changing the value of cardsent to True
    
               


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a DOB 
add name, DOB, cardsent:0 in to the Database
"""
reminder = BirthdayReminder()
reminder.add("Amy Brow","1990-07-20")
assert reminder.database == {"Amy Brown":{'DOB':"1990-07-20",'cardsent':False}}

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._