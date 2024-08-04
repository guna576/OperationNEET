# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.


from abc import ABC, abstractmethod
class SendMessage(ABC):
    @abstractmethod
    def send(self, msg: str):
        pass 

class EmailNotification(SendMessage):
    def send(self, msg: str):
        print("Email sent to the user: ", msg)

class SMSNotification(SendMessage):
    def send(self, msg: str):
        print("SMS Notification sent to the suer: ", msg)


class Notification:
    def __init__(self, service: SendMessage):
        self.service = service

    def send_message(self, msg: str):
        self.service.send(msg)

email_message = EmailNotification()
sms_notification = SMSNotification()

email_notify = Notification(email_message)
sms_notify = Notification(sms_notification)

email_notify.send_message("File Scan Successful")
sms_notify.send_message("File Scan Successful ra Hukka")