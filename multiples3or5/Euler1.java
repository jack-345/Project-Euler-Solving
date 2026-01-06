// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. 
// The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

public class Euler1 {
    public static void main(String[] args) {
        // calculate below n of 1000 so decrement to 999
        int n = 1000;
        n--;

        int sum = 0;
        int totalElements = 0;

        if (n >= 3) {
            totalElements = n/3;
            sum += (totalElements * (3 + totalElements*3))/2;
        }

        if (n >= 5) {
            totalElements = n/5;
            sum += (totalElements * (5 + totalElements*5))/2;
        }

        if (n >= 15) {
            totalElements = n/15;
            sum -= (totalElements * (15 + totalElements*15))/2;
        }
        System.out.println(sum);
    }
}
