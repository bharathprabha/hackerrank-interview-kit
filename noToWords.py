def noToWord(number):
    ones = ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
    tens = ['ten', 'twenty', 'thirty', 'fourty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = 'thousand'

    word = ''

    if (number < 10):
        word = ones[number]
    elif (number < 100):
        
        
