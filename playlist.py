liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    },
    "Pearls": {
        "artist": "Sade",
        "duration": (4, 35),
        "genre": "Soul"
    },
    "Wicked Game": {
        "artist": "Chris Isaak",
        "duration": (4, 47),
        "genre": "Rock"
    },
    "Forget Her": {
        "artist": "Jeff Buckley",
        "duration": (5, 14),
        "genre": "Alternative"
    }
}





def main():
    print("Updated playlist with details:\n")
    for song_name, details in liked_songs.items():
        print(f"Title: {song_name}")
        print(f"  Artist: {details['artist']}")
        print(f"  Duration: {details['duration'][0]}:{details['duration'][1]:02d}")
        print(f"  Genre: {details['genre']}\n")

    # בדיקת שיר והסרה
    song_name = input("Enter the name of the song you want to check: ")

    if song_name in liked_songs:
        print(f"The song '{song_name}' is in the playlist.")
        remove = input("Do you want to remove it? (yes/no): ")
        if remove.lower() == "yes":
            del liked_songs[song_name]
        else:
            print("The song remains in the playlist.")
    else:
        print(f"The song '{song_name}' is not in the playlist.")

    # הסרת כל השירים של אמן מסוים
    artist_to_remove = input("\nEnter the name of an artist to remove all their songs: ")
    liked_songs_copy = {song: details for song, details in liked_songs.items() if details['artist'] != artist_to_remove}
    liked_songs.clear()
    liked_songs.update(liked_songs_copy)
    print(f"All songs by '{artist_to_remove}' have been removed.\n")

    # הדפסת הפלייליסט המעודכן
    print("Playlist after updates:")
    for name in liked_songs:
        print(name)

# קריאה לפונקציה
main()