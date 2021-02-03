# Complete the jumpingOnClouds function below.
# Only concered about jumping from safe index to safe index.
def jumpingOnClouds(c):
    min_steps = i = 0
    if c[0] == 1: return min_steps # One Cloud.
    while i < c[0]: # Stepping through all clouds.
        try: # Handlin out of range exception.
            if c[1][i+2] == 0: # Looking forward two steps.
                min_steps += 1
                i += 2
            else: # Knowing we can only move one step.
                min_steps += 1
                i +=1
        except: # Because we known we've moved out of the index.
            if c[1][i+1] == 0: min_steps += 1
            return min_steps
    return min_steps


num_clouds = 6
describing_clouds = [0,0,0,1,0,0]
c = [num_clouds, describing_clouds]

print(jumpingOnClouds(c))
