from meeting_rooms import MeetingRooms
from notification_service import NotificationService
from users import Users
from datetime import datetime
from typing import List

class Meeting(MeetingRooms):
    def __init__(
            self,
            meeting_id: int,
            meeting_room: int,
            start_time: datetime,
            end_time: datetime,
            invitees: int,
    ):
        self.meeting_id = meeting_id
        self.meeting_room = meeting_room
        self.start_time = start_time
        self.end_time = end_time
        self.invitees = invitees


    def schedule_meeting(
            self
    ):
        if self.book_room(
            start_time=self.start_time,
            end_time=self.end_time
        ):
            for invitee in self.invitees:
                NotificationService.notify_users(user:, )
            return True 
        return False