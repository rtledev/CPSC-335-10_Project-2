#Pseudo 
Algorithm NumRescueBoats(people, limit)

Input:
    people = array of people's weights
    limit = maximum weight a boat can carry

Output:
    Minimum number of boats needed

1. Sort people in nondecreasing order
2. Set left = 0
3. Set right = length of people - 1
4. Set boats = 0

5. While left <= right:
       If people[left] + people[right] <= limit:
            left = left + 1
            right = right - 1
       Else:
            right = right - 1

       boats = boats + 1

6. Return boats

#Python 
# CPSC 335 - Project 2
# Problem 2: Boats to Save People
# Name: Arman Madatyan, 


def num_rescue_boats(people, limit):
    # Sort the weights from lightest to heaviest
    people.sort()

    # Two pointers: one at the lightest, one at the heaviest
    left = 0
    right = len(people) - 1

    # Count how many boats we use
    boats = 0

    # Keep pairing people until all are assigned a boat
    while left <= right:
        # If the lightest and heaviest person can fit together,
        # put them in the same boat
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            # Otherwise, the heaviest person goes alone
            right -= 1

        # In either case, we used one boat
        boats += 1

    return boats


def main():
    # Simple test case
    people = [3, 2, 2, 1]
    limit = 3

    # Print result
    print(num_rescue_boats(people, limit))


if __name__ == "__main__":
    main()
