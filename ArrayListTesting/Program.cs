// See https://aka.ms/new-console-template for more information
using System.Collections;

Console.WriteLine("Hello, World!");

ArrayList myArr = new ArrayList();

myArr.Add("mccue");
myArr.Add(55);
Node firstNode = new Node();
myArr.Add(firstNode);

Console.WriteLine(myArr);

foreach (var item in myArr)
    Console.WriteLine(item + ", "); //output: 1, Bill, 300, 4.5, 

myArr.Reverse();
            
for(int i = 0 ; i < myArr.Count; i++)
    Console.WriteLine(myArr[i] + ", "); 