import java.util.Arrays;

class PetsArraySort {

    public static void main(String[] args) {

        String[] petsArray = {
            "dog",
            "cat",
            "fish",
            "rabbit",
            "hamster",
            "bird"
        };

        int[] numbers = {1, 2, 3};

        String text = Arrays.toString(numbers);

        System.out.println("Array contents: " + Arrays.toString(numbers));

        System.out.println(
            "Original array: " + Arrays.toString(petsArray)
        );

        Arrays.sort(petsArray);

        System.out.println(
            "Sorted array: " + Arrays.toString(petsArray)
        );
    }
}
