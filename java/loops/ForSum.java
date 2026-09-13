import java.util.Arrays;

class ForSum {
    public static void main(String[] args) {
        int[] numbers = {3, 41, 12, 9, 74, 15};
        int sum = 0;

        for (int index = 0; index < numbers.length; index++) {
            sum += numbers[index];
        }

        System.out.print("The sum of the values in the array ");
        System.out.print(Arrays.toString(numbers));
        System.out.println(" = " + sum + ".");
    }
}
