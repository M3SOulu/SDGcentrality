import java.text.DecimalFormat;
public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");
        // Mortgage details
        double principal = 200000;   // Principal amount
        double annualInterestRate = 5.0; // Annual interest rate (as a percentage)
        int loanTermYears = 5;     // Loan term in years

        // Calculate monthly interest rate
        double monthlyInterestRate = (annualInterestRate / 100) / 12;

        // Calculate the number of monthly payments
        int numberOfPayments = loanTermYears * 12;

        // Calculate monthly mortgage payment using formula:
        // M = P * (r(1+r)^n) / ((1+r)^n - 1)
        double monthlyPayment = principal * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments))
                / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);

        // Display the mortgage repayment plan
        DecimalFormat df = new DecimalFormat("#.##");
        System.out.println("Mortgage Amount: $" + principal);
        System.out.println("Annual Interest Rate: " + annualInterestRate + "%");
        System.out.println("Loan Term: " + loanTermYears + " years");
        System.out.println("Monthly Payment: $" + df.format(monthlyPayment));

        // Print the repayment schedule
        double remainingBalance = principal;
        System.out.println("\nRepayment Schedule:");
        System.out.println("Month\tPayment\t\tMarkup\t\tPrincipal\tRemaining Balance");
        for (int month = 1; month <= numberOfPayments; month++) {
            double interestPayment = remainingBalance * monthlyInterestRate;
            double principalPayment = monthlyPayment - interestPayment;
            remainingBalance -= principalPayment;
            System.out.println(month + "\t\t" + df.format(monthlyPayment) + "\t\t" + df.format(interestPayment) + "\t\t" + df.format(principalPayment) + "\t\t" + df.format(remainingBalance));
        }
    }
}