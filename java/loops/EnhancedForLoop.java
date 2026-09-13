class EnhancedForLoop {
    public static void main(String[] args) {
        int[] numbers = {3, 41, 12, 9, 74, 15};
        int sum = 0;

        for (int number : numbers) {
            sum += number;
        }

        System.out.println("Sum = " + sum);
    }
}
