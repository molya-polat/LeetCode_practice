class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_diction = {}
        email_name = {}
        for records in accounts:
            name = records[0]
            email = records[1]
            emails = records[2:]
            if email not in email_diction:
                email_diction[email] = set()
                email_name[email] = name

            for e in emails:
                email_diction[email].add(e)
                if e not in email_diction:
                    email_diction[e] = set()
                email_diction[e].add(email)
                email_name[e] = name

        def dfs(account):
            visited.add(account)
            ans = [account]
            if account in email_diction:
                neighbors = email_diction[account]
                
                for n in neighbors:
                    if n not in visited:
                        ans.extend(dfs(n))
            
            return ans

        email_groups = []    
        visited = set()
        for account in email_name.keys():
            if account not in visited:
                accounts_connected = dfs(account)
                email_groups.append(accounts_connected)
        answer = []
        for group in email_groups:
            result = [email_name[group[0]]]
            sorted_emails = sorted(group)
            result.extend(sorted_emails)
            answer.append(result)

        return answer
    # O(n * m) - time
    # O(n * m) - space
        

        




            

                

            
        






        # ans = []
        # diction = {}

        # def haveSimilarEmails(emails1, emails2):
        #     for email in emails1:
        #         if email in emails2:
        #             return True
            
        #     return False


        # for record in accounts:
        #     name = record[0]
        #     accounts_list = record[1:]
        #     if name in diction:
        #         foundSimilar = False
        #         for email_set in diction[name]:
        #             haveSimilarEmail = haveSimilarEmails(accounts_list, email_set)
        #             if haveSimilarEmail:
        #                 email_set.update(accounts_list)
        #                 foundSimilar = True
        #                 break
        #         if not foundSimilar:
        #             diction[name].append(set(accounts_list))
        #     else:
        #         diction[name] = [set(accounts_list)]

        # # for name, sets in diction.items():
        # #     for i in range(len(sets) - 1):
        # #         for j in range(i + 1, len(sets)):
        # #             haveSimilar = haveSimilarEmails(sets[i], sets[j])
        # #             if haveSimilar:
                        

        # for name, sets in diction.items():
        #     for email_set in sets:
        #         sorted_email = sorted(list(email_set))
        #         array = [name]
        #         array.extend(sorted_email)
        #         ans.append(array)
        
        # return ans