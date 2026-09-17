class NestedLoop {

    public static void main(String[] args) {

        for (int outer = 1; outer <= 3; outer++) {

            for (int inner = 1; inner <= 2; inner++) {

                System.out.println(
                    "outer = " + outer
                    + ", inner = " + inner
                );
            }
        }
    }
}