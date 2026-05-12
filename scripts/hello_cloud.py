"""
hello_cloud.py
My first Python script — a tiny tool every engineer needs.
Shows the current date, time, and a friendly motivation message.
"""

from datetime import datetime
import platform

def main():
    now = datetime.now()
    today = now.strftime("%A, %d %B %Y")
    time_now = now.strftime("%H:%M:%S")
    machine = platform.system()
    
    print("=" * 50)
    print("☁️  Cloud Journey — Daily Check-in")
    print("=" * 50)
    print(f"📅 Date: {today}")
    print(f"⏰ Time: {time_now}")
    print(f"💻 Machine: {machine}")
    print("=" * 50)
    print("Today's goal: Show up. Build something. Push it.")
    print("=" * 50)

if __name__ == "__main__":
    main()