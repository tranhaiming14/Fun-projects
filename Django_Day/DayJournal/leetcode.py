class Solution(object):
    def trap(self, height):
        res = 0
        first = 0
        last = len(height) - 1
        while height[first] == 0:
            first += 1
        while height[last] == 0:
            last -= 1
        for i in range(first + 1, last):
            left = i - 1
            right = i + 1
            max_left = left
            max_right = right
            while left - 1 >= first:
                left -= 1
                if height[left] > height[max_left]:
                    max_left = left
            while right + 1 <= last:
                right += 1
                if height[right] > height[max_right]:
                    max_right = right
            n = max(min(height[max_left], height[max_right]) - height[i], 0)
            res += n

        return res    
solution = Solution()
height = [4,2,0,3,2,5]

print(solution.trap(height))

#second
class Solution(object):
    def trap(self, height):
        res = 0
        first = 0
        last = len(height) - 1
        while first == 0:
            first += 1
        while last == 0:
            last -= 1
        for i in range(first + 1, last):
            left = i - 1
            right = i + 1
            max_left = left
            max_right = right
            while left - 1 >= first and height[left - 1] >= height[left] and height[left - 1] >= height[i]:
                left -= 1
            while right + 1 <= last and height[right + 1] >= height[right] and height[right + 1] >= height[i]:
                right += 1
            n = max(min(height[left], height[right]) - height[i], 0)
            res += n

        return res