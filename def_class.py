from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: date
    
    def age():
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

    @property
    def full_name():
        return f"{self.first_name} {self.last_name}"
                
    employees = [
        Person("John", "Doe", date(1989, 10, 10)),
        Person("Jane", "Smith", date(1990, 11, 11)),
        Person("Jack", "Brown", date(1991, 12, 12)),
        Person("Jill", "Johnson", date(1992, 1, 1)),
        Person("Alex", "Williams", date(1993, 2, 2)),
        Person("Emily", "Davis", date(1994, 3, 3)),
        Person("Daniel", "Miller", date(1995, 4, 4)),
        Person("Olivia", "Wilson", date(1996, 5, 5)),
        Person("Michael", "Anderson", date(1997, 6, 6)),
        Person("Sophia", "Taylor", date(1998, 7, 7)),
        Person("Matthew", "Thomas", date(1999, 8, 8)),
        Person("Ava", "Robinson", date(2000, 9, 9)),
        Person("William", "Clark", date(2001, 10, 10)),
        Person("Isabella", "Lewis", date(2002, 11, 11)),
        Person("James", "Hill", date(2003, 12, 12)),
        Person("Mia", "Moore", date(2004, 1, 1)),
        Person("Benjamin", "Walker", date(2005, 2, 2)),
        Person("Charlotte", "Hall", date(2006, 3, 3)),
        Person("Henry", "Young", date(2007, 4, 4)),
        Person("Amelia", "Scott", date(2008, 5, 5)),
        Person("Alexander", "Green", date(2009, 6, 6)),
        Person("Ella", "Baker", date(2010, 7, 7)),
        Person("Joseph", "Adams", date(2011, 8, 8)),
        Person("Grace", "Nelson", date(2012, 9, 9)),
        Person("Daniel", "Wright", date(2013, 10, 10)),
    ]