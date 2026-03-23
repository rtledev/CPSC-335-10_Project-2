#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu

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

    # Return the minimum number of boats required
    return boats


def main():
    # Example 1 from the project sheet
    people1 = [3, 2, 2, 1]
    limit1 = 3

    # Example 2 from the project sheet
    people2 = [3, 5, 3, 4, 2, 2, 1, 4, 1]
    limit2 = 5

    # Print the required outputs
    print("Example 1 Output:", num_rescue_boats(people1, limit1))  # Expected: 3
    print("Example 2 Output:", num_rescue_boats(people2, limit2))  # Expected: 5

# Run main only if this file is executed directly
if __name__ == "__main__":
    main()
