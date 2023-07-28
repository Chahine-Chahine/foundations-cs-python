import datetime
#datetime search from : https://www.w3schools.com/python/python_datetime.asp
# Function to read tickets from the file and store them in a list of dictionaries
def readTickets(file_path):
    tickets = []
    with open(file_path, 'r') as file:
        for line in file:
            ticket_info = line.strip().split(', ')
          #ticket is a dictionary
            ticket = {
                "ticket_id": ticket_info[0],
                "event_id": ticket_info[1],
                "username": ticket_info[2],
              #strptime method from https://www.geeksforgeeks.org/python-time-strptime-function/
                "timestamp": datetime.datetime.strptime(ticket_info[3], '%Y%m%d'),
                "priority": int(ticket_info[4])
            }
            tickets.append(ticket)
    return tickets

# Function to add a new ticket to the system
def saveTickets(file_path, tickets):
    with open(file_path, 'w') as file: #'w', is the mode for writing while 'r' is for reading
        for ticket in tickets:
            file.write(f"{ticket['ticket_id']}, {ticket['event_id']}, {ticket['username']}, {ticket['timestamp'].strftime('%Y%m%d')}, {ticket['priority']}\n")

def addTicket(tickets, event_id, username, current_date):
    ticket_id = f"tick{str(len(tickets) + 1).zfill(3)}"
    new_ticket = {
        'ticket_id': ticket_id,
        'event_id': event_id,
        'username': username,
        'timestamp': current_date,
        'priority': 0
    }
    tickets.append(new_ticket)
    print("Ticket booked successfully!")

# Function to find the event with the highest number of tickets
def findMostBooked(tickets):
    events = {} #Initializing a dict
    for ticket in tickets:
        event_id = ticket["event_id"]
        if event_id in events:
            events[event_id] += 1
        else:
            events[event_id] = 1

    if not events:
        return None
#max value in a dictionary by key https://www.youtube.com/watch?v=CJsBF2a5zsg (Indians are the best)
    most_booked_event = max(events, key=events.get)
    return most_booked_event

def userMenu(tickets):  
    username = input("Username: ")
    password = input("Password: ")

    while True:
        print("1. Book A ticket")
        print("2. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            event_id = input("Enter the event id: ")
            current_date = datetime.datetime.now()
            addTicket(tickets, event_id, username, current_date)
        elif choice == 2:
            saveTickets("tickets.txt", tickets)  # Save tickets before exiting
            print("Exiting Program...")
            break
        else:
            print("Invalid choice. Please try again.")

def adminMenu(tickets):
    attempts = 0
    while attempts < 5:
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "admin123123":
            print("Welcome admin")
            while True:
                print("\nMenu")
                print("1. Display Statistics")
                print("2. Book a ticket")
                print("3. Display all tickets")
                print("4. Change Ticket’s Priority")
                print("5. Disable Ticket")
                print("6. Run events")
                print("7. Exit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    most_booked_event = findMostBooked(tickets)
                    if most_booked_event is not None:
                        print(f"Event ID with the highest number of tickets: {most_booked_event}")
                    else:
                        print("No tickets available.")  
                elif choice == 2:
                    pass  
                elif choice == 3:
                    pass  
                elif choice == 4:
                    pass 
                elif choice == 5:
                    pass  
                elif choice == 6:
                    pass  
                elif choice == 7:
                    print("Exiting Program...")
                    return False  
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Incorrect Username and/or Password.")
            attempts += 1

    print("Maximum login attempts reached, exiting Program...")
    return False

def main():
    file_path = "tickets.txt"
    tickets = readTickets(file_path)

    choice = input("User Type Admin or User: ").lower()

    if choice == "admin":
        adminMenu(tickets)
    elif choice == "user":
        userMenu(tickets)  
    else:
        print("Invalid user type. Exiting...")

main()
