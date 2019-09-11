from random import randint


def cube_test(string):
    user_cube2 = list(string)
    throws = []
    allowed_cubes = [3, 4, 6, 8, 10, 12, 20, 100]
    while " " in user_cube2:
        user_cube2.remove(" ")
    try:
        if "d" in user_cube2:
            if user_cube2.index("d") != 0:
                z = user_cube2.index("d")
                cube_throws = (int(''.join(user_cube2[0:z])))
                if "-" in user_cube2:
                    w = user_cube2.index("-")
                    cube_type = (int(''.join(user_cube2[z + 1:w])))
                    if cube_type in allowed_cubes:
                        cube_mod = (int(''.join(user_cube2[w + 1::])))
                        for _ in (range(cube_throws)):
                            rnd = randint(1, cube_type)
                            throws.append(rnd)
                        result = sum(throws) - cube_mod
                        return f"Result: {result}"
                    return "Cube not allowed!"
                elif "+" in user_cube2:
                    w = user_cube2.index("+")
                    cube_type = (int(''.join(user_cube2[z + 1:w])))
                    if cube_type in allowed_cubes:
                        cube_mod = (int(''.join(user_cube2[w + 1::])))
                        for _ in (range(cube_throws)):
                            rnd = randint(1, cube_type)
                            throws.append(rnd)
                        result = sum(throws) + cube_mod
                        return f"Result: {result}"
                    return "Cube not allowed!"
                else:
                    cube_type = (int(''.join(user_cube2[z + 1::])))
                    if cube_type in allowed_cubes:
                        for _ in (range(cube_throws)):
                            rnd = randint(1, cube_type)
                            throws.append(rnd)
                        result = sum(throws)
                        return f"Cube value: {result}"
                    return "Cube not allowed!"
            if user_cube2.index("d") == 0:
                if "-" in user_cube2:
                    w = user_cube2.index("-")
                    cube_type = (int(''.join(user_cube2[1:w])))
                    if cube_type in allowed_cubes:
                        print(f"Cube type: {cube_type}")
                        cube_mod = (int(''.join(user_cube2[w + 1::])))
                        cube_rand = randint(1, cube_type)
                        print(f"Cube mod: {cube_mod}")
                        print(f"Cube random: {cube_rand}")
                        result = cube_rand - cube_mod
                        return f"Result: {result}"
                    return "Cube not allowed!"
                elif "+" in user_cube2:
                    w = user_cube2.index("+")
                    cube_type = (int(''.join(user_cube2[1:w])))
                    if cube_type in allowed_cubes:
                        cube_mod = (int(''.join(user_cube2[w + 1::])))
                        cube_rand = randint(1, cube_type)
                        result = cube_rand + cube_mod
                        return f"Result: {result}"
                    return "Cube not allowed!"
                else:
                    cube_type = (int(''.join(user_cube2[1::])))
                    if cube_type in allowed_cubes:
                        cube_rand = randint(1, cube_type)
                        result = cube_rand
                        return f"Result: {result}"
                    return "Cube not allowed!"
        return "Provide correct cube type!"
    except ValueError:
        return "Provide correct cube type!"


print(cube_test(input("Provide the cube: ")))
