import java.util.HashMap;
import java.util.Scanner;

public class ScoresHashMap {

    public static void main(String[] args) {

        HashMap<String, Integer> scores = new HashMap<>();

        scores.put("ssmith04", 88);
        scores.put("tlang01", 100);
        scores.put("glewis03", 99);

        System.out.println("Scores: " + scores);

        Scanner input = new Scanner(System.in);

        System.out.print("Enter an ID: ");

        String id = input.nextLine();

        if(scores.containsKey(id)) {

            int score = scores.get(id);

            System.out.println(
                id + " has a score of " + score + "."
            );

        }
        else {

            System.out.println(
                "There is no score for " + id + "."
            );
        }
    }
}
