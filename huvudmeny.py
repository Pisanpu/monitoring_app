from övervakning import Monitoring_övervakning
from larm import Alarm, AlarmManager

class Monitoring:
    def __init__(self):
        self.active = False  # Status för övervakning
        self.alarm_manager = AlarmManager()  # Skapar en instans av AlarmManager
    
    def list_alarms(self):
        """Visar aktiva larm."""
        if not self.alarm_manager.alarms:
            print("Inga aktiva alarm.")
        else:
            print("Aktiva alarm:")
            for alarm in self.alarm_manager.alarms:
                print(f"{alarm.type} - Nivå: {alarm.level}%")

    def start(self):
        """Startar övervakning."""
        self.active = True
        print("Övervakning har startat.")
        # Logik för att börja övervakningen...

    def stop(self):
        """Stoppar övervakning."""
        self.active = False
        print("Övervakning har stoppats.")
        # Logik för att stoppa övervakningen...
    @staticmethod
    def main_menu():
        """Visa huvudmenyn och hantera användarinteraktion."""
        monitor = Monitoring()  # Skapar en instans av Monitoring
    
        while True:
            print("Välj ett alternativ:")
            print("1. Starta övervakning")
            print("2. Lista aktiv övervakning")
            print("3. Skapa larm")
            print("4. Visa larm")
            print("5. Avsluta")

            choice = input("Ange ditt val: ")

            if choice == '1':
                monitor.start()  # Startar övervakning
            elif choice == '2':
                monitor.list_alarms()  # Visar aktiva övervakningar
                input("Tryck valfri tangent för att gå tillbaka till huvudmeny.")
            elif choice == '3':
                AlarmManager.create_alarm_menu()  # Öppnar meny för att skapa larm
            elif choice == '4':
                monitor.list_alarms()  # Visar larm
                input("Tryck valfri tangent för att gå tillbaka till huvudmeny.")
            elif choice == '5':
                print("Avslutar programmet.")  # Avslutar programmet
                break
            else:
                print("Ogiltigt val, försök igen.")  # Felmeddelande för ogiltigt val

    def create_alarm_menu(self):
        """Visar menyn för att skapa larm."""
        while True:
            print("Välj typ av larm:")
            print("1. CPU användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("4. Tillbaka till huvudmeny")

            choice = input("Ange ditt val: ")
            if choice in ['1', '2', '3']:
                Monitoring.set_alarm_level(choice)  # Sätter larmnivå
                break
            elif choice == '4':
                break
            else:
                print("Ogiltigt val, försök igen.")  # Felmeddelande för ogiltigt val

    def set_alarm_level(self, choice):
        """Ställ in larmnivån."""
        while True:
            try:
                level = int(input("Ställ in nivå för alarm mellan 0-100: "))  # Frågar efter larmnivå
                if 0 <= level <= 100:
                    Monitoring_övervakning.add_alarm('CPU' if choice == '1' else 'Minne' if choice == '2' else 'Disk', level)
                    print(f"Larm för {'CPU' if choice == '1' else 'Minne' if choice == '2' else 'Disk'} användning satt till {level}%.")
                    break
                else:
                    print("Nivån måste vara mellan 0 och 100.")  # Felmeddelande för ogiltig nivå
            except ValueError:
                print("Ogiltig inmatning. Vänligen ange ett heltal.")  # Felmeddelande för ogiltig inmatning


