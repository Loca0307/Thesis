namespace AdventOfCode.Day03;

public class Day03
{
    private readonly string[] _input;

    public Day03(string[] input)
    {
        _input = input;
    }

    public int Part1()
    {
        var schema = Array.ConvertAll(_input, line => line.ToCharArray());

        var sumParts = 0;

        for (var x = 0; x < schema.Length; x++)
        {
            var y = 0;
            while (y < schema[x].Length)
            {
                if (char.IsDigit(schema[x][y]))
                {
                    var number = schema[x][y].ToString();
                    var length = 1;

                    while (y + length < schema[x].Length && char.IsDigit(schema[x][y + length]))
                    {
                        number += schema[x][y + length];
                        length++;
                    }

                    if (IsAdjacentToSymbol(number, x, y, schema))
                    {
                        sumParts += int.Parse(number);
                    }

                    y += length;
                }
                else
                {
                    y++;
                }
            }
        }

        return sumParts;
    }

    public int Part2()
    {
        var schema = Array.ConvertAll(_input, line => line.ToCharArray());
        var sumRatios = 0;

        for (var x = 0; x < schema.Length; x++)
        {
            for (var y = 0; y < schema[x].Length; y++)
            {
                if (!IsGear(schema[x][y])) continue;

                var adjacentNumbers = new HashSet<int>();
                foreach (var (adjX, adjY) in GetAdjacentCells(x, y, schema.Length, schema[0].Length))
                {
                    if (!char.IsDigit(schema[adjX][adjY])) continue;

                    var number = FindNumbers(schema, adjX, adjY);
                    if (number != -1)
                    {
                        adjacentNumbers.Add(number);
                    }
                }

                if (adjacentNumbers.Count == 2)
                {
                    var gearRatio = 1;
                    foreach (var num in adjacentNumbers)
                    {
                        gearRatio *= num;
                    }
                    sumRatios += gearRatio;
                }
            }
        }

        return sumRatios;
    }

    private static bool IsSymbol(char c) => char.IsLetter(c) || "$*+-/=&#%@".Contains(c);

    private static bool IsGear(char c) => "*".Contains(c);

    private static int FindNumbers(IReadOnlyList<char[]> schema, int x, int y)
    {
        while (y > 0 && char.IsDigit(schema[x][y - 1]))
        {
            y--;
        }

        var number = "";
        while (y < schema[x].Length && char.IsDigit(schema[x][y]))
        {
            number += schema[x][y];
            y++;
        }
        return number.Length > 0 ? int.Parse(number) : -1;
    }

    private static List<(int, int)> GetAdjacentCells(int x, int y, int maxX, int maxY)
    {
        var adjacent = new List<(int, int)>();
        for (var dx = -1; dx <= 1; dx++)
        {
            for (var dy = -1; dy <= 1; dy++)
            {
                if (dx == 0 && dy == 0) continue;
                int newX = x + dx, newY = y + dy;
                if (newX >= 0 && newX < maxX && newY >= 0 && newY < maxY)
                {
                    adjacent.Add((newX, newY));
                }
            }
        }
        return adjacent;
    }

    private static bool IsAdjacentToSymbol(string number, int x, int y, IReadOnlyList<char[]> schema)
    {
        var length = number.Length;
        for (var i = 0; i < length; i++)
        {
            foreach (var (adjX, adjY) in GetAdjacentCells(x, y + i, schema.Count, schema[0].Length))
            {
                if (IsSymbol(schema[adjX][adjY])) return true;
            }
        }

        return false;
    }
}