namespace CaloryCalculator.model
{
    class Meal
    {

        public string name;
             
        private System.Collections.Generic.List<Product> products;

        public Meal()
        {
            products = new System.Collections.Generic.List<Product>();
        }

        public Meal(string name) : this()
        {
            this.name = name;
        }

        public void AddProduct(Product product)
        {
            this.products.Add(product);
        }

        public void RemoveProduct(Product product)
        {
            this.products.Remove(product);
        }

        public override string ToString()
        {

            string meal = $"{nameof(Meal)} \'{this.name}\':\n";


            foreach (Product item in this.products) 
                meal += item.ToString() + "\n";
            
            return meal;
        }

    }
}
