import java.util.Arrays;

public class GenericMethod {

    // T represents an object type.
    // The method receives an array of T
    // and returns one element of type T.
    public static <T> T getMidPointItem(T[] array) {

        return array[array.length / 2];
    }

    public static void main(String[] args) {

        String[] names = {
            "Ann", "George", "Kim", "Pat", "Steve"
        };

        String midPointName = getMidPointItem(names);

        System.out.print(
            "The middle item in the array "
            + Arrays.toString(names)
        );

        System.out.println(
            " is " + midPointName + "."
        );

        Character[] letters = {'a', 'b', 'c'};

        char midPointLetter = getMidPointItem(letters);

        System.out.print(
            "The middle item in the array "
            + Arrays.toString(letters)
        );

        System.out.println(
            " is " + midPointLetter + "."
        );

        Integer[] agesInYears = {
            27, 33, 33, 39, 40, 40, 42, 45
        };

        int midPointAge = getMidPointItem(agesInYears);

        System.out.print(
            "The middle item in the array "
            + Arrays.toString(agesInYears)
        );

        System.out.println(
            " is " + midPointAge + "."
        );

        Double[] temperatures = {
            10.0, 21.5, 22.3, 25.0, 31.85, 35.99
        };

        double midPointTemp =
            getMidPointItem(temperatures);

        System.out.print(
            "The middle item in the array "
            + Arrays.toString(temperatures)
        );

        System.out.println(
            " is " + midPointTemp + "."
        );
    }
}
