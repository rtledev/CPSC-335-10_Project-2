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
