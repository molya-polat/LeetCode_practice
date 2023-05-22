public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        var dic = new Dictionary<int, List<string>>();

        dic.Add(1, new List<string>{"()"});
        dic.Add(2, new List<string>{"()()", "(())"});

        for (int i = 3; i <= n; i++){
            GenerateParenthesisList(i, dic);
        }

        return dic[n];
    }

    private List<string> GenerateParenthesisList(int n, Dictionary<int, List<string>> dic){
        if (dic.ContainsKey(n)) return dic[n];

        var set = new HashSet<string>();

        var prev =  GenerateParenthesisList(n - 1, dic);
        for (int i = 0; i < prev.Count; i++){
            set.Add("(" + prev[i] + ")");   //outside closed
        }

        for (int j = 1; j < n; j++){
            var firstPart = GenerateParenthesisList(j, dic);   
            var secondPart = GenerateParenthesisList(n - j, dic);

            for(int p = 0; p < firstPart.Count; p++){
                for(int d = 0; d < secondPart.Count; d++){
                    if(!set.Contains(firstPart[p] + secondPart[d]))  //each combination of strings
                         set.Add(firstPart[p] + secondPart[d]);
                }
            }
        }
        var list = set.ToList();
        if (!dic.ContainsKey(n)) dic.Add(n, list);
        return list;

    }
}