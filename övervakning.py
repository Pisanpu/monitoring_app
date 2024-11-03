
import psutil  
import time    

class Monitoring_övervakning:
    def __init__(self, alarm_manager):
        self.active = False  # Status för övervakning
        self.alarm_manager = alarm_manager  # Använder den befintliga AlarmManager-instansen

    def check_usage_simple(self):
        """Visar enkel användning av CPU, minne och disk."""
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        print(f"CPU: {cpu_usage}%")  # Visar CPU-användning
        print(f"Minne: {memory_info.percent}%")  # Visar minnesanvändning
        print(f"Disk: {disk_info.percent}%")  # Visar diskens användning

    def start_alarm_check(self):
        """Startar en loop som kontrollerar larm kontinuerligt."""
        print("Startar larmkontroll...")  # Meddelande om att larmkontrollen har startat
        try:
            while True:
                self.check_alarms()  # Kontrollerar om något larm har triggats
                time.sleep(60)  # Väntar 60 sekunder mellan kontroller
        except KeyboardInterrupt:
            print("\nLarmkontroll avslutad.")  # Meddelande om att kontrollen har avslutats

    def check_alarms(self):
        """Kontrollerar om något larm har triggats."""
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        for alarm in self.alarm_manager.alarms:
            if (alarm.type == 'CPU' and cpu_usage > alarm.level) or \
                (alarm.type == 'Minne' and memory_info.percent > alarm.level) or \
                (alarm.type == 'Disk' and disk_info.percent > alarm.level):
                print(f"***VARNING, LARM AKTIVERAT, {alarm.type} ANVÄNDNING ÖVERSTIGER {alarm.level}%***")  # Varningsmeddelande vid larmaktivering