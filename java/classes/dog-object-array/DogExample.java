public class DogExample {
    public static void main(String[] args) {
        Dog[] myDog = new Dog[3];

        myDog[0] = new Dog("Fluffy", "Beagle", 2, "Brown");
        myDog[1] = new Dog("Mochi", "Mutt", 5, "White");
        myDog[2] = new Dog("Wolfie", "Maltese", 10, "Black");

        System.out.println(myDog[0].getName());
        System.out.println(myDog[1].getName());
        System.out.println(myDog[2].getName());

        myDog[0].bark();
        myDog[1].fetch();
    }
}
