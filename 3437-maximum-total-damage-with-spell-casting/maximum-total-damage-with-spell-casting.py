class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        unique_powers = sorted(counts.keys())
        n = len(unique_powers)
        dp = [0] * n
        j = -1 
        
        for i in range(n):
            current_power = unique_powers[i]
            
            while j + 1 < i and unique_powers[j + 1] < current_power - 2:
                j += 1

            damage_if_taken = current_power * counts[current_power]
            if j >= 0:
                damage_if_taken += dp[j]

            damage_if_skipped = dp[i-1] if i > 0 else 0
            
            dp[i] = max(damage_if_taken, damage_if_skipped)
            
        return dp[-1] if dp else 0