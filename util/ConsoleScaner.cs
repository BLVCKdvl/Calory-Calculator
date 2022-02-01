using System;

namespace CaloryCalculator
{
    class ConsoleScaner
    {

        public static string InputString(string invitation="")
        {
            Printer.Print(invitation);
            return Console.ReadLine();
        }

    }
}
