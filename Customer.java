public class Customer {
    private Wallet wallet;

    public Customer(Wallet wallet) {
        this.wallet = wallet;
    }

    public boolean pay(double amount) {
        return wallet != null && wallet.withdraw(amount);
    }
}