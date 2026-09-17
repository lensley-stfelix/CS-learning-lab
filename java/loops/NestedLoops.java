class NestedLoops {

    public static void main(String[] args) {

        int[][] numbers = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Move through each row
        for (int row = 0;
             row < numbers.length;
             row++) {

            // Move through each column
            // inside the current row
            for (int col = 0;
                 col < numbers[row].length;
                 col++) {

                System.out.println(
                    "Row: " + (row + 1)
                    + " Col: " + (col + 1)
                    + " = " + numbers[row][col]
                );
            }
        }
    }
}