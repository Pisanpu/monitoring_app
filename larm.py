

class Alarm:
    def __init__(self, type, level):
        self.type = type  # Typ av larm
        self.level = level  # Nivå för larm

    def __str__(self):
        return f"{self.type} larm {self.level}%"  # Strängrepresentation av larm

class AlarmManager:
    def __init__(self):
        self.alarms = []  # Lista för att hålla larm

    def create_alarm(self):
        """Skapar ett nytt larm baserat på användarens val."""
        print("Välj typ av larm:")
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmeny")
        
        choice = input("Ange ditt val: ")
        
        if choice in ['1', '2', '3']:
            try:
                level = int(input("Ställ in nivå för alarm mellan 0-100: "))  # Frågar efter larmnivå
                if 0 <= level <= 100:
                    type_alarm = 'CPU' if choice == '1' else 'Minne' if choice == '2' else 'Disk'
                    self.alarms.append(Alarm(type_alarm, level))
                    print(f"Larm för {type_alarm} användning satt till {level}%.")
                else:
                    print("Nivån måste vara mellan 0 och 100.")  # Felmeddelande för ogiltig nivå
            except ValueError:
                print("Ogiltig inmatning. Vänligen ange ett heltal.")  # Felmeddelande för ogiltig inmatning
        elif choice == '4':
            return
        else:
            print("Ogiltigt val, försök igen.")  # Felmeddelande för ogiltigt val

    def show_alarms(self):
        """Visar alla konfigurerade larm sorterade efter typ."""
        if not self.alarms:
            print("Inga larm har skapats än.")  # Meddelande om inga larm
        else:
            for alarm in sorted(self.alarms, key=lambda x: x.type):
                print(alarm)  # Visar varje larm


