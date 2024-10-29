from övervakning import Monitoring_övervakning
from larm import AlarmManager
import threading
import time

class Monitoring:
    def __init__(self):
        self.active = False  # Status för övervakning
        self.alarm_manager = AlarmManager()  # Skapar en instans av AlarmManager
        self.monitoring = Monitoring_övervakning(self.alarm_manager)
        self.monitoring_thread = None

    def start(self):
        """Startar övervakning."""
        if not self.active:
            self.active = True
            self.monitoring_thread = threading.Thread(target=self.monitoring.start)
            self.monitoring_thread.start()
            print("Övervakning har startat.")
        else:
            print("Övervakning är redan aktiv.")
                
    def run_monitoring(self):
        while self.active:
            self.monitoring.check_usage()
            time.sleep(60)     # Vänta 60 sekunder mellan verifikationer 

    def stop(self):
        """Stoppar övervakning."""
        if self.active:
            self.active = False
            self.monitoring.stop()
            if self.monitoring_thread:
                self.monitoring_thread.join()
            print("Övervakning har stoppats.")
        else:
            print("Ingen aktiv övervakning att stoppa.")

    @staticmethod
    def main_menu():
        """Visa huvudmenyn och hantera användarinteraktion."""
        monitor = Monitoring()
    
        while True:
            print("\nVälj ett alternativ:")
            print("1. Starta övervakning")
            print("2. Lista aktiv övervakning")
            print("3. Skapa larm")
            print("4. Visa larm")
            print("5. Avsluta")

            choice = input("Ange ditt val: ")

            if choice == '1':
                monitor.start()
            elif choice == '2':
                if monitor.active:
                    monitor.monitoring.check_usage()
                else:
                    print("Ingen övervakning är aktiv.")
                input("Tryck valfri tangent för att gå tillbaka till huvudmeny.")
            elif choice == '3':
                monitor.alarm_manager.create_alarm()
            elif choice == '4':
                monitor.alarm_manager.show_alarms()
                input("Tryck valfri tangent för att gå tillbaka till huvudmeny.")
            elif choice == '5':
                monitor.stop()
                print("Avslutar programmet.")
                break
            else:
                print("Ogiltigt val, försök igen.")
                