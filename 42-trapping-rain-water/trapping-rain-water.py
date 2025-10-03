class Solution:
    def trap(self, height: List[int]) -> int:
        
        total=0

        stack=[]
        first=0
        for i, h in enumerate(height):
            while stack and h>height[stack[-1]]:
                curr=stack.pop()

                if not stack:
                    break
                
                left=stack[-1]

                width=i-left-1

                total+=(min(height[left],h)-height[curr])*width
            stack.append(i)

        return total


