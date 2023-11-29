function palindrome(str) {
    str = str.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
   var reversedStr = str.split("").reverse().join("");
   return str === reversedStr;
   return true;
 }
 
 palindrome("eye");