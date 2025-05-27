#!/usr/bin/env python3
from ics import Calendar, Event
from datetime import datetime
import argparse
import pytz

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create an ICS file for an event.')
    parser.add_argument('event_name', type=str, help='Name of the event')
    parser.add_argument('event_begin', type=str, help='Start time of the event (YYYY-MM-DD HH:MM)')
    parser.add_argument('event_end', type=str, help='End time of the event (YYYY-MM-DD HH:MM)')
    parser.add_argument('file_name', type=str, help='Name of the output ICS file')
    return parser.parse_args()

def create_ics_file(event_name, event_begin, event_end, file_name):
    

    # Create a new calendar
    calendar = Calendar()

    # Create a new event
    event = Event()
    event.name = event_name
    event.begin = event_begin  # CET is UTC+1
    event.end = event_end  # CET is UTC+1
    event.organizer = "Alan Francke:mailto:alan@francke-iot.com"
    event.location = "Microsoft Teams"

    # Add the event to the calendar
    calendar.events.add(event)

    # Prompt user to enter meeting description

    event.description = input("Enter the description for the event: ")

    # Write the calendar to a file
    with open(file_name, 'w') as f:
        f.writelines(calendar)

if __name__ == "__main__":
    args = parse_arguments()
    cet = pytz.timezone('CET')
    event_begin = cet.localize(datetime.strptime(args.event_begin, '%Y-%m-%d %H:%M'))
    event_end = cet.localize(datetime.strptime(args.event_end, '%Y-%m-%d %H:%M'))
    create_ics_file(args.event_name, event_begin, event_end, args.file_name)

# Example usage
# event_name = "Meeting with Bob"
# event_begin = datetime(2023, 10, 25, 10, 0)
# event_end = datetime(2023, 10, 25, 11, 0)
# file_name = "meeting.ics"

#create_ics_file(event_name, event_begin, event_end, file_name)