import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict ={}
        for i in nums:
            if i in dict:
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
        
        heap = []
        for key,value in dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
         
                
            else:
                heapq.heappushpop(heap , (value, key))
                
       

        return [item[1] for item in heap]
            
              
        