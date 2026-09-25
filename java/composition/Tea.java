public class Tea {

    private Beverage beverage;
    private String teaType;
    private boolean iced;

    public Tea(String teaType, int size,
               boolean iced, double price) {

        this.beverage =
            new Beverage("tea", size, price);

        this.teaType = teaType;
        this.iced = iced;
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

    public String getTeaType() {
        return teaType;
    }

    public boolean isIced() {
        return iced;
    }
}