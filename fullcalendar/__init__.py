VERSION = (0, 4)

def get_version():
    return '.'.join([str(i) for i in VERSION])

default_app_config = 'fullcalendar.apps.FullCalendarAppConfig'
