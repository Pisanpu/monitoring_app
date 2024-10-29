from huvudmeny import Monitoring
from felhantering import handle_error

if __name__ == "__main__":
    try:
        Monitoring.main_menu()  # Startar huvudmenyn
    except Exception as e:
        handle_error(f"Ett oväntat fel inträffade: {str(e)}")  # Hanterar eventuella fel

