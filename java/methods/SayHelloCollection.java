import java.util.ArrayList;

public class SayHelloCollection {

    static <T> String sayHello(ArrayList<T> names) {

        String greeting = "";

        for (T name : names) {
            greeting += "Hello, " + name + "\n";
        }

        return greeting;
    }

    public static void main(String[] args) {

        ArrayList<String> userNames = new ArrayList<>();

        userNames.add("Sophia");
        userNames.add("Sophie");
        userNames.add("Sophie");

        String greetingOutput = sayHello(userNames);

        System.out.println(greetingOutput);
    }
}
