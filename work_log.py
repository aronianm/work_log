import os
import csv
import datetime
from datetime import date
import re


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print("  Work Log Menu ")
    print("\n")
    print("     1. Add a New Entry")
    print("     2. Search for an existing entry")
    print("    'Q' to quit ")
    print("\n")


def search_menu():
    print("  Search Menu ")
    print("\n")
    print("     1. All Tasks")
    print("     2. Name of Task")
    print("     3. Date of Task")
    print(".    4. By Duration")
    print(".    5. By Pattern with help")
    print(".    6. By Patter with No Help")
    print("    'Q' to quit ")


def pattern_menu():
    print("Pattern Help")
    print("\n")
    print("type:")
    print("\n")
    print("'any'      (all characters)   '0+'         (0 or more character)")
    print("'letter'   (a-z)              'space'      (white space)")
    print("'number'   (0-9)              '1+'         (1 or more character)")
    print("'start'    (start string)     'end'        (end string)")
    print("'copies'   (x amount).        'special'    (individual characters)")
    print("\n")
    print("Groups")
    print("\n")
    print("'start group'  (open parethesis)  'end group'  (closed parethesis)")
    print("'start class'  (open brackets)    'end class'  (closed brackets)")
    print("\n")
    print("Flags")
    print("\n")
    print("'I'  (upper/lower case)  'M'  (Muli-Line)")
    print("\n")
    print("'done' (to test pattern)       ")


class Add_entry:

    def __init__(self):
        self.task_name = input("What is the name of your task> ")
        clear()
        while True:
            self.user_date = str(input('date> '))
            try:
                self.task_date = datetime.datetime.strptime(
                    self.user_date, '%m/%d/%Y'
                    ).date()
                break
            except ValueError:
                print("Wrong format")
                continue
        clear()
        while True:
            self.task_duration = input("Duration of the task in seconds 00 > ")
            try:
                self.minutes_object = datetime.time(
                    second=int(self.task_duration)
                    )
                break
            except ValueError:
                print("Wrong format")
                continue
            except TypeError:
                print("Wrong format")
                continue
        clear()
        self.task_notes = input("Add some notes to the file? > ")

    def writer(self):

        with open('works_log.csv', 'a') as csvfile:
            fieldnames = [
                'task_name', 'task_date', 'task_duration', 'task_notes'
                ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'task_name': self.task_name,
                'task_date': self.task_date,
                'task_duration': self.minutes_object,
                'task_notes': self.task_notes
                })


