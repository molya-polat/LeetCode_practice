public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        var weakness = new int [k];
        var dictionaryRowsAndSoldiers = new Dictionary<int, int>();
    for (int i = 0; i < mat.Length; i++){
        int soldiers = 0;
    
        for (int j = 0; j < mat[i].Length; j++){
            if (mat[i][j] == 1){
                soldiers ++;
            }
            else{
                break;
            }       
        }
        dictionaryRowsAndSoldiers.Add(i, soldiers);
    }
    var sorted = dictionaryRowsAndSoldiers.OrderBy (x => x.Value);    
    int counter = 0;    
    foreach(var d in sorted){     
        weakness[counter] = d.Key;
        counter++;
        if (counter == k){
            return weakness;
        }
    }
    return null;
}
}