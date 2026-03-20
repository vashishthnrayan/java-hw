abstract class Payment{
    protected double amount;
    public Payment(double amount){
        this.amount = amount;
    }

    abstract double calculateFee();

    public void printReceipt(){
        System.out.println("Payment Amount: $" + amount);
        System.out.println("Transaction Fee: $" + calculateFee());
        System.out.println("Total Amount Charged: $" + (amount + calculateFee()));
        System.out.println("-------------------------------");

    }
}

class CreditCardPayment extends Payment{
    

    public CreditCardPayment(double amount){
        super(amount);
    }

    @Override
    double calculateFee(){
        return amount * 0.02;   
    }
}

class UpiPayment extends Payment{
    
    public UpiPayment(double amount){
        super(amount);
    }

    @Override
    double calculateFee(){
        return 0.1; // flat fee of $0.1   
    }
}

class CashPayment extends Payment{      
    
    public CashPayment(double amount){
        super(amount);
    }

    @Override
    double calculateFee(){
        return amount * 0.01;  // 1% fee   
    }
}

public class PaymentApp {
   public static void main(String[] args) {
       Payment p1 = new CreditCardPayment(100);
       Payment p2 = new UpiPayment(800);
       Payment p3 = new CashPayment(500);
       p1.printReceipt();
        p2.printReceipt();
        p3.printReceipt();

   } 
}
