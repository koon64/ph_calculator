import math


def from_ph(ph):
    h = math.pow(10, -1 * ph)
    poh = 14 - ph
    vals = {
            "ph": ph,
            "h": h,
            "poh": poh,
            "oh": math.pow(10, -1 * poh)
            }
    disp(vals)

def from_h(h):
    from_ph(-1 * math.log(h))

def from_poh(o_oh):
    from_ph(14 - o_oh)

def from_oh(oh):
    from_poh(-1 * math.log(oh))

def disp(nums):
    print("PH:", nums["ph"])
    print("H+:", nums["h"])
    print("pOH:", nums["poh"])
    print("OH-:", nums["oh"])
    if nums["ph"] > 7:
        print("B")
    else:
        print("A")

import os

while True:
    os.system("clear")
    print("Enter things")
    print()
    ph = input("Ph:")
    if ph:
        from_ph(float(ph))
    else:
        h = input("H:")
        if h:
            from_h(float(h))
        else:
            poh = input("pOH:")
            if poh:
                from_poh(float(poh))
            else:
                from_oh(float(input("OH:")))




