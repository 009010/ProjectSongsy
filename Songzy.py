import random

#ของเพลงตามอารมณ์(เพลงฝรั่ง)
songs = {
    "เศร้า": [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "The Night We Met - Lord Huron",
        "Tears In Heaven - Eric Clapton",
        "Hurt - Johnny Cash"
    ],
    "ดีใจ": [
        "Happy - Pharrell Williams",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Can't Stop The Feeling! - Justin Timberlake",
        "Walking On Sunshine - Katrina and the Waves",
        "Good Life - OneRepublic"
    ],
    "ชิวๆ": [
        "Sunflower - Post Malone, Swae Lee",
        "Banana Pancakes - Jack Johnson",
        "Better Together - Jack Johnson",
        "Budapest - George Ezra",
        "Put It All On Me - Ed Sheeran"
    ],
    "อกหัก": [
        "Back To December - Taylor Swift",
        "The One That Got Away - Katy Perry",
        "I Will Always Love You - Whitney Houston",
        "Somebody That I Used To Know - Gotye",
        "Creep - Radiohead"
    ],
    "ตื่นเต้น": [
        "Eye of the Tiger - Survivor",
        "Lose Yourself - Eminem",
        "Stronger - Kanye West",
        "Thunder - Imagine Dragons",
        "Can't Hold Us - Macklemore & Ryan Lewis"
    ],
    "เบื่อ": [
        "The Lazy Song - Bruno Mars",
        "Stressed Out - Twenty One Pilots",
        "Bored to Death - Blink-182",
        "Take It Easy - Eagles",
        "I Don't Want to Miss a Thing - Aerosmith"
    ],
    "หลงรัก": [
        "Perfect - Ed Sheeran",
        "Just The Way You Are - Bruno Mars",
        "All of Me - John Legend",
        "I Don't Want to Miss a Thing - Aerosmith",
        "Kiss Me - Sixpence None The Richer"
    ],
    "สนุก": [
        "Party Rock Anthem - LMFAO",
        "Shake It Off - Taylor Swift",
        "I Gotta Feeling - The Black Eyed Peas",
        "Roar - Katy Perry",
        "Dynamite - BTS"
    ],
    "หวั่นไหว": [
        "Maybe - Ingrid Michaelson",
        "Adore You - Harry Styles",
        "Bleeding Love - Leona Lewis",
        "Chasing Cars - Snow Patrol",
        "All I Want - Kodaline"
    ],
    "ใจเย็น": [
        "Weightless - Marconi Union",
        "Breathe Me - Sia",
        "The Scientist - Coldplay",
        "River Flows In You - Yiruma",
        "Clocks - Coldplay"
    ],
    "โกรธ": [
        "Breaking the Habit - Linkin Park",
        "Smells Like Teen Spirit - Nirvana",
        "You Oughta Know - Alanis Morissette",
        "Killing In The Name - Rage Against the Machine",
        "Give It Away - Red Hot Chili Peppers"
    ]
}
#randomเพลงจากอารมณ์ที่เลือก
def recommend_song(mood):
    if mood in songs:
        return random.choice(songs[mood])
    else:
        return "ไม่มีเพลงสำหรับอารมณ์นี้"

# ตัวอย่างการใช้
mood = input("บอกอารมณ์ของคุณ (เศร้า, ดีใจ, ชิวๆ, อกหัก, ตื่นเต้น, เบื่อ, หลงรัก, สนุก, หวั่นไหว, ใจเย็น, โกรธ): ")
song = recommend_song(mood)
print(f"เพลงที่แนะนำสำหรับอารมณ์ '{mood}': {song}")
