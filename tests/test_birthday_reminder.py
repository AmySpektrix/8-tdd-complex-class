from lib.birthday_reminder import *



def test_blanky_dictionary():
    reminder = BirthdayReminder()
    assert reminder.database == {}

def test_add_birthday():
    reminder = BirthdayReminder()
    reminder.add_birthday("Amy Brown","1990-07-20")
    assert reminder.database == {"Amy Brown":{'DOB':"1990-07-20",'cardsent':False}}

def test_update_name():
    reminder = BirthdayReminder()
    reminder.add_birthday("Amy Brown","1990-07-20")
    reminder.update_name("Amy Brown","Amy Claire Brown")
    assert reminder.database == {"Amy Claire Brown":{'DOB':"1990-07-20",'cardsent':False}}

def test_add_multiple_names_update_a_name():
    reminder = BirthdayReminder()
    reminder.add_birthday("Amy Brown","1990-07-20")
    reminder.add_birthday("Firat Gulmez","1996-08-15")
    reminder.update_name("Amy Brown","Amy Claire Brown")
    assert reminder.database == {"Amy Claire Brown":{'DOB':"1990-07-20",'cardsent':False},"Firat Gulmez":{'DOB':"1996-08-15",'cardsent':False}}