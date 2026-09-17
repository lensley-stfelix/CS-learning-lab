public class SayHelloArray {

    static String sayHello(String[] names) {

        String greeting = "";

        for (String name : names) {
            greeting += "Hello, " + name + "\n";
        }

        return greeting;
    }

    public static void main(String[] args) {

        String[] userNames = {
            "Sophia",
            "Sofia",
            "Sophie"
        };

        String greetingOutput = sayHello(userNames);

        System.out.println(greetingOutput);
    }
}
