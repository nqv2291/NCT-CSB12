if character["Level"] >= skills[inp-1]["Minimum Level"]:
    if rate <= skills[inp-1]["Hit Rate"]:
        print(f"""Damage: {skills[inp-1]["Damage"]}""")
    else:
        print("Missed")
else:
    print(f"""Cannot deploy. Required level {skills[inp-1]["Minimum Level"]}""")