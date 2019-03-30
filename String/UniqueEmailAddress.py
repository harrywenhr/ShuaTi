https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        filteredEmails = set()
        for i in range(len(emails)):
            localName = emails[i].split("@")[0]
            domainName = emails[i].split("@")[1]
            localName = localName.split("+")[0]
            localName = localName.replace(".","")
            newEmail = localName + "@" + domainName
            filteredEmails.add(newEmail)
        return len(filteredEmails)