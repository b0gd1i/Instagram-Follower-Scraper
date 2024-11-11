import os
from instaloader import Instaloader, Profile
from datetime import datetime
from time import sleep

def fetch_followers_and_followees(username):
    instaloader = Instaloader()
    
    session_file = os.path.join(os.path.expanduser("~"), "Desktop", "instagram_sessionfile")
    try:
        instaloader.load_session_from_file(username, session_file)
        print("Sesiunea a fost încărcată cu succes.")
    except Exception as e:
        print(f"Eroare la încărcarea sesiunii: {e}")
        return

    try:
        profile = Profile.from_username(instaloader.context, username)
    except Exception as e:
        print(f"Eroare la accesarea profilului utilizatorului: {e}")
        return

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    timestamp = datetime.now().strftime("%d.%m.%Y_%H.%M")
    followers_file = os.path.join(desktop_path, f"{username}_followers_{timestamp}.txt")
    followees_file = os.path.join(desktop_path, f"{username}_followees_{timestamp}.txt")
    
    try:
        print("Preiau lista de urmăritori...")
        followers = profile.get_followers()
        followers_list = list(followers)
        print(f"Număr de urmăritori preluați: {len(followers_list)}")

        with open(followers_file, 'w') as f:
            for follower in followers_list:
                f.write(f'{follower.username}\n')
                sleep(0.2)
    except Exception as e:
        print(f"Eroare la preluarea urmăritorilor: {e}")
    
    try:
        print("Preiau lista de urmăriți...")
        followees = profile.get_followees()
        followees_list = list(followees)
        print(f"Număr de urmăriți preluați: {len(followees_list)}")

        with open(followees_file, 'w') as f:
            for followee in followees_list:
                f.write(f'{followee.username}\n')
                sleep(0.2)
    except Exception as e:
        print(f"Eroare la preluarea urmăriților: {e}")

    print(f"Listele au fost salvate în fișierele:\n{followers_file}\n{followees_file}")

if __name__ == "__main__":
    username = input("Introdu username-ul contului Instagram: ")
    fetch_followers_and_followees(username)
