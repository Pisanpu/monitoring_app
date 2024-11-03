from övervakning import Monitoring_övervakning
from larm import AlarmManager
from felhantering import handle_error

class Monitoring:
    @staticmethod
    def main_menu():
        alarm_manager = AlarmManager()
        monitoring = Monitoring_övervakning(alarm_manager)

        while True:
            print("\nHuvudmeny:")
            print("1. Starta övervakning")
            print("2. Visa nuvarande användning")
            print("3. Hantera larm")
            print("4. Visa alla larm")
            print("5. Starta larmkontroll")
            print("6. Avsluta")

            choice = input("Välj ett alternativ: ")

            if choice == '1':
                print("Övervakning har startat.")  # Meddelande om att övervakningen har startat
            elif choice == '2':
                monitoring.check_usage_simple()  # Visar enkel användning av resurser
            elif choice == '3':
                alarm_manager.create_alarm()  # Hanterar larm
            elif choice == '4':
                alarm_manager.show_alarms()  # Visar alla konfigurerade larm
            elif choice == '5':
                monitoring.start_alarm_check()  # Startar kontroll av larm
            elif choice == '6':
                print("Avslutar programmet...")  # Avslutar programmet
                break
            else:
                print("Ogiltigt val, försök igen.")  # Felmeddelande för ogiltigt val

if __name__ == "__main__":
    try:
        Monitoring.main_menu()  # Startar huvudmenyn
    except Exception as e:
        handle_error(f"Ett oväntat fel inträffade: {str(e)}")  # Hanterar eventuella fel