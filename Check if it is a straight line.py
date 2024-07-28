class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        d_x = coordinates[1][0] - coordinates[0][0]
        d_y = coordinates[1][1] - coordinates[0][1]

        for i in range(2,len(coordinates)):
            d_x_i = coordinates[i][0] - coordinates[0][0]
            d_y_i = coordinates[i][1] - coordinates[0][1]
            if(d_x*d_y_i!=d_x_i*d_y):
                return False
        return True
