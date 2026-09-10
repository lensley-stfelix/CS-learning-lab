import java.util.Arrays;

class FinalArray {

    public static void main(String[] args) {

        final int[] numbers = {1, 2, 3};

        System.out.println(
            "Original: " + Arrays.toString(numbers)
        );

        // Modify individual elements
        numbers[0] = 4;
        numbers[1] = 5;
        numbers[2] = 6;

        System.out.println(
            "Modified: " + Arrays.toString(numbers)
        );

        // This would NOT work:
        // numbers = new int[]{7, 8, 9};
    }
}
