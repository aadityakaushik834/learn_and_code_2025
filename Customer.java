public class Customer {
    private Wallet wallet;

    public Customer(Wallet wallet) {
        if (wallet == null) {
            throw new IllegalArgumentException("Wallet cannot be null");
        }
        this.wallet = wallet;
    }

    public boolean pay(double amount) {
        return wallet.withdraw(amount);
    }
}