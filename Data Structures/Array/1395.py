class Solution:
    def numTeams(self, rating: List[int]) -> int:
        elements_greater_than_current_rating = len(rating)*[0]
        elements_less_than_current_rating = len(rating)*[0]
        number_of_teams = 0
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    elements_less_than_current_rating[i] += 1
                if rating[j] > rating[i]:
                    elements_greater_than_current_rating[i] += 1
        # print ("elements_greater_than_current_rating: %s" % elements_greater_than_current_rating)
        # print ("elements_less_than_current_rating: %s" % elements_less_than_current_rating)
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    if (elements_greater_than_current_rating[j] > 0):
                        number_of_teams += elements_greater_than_current_rating[j]
                if rating[j] < rating[i]:
                    if (elements_less_than_current_rating[j] > 0):
                        number_of_teams += elements_less_than_current_rating[j]
        return number_of_teams