public class SayHelloRepeated {

    static String sayHello(String name, int count) {

        String greeting = "";

        for (int i = 0; i < count; i++) {
            greeting += "Hello, " + name + "\n";
        }

        return greeting;
    }

    public static void main(String[] args) {

        String userName = "Sophia";

        String greetingOutput = sayHello(userName, 3);

        System.out.println(greetingOutput);
    }
}
