class OverloadMethod {

    public static void main(String[] args) {

        // Java chooses sayHello(String)
        String result = sayHello("Sophia");
        System.out.println(result + "\n");


        // Java chooses sayHello(String, int)
        result = sayHello("Sophia", 3);
        System.out.println(result + "\n");


        // Create an array
        String[] firstNames = {
            "John",
            "Sophia",
            "Mary",
            "Kim"
        };

        // Java chooses sayHello(String[])
        result = sayHello(firstNames);
        System.out.println(result);
    }


    // OVERLOAD #1
    // Receives one String
    static String sayHello(String name) {
        return "Hello, " + name;
    }


    // OVERLOAD #2
    // Receives a String AND an int
    static String sayHello(String name, int count) {

        String greeting = "";

        for (int i = 0; i < count; i++) {
            greeting += "Hello, " + name + "\n";
        }

        return greeting;
    }


    // OVERLOAD #3
    // Receives an array of Strings
    static String sayHello(String[] names) {

        String greeting = "";

        for (String name : names) {
            greeting += "Hello, " + name + "\n";
        }

        return greeting;
    }
}
