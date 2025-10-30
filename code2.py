import java.util.Scanner;

class EvenThread extends Thread {
    int[] numbers;

    EvenThread(int[] numbers) {
        this.numbers = numbers;
    }

    public void run() {
        for (int n : numbers) {
            if (n % 2 == 0) {
                System.out.println(n);
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    System.out.println(e);
                }
            }
        }
    }
}

class OddThread extends Thread {
    int[] numbers;

    OddThread(int[] numbers) {
        this.numbers = numbers;
    }

    public void run() {
        for (int n : numbers) {
            if (n % 2 != 0) {
                System.out.println(n);
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    System.out.println(e);
                }
            }
        }
    }
}

public class ExtendingThread {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = new int[10];
        System.out.println("Enter 10 numbers:");
        for (int i = 0; i < 10; i++) {
            numbers[i] = sc.nextInt();
        }

        EvenThread even = new EvenThread(numbers);
        OddThread odd = new OddThread(numbers);

        even.start();
        odd.start();
    }
}
