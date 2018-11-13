from datetime import datetime


class Event:
    dict = {}

    def __init__(self, id, name, image, time):
        self.__id = id
        self.__name = name
        self.__image = image
        self.__time = time

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__image

    def get_time_str(self):
        return self.__time.strftime('%d %b, %H:%M')

    @staticmethod
    def get_dict():
        dict = Event.dict
        if len(dict) == 0:
            e1 = Event(
                1,
                'Guitar Club Annual Concert',
                'https://www.nyp.edu.sg/content/dam/nyp/campus-life/cca-activities-and-events/student-clubs-and-interest-groups/events/2018/guitar-annual-concert/thumb_guitar_concert.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg',
                datetime.strptime('23/11/18, 19:00', '%d/%m/%y, %H:%M')
            )
            dict[e1.get_id()] = e1
            e2 = Event(
                2,
                'Food Safety In Action',
                'https://www.nyp.edu.sg/content/dam/nyp/schools-course/scl/events/2018/foodsafety/foodsafety.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg',
                datetime.strptime('29/11/18, 08:45', '%d/%m/%y, %H:%M')
            )
            dict[e2.get_id()] = e2
            e3 = Event(
                3,
                'NYP Groove! Street Dance Competition',
                'https://www.nyp.edu.sg/content/dam/nyp/campus-life/school-events/2018/nypgroove/groove-eventbrite-event-page-banner.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg',
                datetime.strptime('03/12/18, 10:00', '%d/%m/%y, %H:%M')
            )
            dict[e3.get_id()] = e3
            e4 = Event(
                4,
                'NYP Jam! Singing Competition',
                'https://www.nyp.edu.sg/content/dam/nyp/campus-life/school-events/2018/nypjam/nyp-jam-event-listing-banner.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg',
                datetime.strptime('04/12/18, 09:00', '%d/%m/%y, %H:%M')
            )
            dict[e4.get_id()] = e4
        return dict