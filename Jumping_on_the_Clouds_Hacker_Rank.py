# Complete the jumpingOnClouds function below.
# Only concered about jumping from safe index to safe index.
def jumpingOnClouds(c):

    i=0
    min_steps = 0
    steps = c[1]

    for i in list(steps):
        if steps[i+2] == 0:
            min_steps += 1
            print(steps[i+2])

    return min_steps

num_clouds = 7
describing_clouds = [0,0,1,0,0,1,0]
c = [num_clouds, describing_clouds]

print(jumpingOnClouds(c))
