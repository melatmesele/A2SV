class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         [seat][][seat][][seat][][][]
#         pp    move 1   
#                   pp    move 1     
#                          pp  move 2   total = 1 + 1 +2 = 4moves
#         [seat][][][seat][seat][][][][seat]
#          pp  move = 0 
#                          pp move = 3
#                    pp move= 1
#                                       pp move= 3    total= 0+3+1+3 = 7
#         1,4,5,9
#          [seat][][][seat][seat][][][][seat]
#           pp move=0
          
#         1 ,2 ,3 ,6   
#           pp    
            
        seats.sort()
        students.sort()
        ans = 0
        for i in range(len(seats)):
            ans+= abs(seats[i] - students[i])
        return ans            
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        seats.sort() 
        students.sort()
        
        res = 0 # variable to store the result
        
        for i in range(len(seats)): 
            res += abs(students[i] - seats[i]) # calculating diff of both the list and adding it to the variable , rather then adding it to the list, and then to traverse that list for the total moves.
            
        return res
                