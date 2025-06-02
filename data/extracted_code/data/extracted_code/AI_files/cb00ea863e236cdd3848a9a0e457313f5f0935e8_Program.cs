Console.WriteLine();


/*
 search for a name in the array
display 'found' if the name is in the array
display 'not found' if the name is not in the array
 */

if (Array.BinarySearch(names, "Alfa") >= 0)
{
    Console.WriteLine("Found");
}
else
{
    Console.WriteLine("Not Found");
}
Console.WriteLine();

// search for a name in the array and display the location of the name
Console.WriteLine(Array.BinarySearch(names, "Alfa"));
Console.WriteLine();


