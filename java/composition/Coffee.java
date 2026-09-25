public class Coffee {

    private Beverage beverage;
    private String roastType;
    private boolean decaf;

    public Coffee(String roastType, int size,
                  boolean decaf, double price) {

        this.beverage =
            new Beverage("coffee", size, price);

        this.roastType = roastType;
        this.decaf = decaf;
    }

    public String getName() {
        return beverage.getName();
    }

    public int getSize() {
        return beverage.getSize();
    }

    public double getPrice() {
        return beverage.getPrice();
    }

    public String getRoastType() {
        return roastType;
    }

    public boolean isDecaf() {
        return decaf;
    }

    public String toString() {
        String item =
            roastType + " coffee (" +
            getSize() + " oz.) " +
            beverage.PriceFormat.format(getPrice());

        if (decaf) {
            return "decaf " + item;
        } else {
            return item;
        }
    }
}