import java.util.Arrays;

class ForCountEven {
    public static void main(String[] args) {
        int[] numbers = {3, 41, 12, 9, 74, 15};
        int evenCount = 0;

        for (int index = 0; index < numbers.length; index++) {
            if (numbers[index] % 2 == 0) {
                evenCount++;
            }
        }

        System.out.print("The array " + Arrays.toString(numbers) + " ");
        System.out.println("contains " + evenCount + " even values.");
    }
}
