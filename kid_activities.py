def run(name):
    return f"{name} is running from their problems!"
    

def swing(name):
    return f"{name} is a swinger!"
    

def slide(name):
    return f"{name} slid into your DM's!"
    

def hide_and_seek(name):
    return f"{name} is hiding from their demons and seeking short term happiness."
    

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


for kid in hiding_kids:
    print(hide_and_seek(kid))


for kid in sliding_kids:
    print(slide(kid))


for kid in running_kids:
    print(run(kid))


for kid in swinging_kids:
    print(swing(kid))