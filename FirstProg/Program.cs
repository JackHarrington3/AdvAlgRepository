namespace FirstProg;
class Program
{
    static void Main(string[] args)
    {
        int[] numbers = new int[10];
        string[] names = new string[10];
        string myName = "McCue";
        int myAge = 55;
        //Console.WriteLine("Hello, " + myName + "!\nYou will be " +
        //(myAge + 10) + " years old in a decade.");

        //for (int x = 0; x < 10; x++)
        //    Console.WriteLine(x + ".");

        numbers[0] = 99;
        //Console.WriteLine(numbers[0] + "," + numbers[9]);
        names[0] = "gavin";
        //Console.WriteLine(names[0] + "," + names[9] + "," + names[0]);

        Random rnd = new Random();
        int diceRoll = rnd.Next(10);
        //Console.WriteLine(diceRoll);

        //for (int x = 0; x < numbers.Length; x++)
        //    numbers[x] = rnd.Next(10);
        
        bool found = false;
        //int count = 0;  //This ends up being too small a placeholder
        UInt64 count = 0;
        int counterCount = 0;
        while (!found) {
            count++;
            if (count == 18446744073709551614) {
                counterCount++;
                count = 0;
            }
            for (int x = 0; x < numbers.Length; x++)
                numbers[x] = rnd.Next(10);
            int sum = 0;
            for (int x = 0; x < numbers.Length; x++)
                sum = sum + numbers[x];
            int avg = sum/numbers.Length;
            if (avg == 9)
                found = true;
            if (count % 100000 == 0)
                Console.Write(".");
            if (count % 7000000 == 0)
                Console.WriteLine(".");
        }
        Console.WriteLine("# of tries: " + count);
        Console.WriteLine("# of overflows: " + counterCount);
        
    }
}
