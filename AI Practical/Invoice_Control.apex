public class Invoice_Control {
    public String message { get; set; }
    public Decimal amount { get; set; }
    public String customerEmail { get; set; }
    public List<Invoice__c> customerInvoices { get; set; }

    public void createInvoice() {
        customerInvoices = new List<Invoice__c>(); // Reset the invoice list

        if (amount <= 0 || String.isEmpty(customerEmail)) {
            message = 'Error: Amount must be greater than 0 and email is required.';
            return;
        }

        try {
            // Create the invoice
            Invoice__c inv = new Invoice__c(
                Amount__c = amount, 
                Customer_Email__c = customerEmail, 
                Due_Date__c = Date.today().addDays(30),
                Name = 'INV-' + String.valueOf(Datetime.now().getTime()) // simple unique name
            );
            insert inv;

            // Re-query the record to ensure we get the Name
            inv = [SELECT Name FROM Invoice__c WHERE Id = :inv.Id LIMIT 1];

            // Set success message with name
            message = 'Invoice Created: ' + inv.Name;

            // Query all customer invoices
            customerInvoices = [SELECT Name, Amount__c, Due_Date__c FROM Invoice__c WHERE Customer_Email__c = :customerEmail];

        } catch (Exception e) {
            message = 'Error: ' + e.getMessage();
        }
    }
}
