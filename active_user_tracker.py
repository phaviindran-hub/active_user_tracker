# Login-Logout tracker made by me to check who is logged in on each machine


def get_event_date(event):
    return event.date

def check_logged_in(events):
    # sort events so older ones go first
    events.sort(key=get_event_date)

    machine_dict = {}  # keeps track of users on each machine

    for e in events:
        if e.machine not in machine_dict:
            machine_dict[e.machine] = set()  # new machine, empty set of users

        if e.type == "login":
            machine_dict[e.machine].add(e.user)

        elif e.type == "logout":
            if e.user in machine_dict[e.machine]:
                machine_dict[e.machine].remove(e.user)
            else:
                # user tried to logout but wasn't logged in, i just wanted to show Aaron was logged out without logging in 
                print(f"Warning: {e.user} tried to logout from {e.machine} but wasn't logged in ")

    return machine_dict

def show_report(machine_dict):
    print("\n   Active Users Report  ")
    for machine, users in machine_dict.items():
        if users:
            user_list = ", ".join(users)
            print(machine + ": " + user_list)  

class Event:
    def __init__(self, date, type, machine, user):
        self.date = date
        self.type = type
        self.machine = machine
        self.user = user

# some sample events, might not be perfect 
events = [
    Event('2020-01-21 12:45:00', 'login', 'myworkstation.local', 'Johnathan'),
    Event('2020-01-22 15:53:00', 'logout', 'webserver.local', 'Johnathan'),
    Event('2020-01-21 18:53:00', 'login', 'webserver.local', 'layla'),
    Event('2020-01-22 10:25:00', 'logout', 'myworkstation.local', 'Johnathan'),
    Event('2020-01-21 08:20:00', 'login', 'webserver.local', 'Johnathan'),
    Event('2020-01-23 11:24:00', 'logout', 'mailserver.local', 'Aaron'),
]

# run the tracker
current = check_logged_in(events)
show_report(current)
