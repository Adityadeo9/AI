# Water Jug Problem
# Jugs: 4 Litres and 3 Litres
# Goal: Measure exactly 2 Litres

def water_jug():
    jug4 = 0
    jug3 = 0

    print("Initial State:", (jug4, jug3))

    # Fill 3L jug
    jug3 = 3
    print("Fill 3L:", (jug4, jug3))

    # Pour 3L into 4L
    jug4 = jug3
    jug3 = 0
    print("Pour 3L -> 4L:", (jug4, jug3))

    # Fill 3L jug again
    jug3 = 3
    print("Fill 3L:", (jug4, jug3))

    # Pour 3L into 4L until 4L is full
    jug3 = 2
    jug4 = 4
    print("Pour 3L -> 4L:", (jug4, jug3))

    print("\nGoal Reached!")
    print("4L Jug =", jug4, "Litres")
    print("3L Jug =", jug3, "Litres")


water_jug()