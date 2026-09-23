import json
from yue2 import YuE2Pipeline

pipe = YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="mps")

styleWarmEnglish = "English, Indian accent, 80's style pop, expressive female voice, synthesizer, rounded bass and light drums, guitar, lyrical memorable melody, unhurried phrasing"

styleRockHindi = "Hindi, rock, aggressive male voice, electric guitar, bass, drums, energetic, driving rhythm, 120 BPM"


lyrics = """**Verse**
Morning light is shining through in Houston, USA,
Gaurav is cooking breakfast, starting off the day.
Kalpana’s getting ready for her dance class in style,
Mona’s finished yoga, heading to the office with a smile.

Ayush is going for a run, the youngest on the crew,
But with that mischievous little grin, what will he get up to?
“Hey Ayush, focus on your health, we’re telling you again,
Cut down on all that sugar, be the healthiest of men!”

**Chorus**
Oh, this is our family, scattered near and far,
Houston to Berlin, wherever we are.
Kalpana and Mona, Kuldeep too,
Siblings at heart, with a bond that stays true.
Ayush, less sugar, more healthy days,
And Kuldeep, maybe love is headed your way!
We may tease each other, but one thing’s always true,
No matter where life takes us, we’ll always come through.

**Bridge**
Gaurav flips the pancakes, “Breakfast is ready!”
Kalpana grabs her dance shoes, “Come on, let’s get steady!”
Mona checks the clock, “The office calls my name!”
Ayush runs a little faster, still playing his game!

From Houston’s sunny mornings to Berlin’s open roads,
Every mile they travel carries family loads.
Different dreams and different skies,
But the same old jokes and loving advice.

**Final Chorus**
Oh, this is our family, scattered near and far,
Houston to Berlin, shining like a star.
Gaurav and Kalpana, Mona and Ayush too,
Kuldeep on his bicycle, with a world to ride through.
Ayush, choose your health, let the sugar take a break,
Kuldeep, find some love, for goodness’ sake!
Laughing, teasing, caring—that’s the family way,
Together in our hearts, every single day.
"""

cot =  "off"
seed =  831001

request = json.loads(json.dumps({
    "style": styleWarmEnglish,
    "lyrics": lyrics,
    "cot": cot,
    "seed": seed,
}))

song = pipe(**request)
song.save_artifacts("outputs/my-song")
print(song.truncated)