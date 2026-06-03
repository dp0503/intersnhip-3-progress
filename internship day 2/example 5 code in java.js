class Bank {
  constructor(amount) {
    this.amount = amount;
  }
  
  getBalance() {
    console.log("Balance is:", this.amount);
  }
  
  deposit(amount) {
    this.amount = this.amount + amount;
  }
  
  withdraw(amount) {
    if (amount > this.amount) {
      console.log("Transaction failed! Withdrawal amount exceeds balance.");
    } else {
      this.amount = this.amount - amount;
      console.log("Successfully withdrew:", amount);
    }
  }
}

var myobj = new Bank(1000);
console.log(myobj.amount); // 1000
myobj.getBalance(); // 1000

myobj.deposit(5000);
myobj.getBalance(); // 6000

myobj.withdraw(10000); // Triggers the error message
myobj.getBalance(); // 6000

var myobj2 = new Bank(1000);
myobj2.getBalance(); // 1000
