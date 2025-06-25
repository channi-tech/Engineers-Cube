user_input = input("how are you feeling today?")
mood = user_input.strip().lower()
if mood == "happy":
    print("\U0001F60A I'm glad to hear that! Keep smiling!")
elif mood == "sad":
    print("\U0001F614 It's okay to feel sad sometimes. I'm here for you .")
elif mood == "tired":
    print("\U0001F4A4 Take some rest, you deserve it .")
else:
    print("\U0001F917 Whatever you're feeling, you're doing great. Keep going!")
