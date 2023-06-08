public class Solution {
    public string AddBinary(string a, string b) {
    //     int lengthA = a.Length - 1;
    //     int lengthB = b.Length - 1;
    //     int temp = 0;
    //     bool isPlusOne = false;
    //     StringBuilder result = new StringBuilder("");
    //     while (lengthA >= 0 || lengthB >= 0){
    //         if (lengthA < 0 && lengthB >= 0){
    //             temp = Int32.Parse(b[lengthB].ToString());
    //         }
    //         else if(lengthB < 0 && lengthA >= 0){
    //             temp = Int32.Parse(a[lengthA].ToString());
    //         }
    //         else{
    //             temp = Int32.Parse(a[lengthA].ToString()) + Int32.Parse(b[lengthB].ToString());
    //         }   

    //         if (isPlusOne) temp++;
    //         if(temp == 2) {
    //             temp = 0;
    //             isPlusOne = true;
    //         }
    //         else if(temp == 3){
    //             temp = 1;
    //             isPlusOne = true;
    //         }
    //         else{
    //             isPlusOne = false;
    //         }
    //         result.Insert(0, temp.ToString());
    //         lengthA--;
    //         lengthB--;
    //     }
    //     if (isPlusOne)  result.Insert(0, "1");
    //   return result.ToString();
        var resultBuilder = new StringBuilder();
        int i = a.Length - 1, j = b.Length - 1;
        int carriage = 0;

        for(; i >= 0 || j >= 0; i--, j--)
        {
            carriage += (i >= 0 ? a[i] - 48 : 0);     // 48 -> '0'
            carriage += (j >= 0 ? b[j] - 48 : 0);    // 48 -> '0'

            resultBuilder.Insert(0, carriage % 2);
            carriage = carriage / 2;

        }

        if(carriage > 0)
            resultBuilder.Insert(0, carriage);
        
        return resultBuilder.ToString();

    }
}