class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_changes = [0] * 101
        
        for birth, death in logs:
            population_changes[birth - 1950] += 1
            population_changes[death - 1950] -= 1

        max_population = 0
        year_of_max_population = 1950
        current_population = 0

        for year in range(101):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                year_of_max_population = 1950 + year

        return year_of_max_population
