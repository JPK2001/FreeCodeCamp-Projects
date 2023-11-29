function checkCashRegister(price, cash, cid) {
    const currencyValues = {
      "PENNY": 0.01,
      "NICKEL": 0.05,
      "DIME": 0.1,
      "QUARTER": 0.25,
      "ONE": 1,
      "FIVE": 5,
      "TEN": 10,
      "TWENTY": 20,
      "ONE HUNDRED": 100
    };
    
    let changeNeeded = cash - price;
    let changeAvailable = cid.reduce((total, currency) => total + currency[1], 0);
    
    if (changeAvailable < changeNeeded) {
      return {status: "INSUFFICIENT_FUNDS", change: []};
    }
    
    if (changeAvailable === changeNeeded) {
      return {status: "CLOSED", change: cid};
    }
    
    let changeToGive = [];
    
    for (let i = cid.length - 1; i >= 0; i--) {
      const currencyName = cid[i][0];
      const currencyValue = currencyValues[currencyName];
      let currencyAmount = cid[i][1];
      let currencyCount = 0;
      let currencyTotal = 0;
  
      while (changeNeeded >= currencyValue && currencyAmount > 0) {
        changeNeeded -= currencyValue;
        changeNeeded = Math.round(changeNeeded * 100) / 100;
        currencyAmount -= currencyValue;
        currencyTotal += currencyValue;
        currencyCount++;
      }
  
      if (currencyCount > 0) {
        changeToGive.push([currencyName, currencyTotal]);
      }
    }
  
    if (changeNeeded > 0) {
      return {status: "INSUFFICIENT_FUNDS", change: []};
    }
    
    return {status: "OPEN", change: changeToGive};
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);