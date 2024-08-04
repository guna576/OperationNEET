from Observable.stocks_observable import StocksObservable
from Observer.notification_observer import NotificationObserver

class IphoneObservable(StocksObservable):
    observer_list = []
    stock_count = 0

    def add(observer: NotificationObserver):
        IphoneObservable.observer_list += [observer]

    def remove(observer: NotificationObserver):
        IphoneObservable.observer_list.remove(observer)

    def notify():
        for observer in IphoneObservable.observer_list:
            observer.update()

    def set_stock_item_count(new_stock_count):
        if IphoneObservable.stock_count == 0: 
            IphoneObservable.notify()
        IphoneObservable.stock_count += new_stock_count

    def get_stock_item_count():
        return IphoneObservable.stock_count
    

