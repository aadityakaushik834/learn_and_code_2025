class DeviceLockedException extends Exception {
    public DeviceLockedException(String message) {
        super(message);
    }
}

class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

class NetworkConnectionException extends Exception {
    public NetworkConnectionException(String message) {
        super(message);
    }
}

public class ATMDeviceController {

    private static final String DEV1 = "DEV1";
    private static final int DEVICE_SUSPENDED = -1;
    private static final int WIFI_CONNECTED = 1;

    public void processWithdrawal(String accountId, double amount) {
        try {
            withdraw(accountId, amount);
            System.out.println("Withdrawal successful! Cash dispensed.");
        } catch (DeviceLockedException | NetworkConnectionException | InsufficientFundsException e) {
            System.err.println("Transaction Failed: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("System Error: " + e.getMessage());
        }
    }

    public void withdraw(String accountId, double amount) throws DeviceLockedException, NetworkConnectionException, InsufficientFundsException {
        DeviceHandle handle = getValidDeviceHandle(DEV1);
        
        validateATMDevice(handle);
        validateSufficientFunds(accountId, amount);
        
        dispenseCash(handle, amount);
    }

    private DeviceHandle getValidDeviceHandle(String deviceId) {
        DeviceHandle handle = getHandle(deviceId);
        if (handle == DeviceHandle.INVALID) {
            throw new IllegalStateException("Unknown Error: Invalid Device Handle");
        }
        return handle;
    }

    private void validateATMDevice(DeviceHandle handle) throws DeviceLockedException, NetworkConnectionException {
        DeviceRecord record = retrieveDeviceRecord(handle);
        
        if (record.getStatus() == DEVICE_SUSPENDED) {
            throw new DeviceLockedException("The ATM device is currently suspended.");
        }
        if (record.getWifiConnection() != WIFI_CONNECTED) {
            throw new NetworkConnectionException("No WiFi connection established.");
        }
    }

    private void validateSufficientFunds(String accountId, double amount) throws InsufficientFundsException {
        if (getBalance(accountId) < amount) {
            throw new InsufficientFundsException("Account balance is lower than the requested amount.");
        }
    }

    private DeviceHandle getHandle(String devId) { return new DeviceHandle(); }
    private DeviceRecord retrieveDeviceRecord(DeviceHandle handle) { return new DeviceRecord(); }
    private double getBalance(String accountId) { return 500.0; }
    private void dispenseCash(DeviceHandle handle, double amount) { /* Hardware dispense logic */ }

    static class DeviceHandle {
        public static final DeviceHandle INVALID = new DeviceHandle();
    }

    static class DeviceRecord {
        public int getStatus() { return 0; }
        public int getWifiConnection() { return 1; }
    }
}
