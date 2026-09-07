import java.util.Scanner;

class UpperCaseInput {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your name:");
        String name = input.nextLine();
        
        System.out.println(name.toUpperCase());
    }
}
