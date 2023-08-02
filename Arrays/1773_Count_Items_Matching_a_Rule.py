# https://leetcode.com/problems/count-items-matching-a-rule/
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Array contains items[i] = [typei, colori, namei]
        Counts the number of items that match the rule.
        The ith item is said to match the rule if one of the following is true:
            ruleKey == "type" and ruleValue == typei.
            ruleKey == "color" and ruleValue == colori.
            ruleKey == "name" and ruleValue == namei
        :param items:
        :param ruleKey:
        :param ruleValue:
        :return:

        Switch case which checks a rule key, then loops over the array and checks value
        """
        key = None
        counter = 0
        match ruleKey:  # Assigns proper key
            case "type":
                key = 0
            case "color":
                key = 1
            case "name":
                key = 2

        for item in items:
            # Counts arrays that mach ruleValue
            if item[key] == ruleValue:
                counter += 1

        return counter
