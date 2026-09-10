import java.util.Arrays;

class BinarySearch {

    public static void main(String[] args) {

        // Create array
        int[] scores = {77, 89, 100, 68, 95};

        // Value we're looking for
        int searchValue = 100;

        // Binary search requires sorted data
        Arrays.sort(scores);

        System.out.println(
            "Sorted Array: " + Arrays.toString(scores)
        );

        // Search and capture the returned index
        int location =
            Arrays.binarySearch(scores, searchValue);

        // Nonnegative index means it was found
        if(location >= 0) {

            System.out.println(
                searchValue + " found."
            );

        }
        else {

            System.out.println(
                searchValue + " not found."
            );
        }
    }
}
