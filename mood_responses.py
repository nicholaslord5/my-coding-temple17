 # mood_responses.py
def mood_response(mood):
        mood = mood.lower()
        if mood == "happy":
            return "That's awesome! Keep the good times rolling!"
        elif mood == "sad" or mood == "down":
            return "It's ok, we all feel that way sometimes. Wanna talk about it?"
        elif mood == "angry" or mood == "mad":
            return "What's got you upset? Would you like to do some breathing exercises?"
        elif mood == "nervous" or mood == "anxious":
            return "If you'd like, sometimes it helps to occupy your time with other activities, or go for a walk outside."
        elif mood == "panic" or mood == "panicked":
            return "It's going to be all right. Try breathing as slow and deep as you can."
        elif mood == "excited":
            return "Fantastic! I'm excited for you, too!"
        elif mood == "tired" or mood == "sleepy":
            return "Sounds like it's time for bed or a nap. Breaks are good and necessary. Sit back and relax a bit."
        else:
            return "That's ok. Would you like to talk about whatever is on your mind?"