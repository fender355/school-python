import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pomodoro_timer(total_pomodoros):
    study_time = 30 * 60  # 30 minutes
    short_break_time = 5 * 60  # 5 minutes
    pomodoro_count = 0

    while pomodoro_count < total_pomodoros:
        # Study time
        clear_screen()
        print(f"Pomodoro {pomodoro_count + 1}/{total_pomodoros}")
        print("Study Time!")
        countdown(study_time)

        # Short break
        clear_screen()
        print("Short Break!")
        countdown(short_break_time)

        pomodoro_count += 1

    clear_screen()
    print("Congratulations! You have completed all the pomodoros.")

def countdown(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time remaining: {timer}", end="\r")
        time.sleep(1)
        duration -= 1

# Entry point of the program
if __name__ == "__main__":
    clear_screen()
    print("Pomodoro Timer")
    total_pomodoros = int(input("Enter the total number of pomodoros: "))
    pomodoro_timer(total_pomodoros)
