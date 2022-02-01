namespace CaloryCalculator.model
{
    class Product
    {
        public string name;
        public uint amountOfCalories; // per 100 gramms


        public Product()
        {
            
        }

        public Product(string name)
        {
            this.name = name;
        }

        public Product(string name, uint amountOfCalories)
        {
            this.name = name;
            this.amountOfCalories = amountOfCalories;
        }

        public override string ToString()
        {
            return $"Product {this.name} -- {this.amountOfCalories}";
        }
    }
}
