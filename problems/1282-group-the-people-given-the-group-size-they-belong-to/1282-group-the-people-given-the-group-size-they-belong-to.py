class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        personGroups = []
        diction = {}
        for person, size in enumerate(groupSizes):
            if size in diction:
                # diction[size] = diction[size] + [person]
                diction[size].append(person)
            else:
                diction[size] = [person]

        for size, persons in diction.items():
            groupSize = len(persons)
            if groupSize > size:
                miniGroups = groupSize // size
                while miniGroups > 0:
                    personGroups.append(persons[:size])
                    persons = persons[size:]
                    miniGroups -= 1
            else:
                personGroups.append(persons)
        
        return personGroups

# O(n^2) - time complexity
# O(n) - spacr complexity