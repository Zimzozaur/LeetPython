# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        holder = set()
        for email in emails:
            email = email.split("@")
            host = email[0].split("+")[0]
            domain = email[1][:-4]
            host = host.replace(".", "")
            holder.add(host + "@" + domain)
        return len(holder)

if __name__ == '__main__':
    sol = Solution()
    x = ["test.email+alex@lee.tcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    sol.numUniqueEmails(x)