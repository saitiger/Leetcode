class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill_sum = sum(skill)

        num_teams = n // 2  # Number of teams

        # Check if total skill can be evenly distributed
        if skill_sum % num_teams != 0:  # Skills can't be equally amongst the teams
            return -1

        target = skill_sum // num_teams  # Total Skill divided by number of teams
        mpp = Counter(skill)
        ans = 0

        # Iterate through unique skill values
        for skill1, freq in mpp.items():
            skill2 = target - skill1
            
            # Check if valid partner skill exists with matching frequency
            if skill2 not in mpp or freq != mpp[skill2]:
                return -1

            # Calculate chemistry for all pairs with this skill
            ans += skill1 * skill2 * freq

        # Return half of total chemistry (as each pair is counted twice)
        return ans // 2
