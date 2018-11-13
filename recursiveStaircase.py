
# This program tells the user how many ways they walk up a staircase of any size given they take steps in 1, 2, or 3 step incrememnts
def main():
    num_steps = input("How many steps are on your staircase? ")
    num_steps = int(num_steps)
    print "There are", countPaths(num_steps), "ways to walk up", num_steps, "steps if you walk in 1, 2, or 3 step increments"

def countPaths (steps):
    memo = [1,1,2]  # use memoization and an iterative approach to save memory and time
    if steps <0:
        return None
    if(steps <= 2):  # our initial memoization table takes care of such small staircases
        return memo[steps]
    for i in range (3, steps+1):
        count = memo[0] + memo[1] + memo[2]  # number of paths up k steps is the sum of the number of paths up (k-1), (k-2), (k-3) steps
        memo[0] = memo[1]
        memo[1] = memo[2]
        memo[2] = count  # update our memoization to keep (k-1), (k-2), and (k-3)
    return memo[2]  # memo[2] at the end will have the number of ways to get up k steps since it takes count





if __name__ == '__main__': main()
