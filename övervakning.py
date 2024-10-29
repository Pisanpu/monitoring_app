
import psutil
import time

class Monitoring_övervakning:
    def __init__(self, alarm_manager):
        self.active = False  # Status för övervakning
        self.alarm_manager = alarm_manager  # Använder den befintliga AlarmManager-instansen

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

        print(f"\nCPU Användning: {cpu_usage}%")
        print(f"Minne Användning: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB av {memory_info.total / (1024 ** 3):.2f} GB används)")
        print(f"Disk Användning: {disk_info.percent}% ({disk_info.used / (1024 ** 3):.2f} GB av {disk_info.total / (1024 ** 3):.2f} GB används)")

        for alarm in self.alarm_manager.alarms:
            if (alarm.type == 'CPU' and cpu_usage > alarm.level) or \
                (alarm.type == 'Minne' and memory_info.percent > alarm.level) or \
                (alarm.type == 'Disk' and disk_info.percent > alarm.level):
                print(f"***VARNING, LARM AKTIVERAT, {alarm.type} ANVÄNDNING ÖVERSTIGER {alarm.level}%***")