from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # res array
        res = []

        # for email in list emails
        for email in emails:

            # split email with @: 'abc'@'xyz.com' -> ['abc', 'xyz.com']
            email_ = email.split("@")

            # local name pre processing
            if '.' in email_[0]:
                email_[0] = email_[0].split(".")
                email_[0] = ''.join(email_[0])
            if '+' in email_[0]:
                email_[0] = email_[0].split("+")[0]

            # join the list to make an email add string after pre processing
            tmp = "@".join(email_)

            # if after everything the email exists in res array, then skip it and dont add
            if tmp in res:
                continue
            # otherwise add
            else:
                res.append(tmp)
        # return length of res array
        return len(res)