class Search():
    """ Search class"""
    def __init__(self):
        self.works_log = open('works_log.csv', encoding='utf-8')
        self.data = self.works_log.read()

    def time_spent(self):
        """User search for dates and lists tasks"""
        self.match_two = input('Date (MM/DD/YYYY) > ')
        try:
            self.match_time = datetime.datetime.strptime(
                self.match_two, '%m/%d/%Y').date()
        except ValueError:
            print("Wrong format")

        self.works_log = open('works_log.csv', 'r', encoding='utf-8')
        for self.line in self.works_log:
            self.search = re.search(
                r'^([a-z\s\']+)[^.]+(\d{4}-\d{2}-\d{2})' +
                r',(\d{2}\:\d{2}\:\d{2}),(.*)', self.line, re.I | re.M
                )
            if str(self.match_time) in self.search.group(2):
                print(
                    "\n" + "Task: " + self.search.group(1) + " " +
                    "\n" + "Date: " + self.search.group(2) + " " +
                    "\n" + "Duration: " + self.search.group(3) + "\n" * 2 +
                    "notes: " +
                    self.search.group(4) +
                    "\n" * 2)

    def exact_task(self):
        """user search for task by name"""
        self.match_task = input("What do you want to search> ")
        self.works_log = open('works_log.csv', 'r', encoding='utf-8')
        for self.line in self.works_log:
            self.search = re.search(
                r'^([a-z\s\']+)[^.]+(\d{4}-\d{2}-\d{2})' +
                r',(\d{2}\:\d{2}\:\d{2}),(.*)', self.line, re.I | re.M
                )
            if str(self.match_task).upper() in self.search.group(1).upper():
                print(
                    "\n" + "Task: " + self.search.group(1) + " " +
                    "\n" + "Date: " + self.search.group(2) + " " +
                    "\n" + "Duration: " + self.search.group(3) + "\n" * 2 +
                    "notes: " +
                    self.search.group(4) +
                    "\n" * 2)

    def all_tasks(self):
        """User will get a list of dates used for tasks"""
        self.works_log = open('works_log.csv', 'r', encoding='utf-8')
        for self.line in self.works_log:
            self.search = re.search(
                r'^([a-z\s\']+)[^.]+(\d{4}-\d{2}-\d{2})' +
                r',(\d{2}\:\d{2}\:\d{2}),(.*)', self.line, re.I | re.M
                )
            if self.search:
                print(
                    "Task Name: " + self.search.group(1) + " " +
                    "\n" + "Task Date: " + self.search.group(2) + " " +
                    "\n" + "Task Duration:" + self.search.group(3) + " " +
                    "\n" + "Task Notes:" + self.search.group(4) + "\n" * 2
                      )

    def by_duration(self):
        """User will search of task by duration in seconds"""
        self.user = input("how many seconds? ")
        self.duration_str = datetime.time(second=int(self.user))
        self.works_log = open('works_log.csv', 'r', encoding='utf-8')
        for self.line in self.works_log:
            self.search = re.search(
                r'^([a-z\s\']+)[^.]+(\d{4}-\d{2}-\d{2})' +
                r',(\d{2}\:\d{2}\:\d{2}),(.*)', self.line, re.I
                )
            if str(self.duration_str) in self.search.group(3):
                print(
                    "Task Name: " + self.search.group(1) + " " +
                    "\n" + "Task Date: " + self.search.group(2) + " " +
                    "\n" + "Task Duration:" + self.search.group(3) + " " +
                    "\n" + "Task Notes:" + self.search.group(4) + "\n" * 2
                      )

    def by_pattern_help(self):
        try:
            self.pattern = ''
            while True:
                print(self.pattern)
                self.user = input("> ")
                if self.user == 'any':
                    self.pattern += '.'
                elif self.user == 'letter':
                    self.pattern += '\w'
                elif user == 'number':
                    self.pattern += '\d'
                elif self.user == '0+':
                    self.pattern += '*'
                elif self.user == '1+':
                    self.pattern += '+'
                elif self.user == 'number':
                    self.pattern += '\d'
                elif self.user == "space":
                    self.pattern += "\s"
                elif self.user == "start group":
                    self.pattern += "("
                elif self.user == "end group":
                    self.pattern += ")"
                elif self.user == "start class":
                    self.pattern += "["
                elif self.user == "end class":
                    self.pattern += "]"
                elif self.user == "start":
                    self.pattern += "^"
                elif self.user == "end":
                    self.pattern += "$"
                elif self.user == "special":
                    self.user_s = input("Enter special character> ")
                    self.pattern += str(self.user_s)
                elif self.user == "copies":
                    self.pattern += "{"
                    self.user_s = input("How many> ")
                    self.pattern += str(self.user_s)
                    self.pattern += "}"
                elif self.user == "done":
                    break
                else:
                    print("Please read the menu")
            print("\n" * 2)
            print("Do you want any flags?")
            self.user = input("Y/N > ").upper()
            if self.user == "Y":
                print("What would you like? ")
                self.user = input("> ").upper()
                if self.user == "I":
                    self.works_log = open(
                       'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.search(
                            str(self.pattern), self.line, re.I)
                        if self.search:
                            print(self.search.group(0))
                elif self.user == "M":
                    self.works_log = open(
                        'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.search(
                            str(self.pattern), self.line, re.M)
                        if self.search:
                            print(self.search.group(0))
                elif self.user == "M and I":
                    self.works_log = open(
                        'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.search(
                            str(self.pattern), self.line, re.I | re.M)
                        if self.search:
                            print(self.search.group(0))
            elif self.user == "N":
                self.works_log = open('works_log.csv', 'r', encoding='utf-8')
                for self.line in self.works_log:
                    self.search = re.search(str(self.pattern), self.line)
                    if self.search:
                        print(self.search.group(0))
        except Exception:
            print(input("Recheck your pattern"))

    def by_pattern_none(self):
        print("Do you want to 'findall' 'search' or 'match'")
        while True:
            user = input("> ").lower()
            if user == "findall":
                print("Enter your REGEX pattern below")
                self.pattern = input("> ")
                clear()
                print("Nice job!")
                print("Do you want any flags for your pattern? Y/n")
                user = input("> ").upper()
                if user == "Y":
                    print("'I' for IgnoreCase or 'M' for Muli-Line or 'Both'")
                    user = input("> ").upper()
                    if user == "I":
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.findall(
                                str(self.pattern), self.line, re.I)
                            print(self.search)
                        break
                    if user == 'M':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.findall(
                                str(self.pattern), self.line, re.M)
                            print(self.search)
                        break
                    if user == 'BOTH':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.findall(
                                str(self.pattern), self.line, re.I | re.M)
                            if self.search:
                                print(self.search)
                        break
                if user == "N":
                    self.works_log = open(
                        'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.findall(
                            str(self.pattern), self.line)
                        print(self.search)
                    break

            elif user == "search":
                print("Enter your REGEX pattern below")
                self.pattern = input("> ")
                clear()
                print("Nice job!")
                print("Do you want any flags for your pattern? Y/n")
                user = input("> ").upper()
                if user == "Y":
                    print("'I' for IgnoreCase or 'M' for Muli-Line or 'Both'")
                    user = input("> ").upper()
                    if user == "I":
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.search(
                                str(self.pattern), self.line, re.I)
                            if self.search:
                                print(self.search.group(0))
                        break
                    if user == 'M':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.search(
                                str(self.pattern), self.line, re.M)
                            if self.search:
                                print(self.search.group(0))
                        break
                    if user == 'BOTH':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.search(
                                str(self.pattern), self.line, re.I | re.M)
                            if self.search:
                                print(self.search.group(0))
                        break
                if user == "N":
                    self.works_log = open(
                        'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.search(str(self.pattern), self.line)
                        if self.search:
                            print(self.search.group(0))
                    break

            elif user == "match":
                print("Enter your REGEX pattern below")
                self.pattern = input("> ")
                clear()
                print("Nice job!")
                print("Do you want any flags for your pattern? Y/n")
                user = input("> ").upper()
                if user == "Y":
                    print("'I' for IgnoreCase or 'M' for Muli-Line or 'Both'")
                    user = input("> ").upper()
                    if user == "I":
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.match(
                                str(self.pattern), self.line, re.I)
                            if self.search:
                                print(self.search.group(0))
                        break
                    if user == 'M':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.match(
                                str(self.pattern), self.line, re.M)
                            if self.search:
                                print(self.search.group(0))
                        break
                    if user == 'BOTH':
                        self.works_log = open(
                            'works_log.csv', 'r', encoding='utf-8')
                        for self.line in self.works_log:
                            self.search = re.match(
                                str(self.pattern), self.line, re.I | re.M)
                            if self.search:
                                print(self.search.group(0))
                        break
                if user == "N":
                    self.works_log = open(
                        'works_log.csv', 'r', encoding='utf-8')
                    for self.line in self.works_log:
                        self.search = re.match(str(self.pattern), self.line)
                        if self.search:
                            print(self.search.group(0))
                    break


# start of program
clear()
while True:
    clear()
    menu()
    user = input(">  ").upper()
    if user == '1':
        clear()
        Add_entry().writer()
    elif user == '2':
        clear()
        search_menu()
        user = input(">  ").upper()
        clear()
        if user == '1':
            while True:
                clear()
                Search().all_tasks()
                user = input("Press Enter to go back to Main Menu ").upper()
                break
        if user == '2':
            while True:
                clear()
                Search().exact_task()
                user = input("Press Y to search another task > ").upper()
                if user == 'Y':
                    continue
                else:
                    break
        if user == '3':
            while True:
                clear()
                Search().time_spent()
                user = input("Press Y to search another task >  ").upper()
                if user == 'Y':
                    continue
                else:
                    break
        if user == '4':
            while True:
                clear()
                Search().by_duration()
                user = input("Press Y to search another task >  ").upper()
                if user == 'Y':
                    continue
                else:
                    break
        if user == '5':
            while True:
                clear()
                pattern_menu()
                Search().by_pattern_help()
                user = input("Press Y to search another task >  ").upper()
                if user == 'Y':
                    continue
                else:
                    break
        if user == '6':
            while True:
                clear()
                Search().by_pattern_none()
                user = input("Press Y to search another task >  ").upper()
                if user == 'Y':
                    continue
                else:
                    break
    elif user == "Q":
        print("Goodbye! Thank you")
        break
else:
    print(" ")
