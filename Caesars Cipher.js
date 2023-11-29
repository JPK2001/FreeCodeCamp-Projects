function rot13(str) {
    let decoded = '';
  
    for (let i = 0; i < str.length; i++) {
      const charCode = str.charCodeAt(i);
  
      if (charCode >= 65 && charCode <= 90) {
        let decodedCharCode = charCode - 13;
        if (decodedCharCode < 65) {
          decodedCharCode += 26;
        }
        decoded += String.fromCharCode(decodedCharCode);
      } else {
        decoded += str[i];
      }
    }
    return decoded;
  }
  
  rot13("SERR PBQR PNZC");