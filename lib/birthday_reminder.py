class BirthdayReminder:

    def __init__(self):
        self.database = {}

    def add_birthday(self,name,birthdate):
        self.database[name] = {'DOB':birthdate,'cardsent':False}

    def update_name(self,old_name,new_name):
        self.database[new_name] = self.database[old_name]
        self.database.pop(old_name)

    def update_birthdate(self,name,new_birthdate):
        self.database[name]['DOB'] = new_birthdate
        

    def age_and_birthdays_next_30_days(self):
        #Parameters:
        #  vibes
        #Returns:
        #   List of upcoming Names, Birthdays and Age at next birthday - format "Name Birthday:DD MM Age: upcomingage" excluding cardsent = True
        pass

    def mark_card_send(self,name):
        #Parameters:
        #  name: String
        #Returns:
        #   nothing
        # Side effect:
        # changing the value of cardsent to True    
        pass