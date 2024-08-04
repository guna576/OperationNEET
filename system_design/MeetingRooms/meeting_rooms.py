from datetime import datetime

class MeetingRooms:
    def __init__(
            self, 
            id: int, 
            name: str,
            capacity: int
    ):
        self.id = id 
        self.name = name 
        self.capacity = capacity
        self.schedule = []
    
    def is_available(
            self,
            start_time: datetime,
            end_time: datetime,
    ):
        for meeting_interval in self.schedule:
            if start_time < meeting_interval[1] and end_time > meeting_interval[0]:
                return False
        return True 
    
    def book_room(
            self,
            start_time: datetime,
            end_time: datetime,
    ):
        if self.is_available(start_time=start_time, end_time=end_time):
            self.schedule += [(start_time, end_time)]
            return True 
        return False