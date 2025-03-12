function numberToWords(num) {
    if (num < 0 || num > 1e15) {
        throw new Error('Input must be a number between 0 and 1 quadrillion (1e15).');
    }
    
    if (num === 0) return 'zero';

    const belowTwenty = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
        'seventeen', 'eighteen', 'nineteen'
    ];
    
    const tens = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ];
    
    const thousands = [
        '', 'thousand', 'million', 'billion', 'trillion', 'quadrillion'
    ];

    const words = (n) => {
        if (n < 20) return belowTwenty[n];
        if (n < 100) return tens[Math.floor(n / 10)] + (n % 10 !== 0 ? ' ' + belowTwenty[n % 10] : '');
        if (n < 1000) return belowTwenty[Math.floor(n / 100)] + ' hundred' + (n % 100 !== 0 ? ' ' + words(n % 100) : '');
        return '';
    };

    let result = '';
    let thousandIndex = 0;

    while (num > 0) {
        const chunk = num % 1000;
        if (chunk > 0) {
            result = words(chunk) + (thousands[thousandIndex] ? ' ' + thousands[thousandIndex] : '') + (result ? ' ' + result : '');
        }
        num = Math.floor(num / 1000);
        thousandIndex++;
    }

    return result.trim();
}

// Example usage:
console.log(numberToWords(123));                // "one hundred twenty three"
console.log(numberToWords(1234567890123));      // "one trillion two hundred thirty four billion five hundred sixty seven million eight hundred ninety thousand one hundred twenty three"
console.log(numberToWords(1000));                // "one thousand"
console.log(numberToWords(0));                   // "zero"
console.log(numberToWords(999999999999999));    // "nine hundred ninety nine trillion nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine"
