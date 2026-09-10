import java.util.Arrays;

class Scores2DArray {

    public static void main(String[] args) {

        int[][] scores = {
            {100, 92, 99, 85},
            {100, 95, 88, 91},
            {99, 100, 100, 100}
        };

        System.out.println(Arrays.deepToString(scores));

        System.out.println(
            "First student's scores: "
            + Arrays.toString(scores[0])
        );

        System.out.println(
            "1st student, 3rd score: "
            + scores[0][2]
        );
    }
}
