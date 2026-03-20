import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {

        int n, first = 0, second = 1, next;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of N: ");
        n = sc.nextInt();

        System.out.println("Fibonacci Series till " + n + " terms:");

        for (int i = 1; i <= n; i++) {
            System.out.print(first + " ");

            next = first + second;
            first = second;
            second = next;
        }

        sc.close();
    }
}