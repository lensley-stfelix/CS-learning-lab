import java.util.Arrays;

class ArraySort {

    public static void main(String[] args) {

        // Create the array
        int[] scores = {77, 89, 100, 68, 95};

        // Display original array
        System.out.println(
            "Scores: " + Arrays.toString(scores)
        );

        // Sort smallest to largest
        Arrays.sort(scores);

        // Display sorted array
        System.out.println(
            "Sorted Scores: " + Arrays.toString(scores)
        );

        // Find the number of elements
        int size = scores.length;

        System.out.println(
            "Array Size: " + size
        );

        // First element = lowest after sorting
        System.out.println(
            "Lowest Score: " + scores[0]
        );

        // Last valid index = length - 1
        int lastIndex = size - 1;

        // Last element = highest after sorting
        System.out.println(
            "Highest Score: " + scores[lastIndex]
        );
    }
}
