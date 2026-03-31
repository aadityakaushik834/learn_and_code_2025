public class Paperboy {
    public void collectPayment(Customer customer, double paymentAmount) {
        if (customer.pay(paymentAmount)) {
            System.out.println("Payment collected.");
        } else {
            System.out.println("Payment failed. Will come back later.");
        }
    }
}