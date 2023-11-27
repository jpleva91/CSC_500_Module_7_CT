# constants for attribute keys
ROOM_NUMBER = 'room_number'
INSTRUCTOR = 'instructor'
MEETING_TIME = 'meeting_time'

# data dictionary with course information
data_dictionary = {
    'CSC101': {ROOM_NUMBER: '3004', INSTRUCTOR: 'Haynes', MEETING_TIME: '8:00 a.m.'},
    'CSC102': {ROOM_NUMBER: '4501', INSTRUCTOR: 'Alvarado', MEETING_TIME: '9:00 a.m.'},
    'CSC103': {ROOM_NUMBER: '6755', INSTRUCTOR: 'Rich', MEETING_TIME: '10:00 a.m.'},
    'NET110': {ROOM_NUMBER: '1244', INSTRUCTOR: 'Burke', MEETING_TIME: '11:00 a.m.'},
    'COM241': {ROOM_NUMBER: '1411', INSTRUCTOR: 'Lee', MEETING_TIME: '1:00 p.m.'}
}

# list of attributes to display in the course information
attributes_to_display = [ROOM_NUMBER, INSTRUCTOR, MEETING_TIME]


def format_label(label):
    # formats the attribute label into title case with spaces.
    return ' '.join(word.title() for word in label.replace('_', ' ').split())


def get_course_info(course_number):
    # returns a dictionary of course information for a given course number.
    return data_dictionary.get(course_number, {})


def print_course_info(course_number):
    # prints course information based on the specified attributes.
    course_info = get_course_info(course_number)
    if course_info:
        for attribute in attributes_to_display:
            formatted_label = format_label(attribute)
            print(f'{formatted_label}: {course_info.get(attribute, "Not available")}')
    else:
        print(f'No information available for course number: {course_number}')


if __name__ == '__main__':
    # Ask user for a course number and display the course's details
    print_course_info(input('Enter a course number: '))
