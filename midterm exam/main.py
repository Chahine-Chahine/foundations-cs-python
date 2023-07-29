import datetime

# Function to read tickets from the file and store them in a list of dictionaries
def readTickets(file_path): #worst case =>O(n), where n is the number of lines in the file
    tickets = []
    with open(file_path, 'r') as file:
        for line in file:
            ticket_info = line.strip().split(', ')
            # ticket is a dictionary
            ticket = {
                "ticket_id": ticket_info[0],
                "event_id": ticket_info[1],
                "username": ticket_info[2],
                # strptime method from https://www.geeksforgeeks.org/python-time-strptime-function/
                "timestamp": datetime.datetime.strptime(ticket_info[3], '%Y%m%d'),
                "priority": int(ticket_info[4])
            }
            tickets.append(ticket)
    return tickets


# Function to save a new ticket to the system
def saveTickets(file_path, tickets):# O(n), where n is the number of tickets
    with open(file_path, 'w') as file: #'w', is the mode for writing while 'r' is for reading
        for ticket in tickets:
            file.write(f"{ticket['ticket_id']}, {ticket['event_id']}, {ticket['username']}, {ticket['timestamp'].strftime('%Y%m%d')}, {ticket['priority']}\n")



# Function to add a new ticket to the system
def addTicket(tickets, event_id, username, current_date): #O(1)
    ticket_id = f"tick{str(len(tickets) + 1).zfill(3)}"
    # Convert the current_date to a datetime object
    current_date = datetime.datetime.strptime(current_date, '%Y%m%d')
    new_ticket = {
        'ticket_id': ticket_id,
        'event_id': event_id,
        'username': username,
        'timestamp': current_date,
        'priority': 0
    }
    tickets.append(new_ticket)
    print("Ticket booked successfully!")



# Function to add a new ticket to the system for admin with extra control
def adminAddTicket(tickets, event_id, username, current_date, priority):# O(1)
    ticket_id = f"tick{str(len(tickets) + 1).zfill(3)}"
    current_date = datetime.datetime.strptime(current_date, '%Y%m%d')
    new_ticket = {
        'ticket_id': ticket_id,
        'event_id': event_id,
        'username': username,
        'timestamp': current_date,
        'priority': priority
    }
    tickets.append(new_ticket)
    print("Ticket booked successfully!")




#remove ticket form the list tickets through ticket_id
#The remove() method removes the first matching element (which is passed as an argument) from the list
#https://www.programiz.com/python-programming/methods/list/remove
def removeTicket(tickets, ticket_id):
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            tickets.remove(ticket)
            print(f"Ticket ID {ticket_id} removed from the system.")
            return True
    return False




# Function to find the event with the highest number of tickets
def findMostBooked(tickets): # O(n), where n is the number of tickets
    events = {} # Initializing a dict
    for ticket in tickets:
        event_id = ticket["event_id"]
        if event_id in events:
            events[event_id] += 1
        else:
            events[event_id] = 1

    if not events:
        return None
    # max value in a dictionary by key https://www.youtube.com/watch?v=CJsBF2a5zsg (Indians are the best)
    most_booked_event = max(events, key=events.get)
    return most_booked_event



# Insertion Sort function implimentation 
def insertionSort(tickets): #O(n^2), where n is the number of tickets
    for i in range(1, len(tickets)): #o(n)
        key = tickets[i]
        j = i - 1
        while j >= 0 and (key['timestamp'], key['event_id']) < (tickets[j]['timestamp'], tickets[j]['event_id']): #o(N)
            tickets[j + 1] = tickets[j]
            j -= 1
        tickets[j + 1] = key


# Function that checks if a ticket exists and returns a boolean either true or false
def checkForTicket(tickets, ticket_id):
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            return True

    return False

# Function that gets the priority
def getPriority(ticket):
    return ticket['priority']


# Function that display then remove the events of today's date
def displayAndRemove(tickets):
    today_date = datetime.datetime.today().date()
    today_events = []

    for ticket in tickets:
        if ticket['timestamp'].date() == today_date:
            today_events.append(ticket)

    if not today_events:
        print("No events found today.")
    else:
        today_events.sort(key=getPriority)
        print("\nToday's Events Sorted by Priority:")
        for event in today_events:
            print(f"Event ID: {event['event_id']}")
            print(f"Username: {event['username']}")
            print(f"Priority: {event['priority']}")
            print(f"Event Date: {event['timestamp'].strftime('%Y%m%d')}")
            print(f"Ticket ID: {event['ticket_id']}\n")

        for event in today_events:
            tickets.remove(event)

    return tickets



