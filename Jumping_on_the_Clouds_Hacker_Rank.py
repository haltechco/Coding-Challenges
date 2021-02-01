# Complete the jumpingOnClouds function below.
# Only concered about jumping from safe index to safe index.
def jumpingOnClouds(c):
    min_steps = i = 0
    if c[0] == 1: return min_steps # One Cloud.
    while i < (c[0]-1):
        if c[1][i+2] == 0:
            min_steps += 1
            i += 2
        else:
            min_steps += 1
            i +=1

    return min_steps


num_clouds = 3
describing_clouds = [0,1,1]
c = [num_clouds, describing_clouds]

print(jumpingOnClouds(c))
