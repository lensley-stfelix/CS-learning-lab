public class Dog {
    private String name;
    private String breed;
    private int age;
    private String color;

    public Dog(String name, String breed, int age, String color) {
        this.name = name;
        this.breed = breed;
        this.age = age;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public String getBreed() {
        return breed;
    }

    public int getAge() {
        return age;
    }

    public String getColor() {
        return color;
    }

    public void bark() {
        System.out.println("Woof!");
    }

    public void fetch() {
        System.out.println(name + " went to fetch.");
    }
}
