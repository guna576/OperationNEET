from Observable.stocks_observable import StocksObservable
from Observer import NotificationObserver

class EmailNotificationObserver(NotificationObserver):
    observable: StocksObservable = None
    email_id: str = ""
    def __init__(self, observable: StocksObservable, email_id:str):
        self.observable = observable
        self.email_id = email_id

    def update():
        EmailNotificationObserver.send_mail(EmailNotificationObserver.email_id, "Product is in stock, Hurry up!")

    def send_mail(email_id, message):
        print(message)
        print("mail sent to: ", email_id)

    