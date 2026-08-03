class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores indices [i]

        for i, t in enumerate(temperatures):
            # Resolve all previous days that are cooler than today's temperature
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            stack.append(i)

        return res