class NestedLoopsEnhanced {

    public static void main(String[] args) {

        int[][] numbers = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int rowNumber = 1;
        int colNumber = 1;

        // Get each row
        for (int[] row : numbers) {

            // Get each value inside current row
            for (int value : row) {

                System.out.println(
                    "Row: " + rowNumber
                    + " Col: " + colNumber++
                    + " = " + value
                );
            }

            // New row → restart column count
            colNumber = 1;

            // Move display counter to next row
            rowNumber++;
        }
    }
}