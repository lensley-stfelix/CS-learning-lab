import java.util.Arrays;

class ArrayCopyOfRange {

    public static void main(String[] args) {

        // Original array
        int[] scores = {77, 89, 100, 68, 95};

        System.out.println(
            "Original: " + Arrays.toString(scores)
        );

        // Sort from lowest to highest
        Arrays.sort(scores);

        System.out.println(
            "Sorted: " + Arrays.toString(scores)
        );

        // Copy the last three elements
        // into a NEW array
        int[] topThree = Arrays.copyOfRange(
            scores,
            scores.length - 3,
            scores.length
        );

        System.out.println(
            "Top 3: " + Arrays.toString(topThree)
        );
    }
}