# User Menue to display for User
def userMenu(tickets): #O(n), where n is the number of user interactions.
    username = input("Username: ")
    password = input("Password: ")

    while True:
        print("1. Book A ticket")
        print("2. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            event_id = input("Enter the event id: ")
            current_date = input("Input the date of the event in yyyymmdd format: ")
            addTicket(tickets, event_id, username, current_date)
        elif choice == 2:
            saveTickets("tickets.txt", tickets)  # Save tickets before exiting
            print("saving...")
            print("Exiting Program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Admin Menue to display for Admin
def adminMenu(tickets): #O(n), where n is the number of user interactions.
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
                    event_id = input("Insert event ID: ")
                    username = input("username for the ticket booking: ")
                    current_date = input("Input the date of the event in yyyymmdd format: ")
                    priority = int(input("Enter priority number: "))
                    adminAddTicket(tickets, event_id, username, current_date, priority)
                    save = input("Do you wish to save? (write y if yes n for no)")
                    if save.lower() == "y":
                       saveTickets("tickets.txt", tickets)  # Save tickets before exiting
                       print("saving...")
                    elif save.lower() == "n":
                      print("Not saved")

              
                elif choice == 3:
                    # Filter out old tickets (tickets with a date greater than or equal to today)
                    today_date = datetime.datetime.today().date()
                    today = datetime.datetime.today()
                    print("\nToday's Tickets:")
                    for ticket in tickets:
                        if ticket['timestamp'].date() == today_date:  # Compare only the date part
                            print(f"Ticket ID: {ticket['ticket_id']}")
                            print(f"Event ID: {ticket['event_id']}")
                            print(f"Username: {ticket['username']}")
                            print(f"Event Date: {ticket['timestamp'].strftime('%Y%m%d')}")
                            print(f"Priority: {ticket['priority']}\n")
                    # Display the sorted tickets
                    print("\nUpcoming Tickets:")
                    for ticket in tickets:
                        if ticket['timestamp'] >= today:
                            print(f"Ticket ID: {ticket['ticket_id']}")
                            print(f"Event ID: {ticket['event_id']}")
                            print(f"Username: {ticket['username']}")
                            print(f"Event Date: {ticket['timestamp'].strftime('%Y%m%d')}")
                            print(f"Priority: {ticket['priority']}\n")

              
                elif choice == 4:
                    ticket_id = input("Enter the ticket ID: ")
                    if checkForTicket(tickets, ticket_id):
                        priority = int(input("Enter the new priority: "))
                        for ticket in tickets:
                            if ticket['ticket_id'] == ticket_id:
                                ticket['priority'] = priority
                                print(f"Priority for Ticket ID {ticket_id} changed to {priority}.")
                                save = input("Do you wish to save? (write y if yes n for no)")
                                if save.lower() == "y":
                                    saveTickets("tickets.txt", tickets)  # Save tickets before exiting
                                    print("saving...")
                                elif save.lower() == "n":
                                    print("Not saved")
                                break
                    else:
                        print(f"Ticket ID {ticket_id} not found.")
              

              
                elif choice == 5:
                    ticket_id = input("Enter the ticket ID: ")
                    if removeTicket(tickets, ticket_id):
                        save = input("Do you wish to save? (write y if yes n for no)")
                        if save.lower() == "y":
                            saveTickets("tickets.txt", tickets)  # Save tickets before exiting
                            print("saving...")
                        elif save.lower() == "n":
                            print("Not saved")
                    else:
                        print(f"Ticket ID {ticket_id} not found.")

              
                elif choice == 6:
                    tickets = displayAndRemove(tickets)
                    save = input("Do you wish to save? (write y if yes n for no)")
                    if save.lower() == "y":
                        saveTickets("tickets.txt", tickets)  # Save tickets before exiting
                        print("saving...")
                    elif save.lower() == "n":
                        print("Not saved")


              
                elif choice == 7:
                    print("Exiting Program...")
                    
                else:
                    print("Invalid choice. Please try again.")


      
        else:
            print("Incorrect Username and/or Password.")
            attempts += 1

    print("Maximum login attempts reached, exiting Program...")
    return False


# Main function the first to be executed 
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
