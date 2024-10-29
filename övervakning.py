import psutil
import time
from larm import AlarmManager

class Monitoring_övervakning:
    def __init__(self):
        self.active = False  # Status för övervakning
        self.alarm_manager = AlarmManager()  # Skapar en instans av AlarmManager

    def start(self):
        """Startar övervakning av systemresurser."""
        self.active = True
        print("Övervakning har startat.")
        while self.active:
            self.check_usage()  # Kontrollerar användning av resurser
            time.sleep(60)  # Väntar 60 sekunder mellan kontroller

    def stop(self):
        """Stoppar övervakning."""
        self.active = False

    def check_usage(self):
        """Kontrollerar och visar användning av CPU, minne och disk."""
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        print(f"CPU Användning: {cpu_usage}%")
        print(f"Minne Användning: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB out of {memory_info.total / (1024 ** 3):.2f} GB used)")
        print(f"Disk Användning: {disk_info.percent}% ({disk_info.used / (1024 ** 3):.2f} GB out of {disk_info.total / (1024 ** 3):.2f} GB used)")

        # Kontrollera larm
        for alarm in self.alarm_manager.alarms:
            if (alarm.type == 'CPU' and cpu_usage > alarm.level) or \
               (alarm.type == 'Minne' and memory_info.percent > alarm.level) or \
               (alarm.type == 'Disk' and disk_info.percent > alarm.level):
                print(f"***VARNING, LARM AKTIVERAT, {alarm.type} ANVÄNDNING ÖVERSTIGER {alarm.level}%***")

    def add_alarm(self, type, level):
        """Lägger till ett nytt larm."""
        self.alarm_manager.alarms.append(alarm(type, level))

    def list_alarms(self):
        """Visar konfigurerade larm."""
        self.alarm_manager.show_alarms()
