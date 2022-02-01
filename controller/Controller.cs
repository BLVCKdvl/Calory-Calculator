
using CaloryCalculator.model;

namespace CaloryCalculator
{
    class Controller
    { 
        public static void test()
        {
            Product p1 = new Product("ананас");
            Product p2 = new Product("абрикос");

            Meal meal = new Meal("Салат");

            meal.AddProduct(p1);
            meal.AddProduct(p2);
            meal.AddProduct(new Product("груша"));
            Printer.Print(meal);

            meal.RemoveProduct(p2);

            Printer.Print(meal);


        }
    }
}
