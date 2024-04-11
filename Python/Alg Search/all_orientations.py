import json

orientations = ['', 'y', 'y2', "y'", 'z2', "z2 y'", 'x2', 'z2 y', 'x y2', "x y'", 'x', 'x y', "x'", "x' y", "x' y2", "x' y'", "z' y'", "z'", "z' y", "z' y2", 'z y', 'z y2', "z y'", 'z']

def inverse_alg(alg):
    if alg.strip() == "":
        return ""
    
    arr = []
    for a in alg.split(" "):
        if "'" in a:
            arr.insert(0, a[:-1])
        elif "2" in a:
            arr.insert(0, a)
        else:
            arr.insert(0, a + "'")
    
    inv_alg = " ".join(arr)
    return inv_alg

def get_moves_without_rotations(mvs):
    main_moves = ["U", "D", "R", "L", "F", "B"]

    def do_rotation(m, rot):
        if rot == "x":
            m[0], m[1], m[4], m[5] = m[4].lower(), m[5].lower(), m[1].lower(), m[0].lower()
        elif rot == "x'":
            m[0], m[1], m[4], m[5] = m[5].lower(), m[4].lower(), m[0].lower(), m[1].lower()
        elif rot == "x2":
            m[0], m[1], m[4], m[5] = m[1].lower(), m[0].lower(), m[5].lower(), m[4].lower()
        elif rot == "y":
            m[2], m[3], m[4], m[5] = m[5].lower(), m[4].lower(), m[2].lower(), m[3].lower()
        elif rot == "y'":
            m[2], m[3], m[4], m[5] = m[4].lower(), m[5].lower(), m[3].lower(), m[2].lower()
        elif rot == "y2":
            m[2], m[3], m[4], m[5] = m[3].lower(), m[2].lower(), m[5].lower(), m[4].lower()
        elif rot == "z":
            m[0], m[1], m[2], m[3] = m[3].lower(), m[2].lower(), m[0].lower(), m[1].lower()
        elif rot == "z'":
            m[0], m[1], m[2], m[3] = m[2].lower(), m[3].lower(), m[1].lower(), m[0].lower()
        elif rot == "z2":
            m[0], m[1], m[2], m[3] = m[1].lower(), m[0].lower(), m[3].lower(), m[2].lower()

        # Convert lower cases back to upper case
        return [x.upper() for x in m]

    # Replace wide moves with rotations
    mvs = mvs.replace("Uw2", "y2 D2").replace("Uw'", "y' D'").replace("Uw", "y D")\
             .replace("Dw2", "y2 U2").replace("Dw'", "y U'").replace("Dw", "y' U")\
             .replace("Rw2", "x2 L2").replace("Rw'", "x' L'").replace("Rw", "x L")\
             .replace("Lw2", "x2 R2").replace("Lw'", "x R'").replace("Lw", "x' R")\
             .replace("Fw2", "z2 B2").replace("Fw'", "z' B'").replace("Fw", "z B")\
             .replace("Bw2", "z2 F2").replace("Bw'", "z F'").replace("Bw", "z' F")\
             .replace("M2", "x2 R2 L2").replace("M'", "x R' L").replace("M", "x' R L'")\
             .replace("S2", "z2 F2 B2").replace("S'", "z' F B'").replace("S", "z F' B")\
             .replace("E2", "y2 U2 D2").replace("E'", "y U' D").replace("E", "y' U D'")\
             .replace("x", "_x").replace("y", "_y").replace("z", "_z")

    new_moves = []
    if mvs.split("_")[0].strip() != "":
        new_moves.append(mvs.split("_")[0].strip())

    for r in mvs.split("_")[1:]:
        if r.strip() != "":
            rot, rest = r.split(" ", 1)
            main_moves = do_rotation(main_moves, rot)
            translated = rest.replace("U", main_moves[0].lower())\
                            .replace("D", main_moves[1].lower())\
                            .replace("R", main_moves[2].lower())\
                            .replace("L", main_moves[3].lower())\
                            .replace("F", main_moves[4].lower())\
                            .replace("B", main_moves[5].lower())
            new_moves.append(translated.upper().replace("W", "w"))

    return " ".join(new_moves).strip()

def get_all_orientations(solutions: list[str]):
    all_orientations = {}
    for i, s in enumerate(solutions):
        all_orientations[i] = []
        for o in orientations:
            all_orientations[i].append({o: get_moves_without_rotations(inverse_alg(o) + " " + s)})

    return all_orientations

def do_rotation(m, rot):
    if rot == "x":
        m[0], m[1], m[4], m[5] = m[4].lower(), m[5].lower(), m[1].lower(), m[0].lower()
    elif rot == "x'":
        m[0], m[1], m[4], m[5] = m[5].lower(), m[4].lower(), m[0].lower(), m[1].lower()
    elif rot == "x2":
        m[0], m[1], m[4], m[5] = m[1].lower(), m[0].lower(), m[5].lower(), m[4].lower()
    elif rot == "y":
        m[2], m[3], m[4], m[5] = m[5].lower(), m[4].lower(), m[2].lower(), m[3].lower()
    elif rot == "y'":
        m[2], m[3], m[4], m[5] = m[4].lower(), m[5].lower(), m[3].lower(), m[2].lower()
    elif rot == "y2":
        m[2], m[3], m[4], m[5] = m[3].lower(), m[2].lower(), m[5].lower(), m[4].lower()
    elif rot == "z":
        m[0], m[1], m[2], m[3] = m[3].lower(), m[2].lower(), m[0].lower(), m[1].lower()
    elif rot == "z'":
        m[0], m[1], m[2], m[3] = m[2].lower(), m[3].lower(), m[1].lower(), m[0].lower()
    elif rot == "z2":
        m[0], m[1], m[2], m[3] = m[1].lower(), m[0].lower(), m[3].lower(), m[2].lower()

    # Convert lower cases back to upper case
    return [x.upper() for x in m]
    
print()
# if __name__ == "__main__":
#     solutions = [] # Liste med løsninger her
#     all_orientations = get_all_orientations(solutions)

#     with open('all_orientations.json', 'w') as file:
#         json.dump(all_orientations, file, indent=4, sort_keys=True)