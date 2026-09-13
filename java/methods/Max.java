/* Author: Sophia
   Created Date: Feb 07, 2022
   Description: This program has 2 methods to find the maximum value of 3 numbers.
   Example of usage: maxOfThree(20, 30, -10)
   Result: method returns 30
*/

public class Max {

    public static int maxOfTwo(int firstNumber, int secondNumber) {
        if (firstNumber > secondNumber) {
            return firstNumber;
        }
        return secondNumber;
    }

    public static int maxOfThree(int firstNumber, int secondNumber, int thirdNumber) {
        return maxOfTwo(firstNumber, maxOfTwo(secondNumber, thirdNumber));
    }

    public static void main(String[] args) {
        System.out.println("Highest number is " + maxOfThree(20, 30, -10) + ".");
    }
}
