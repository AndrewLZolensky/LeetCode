int romanCharToInt(char c) {
    switch (c) {
        case 'I' : return 1;
        case 'V' : return 5;
        case 'X' : return 10;
        case 'L' : return 50;
        case 'C' : return 100;
        case 'D' : return 500;
        case 'M' : return 1000;
        default : return 0;
    }
}

int romanToInt(char* s) {
    int count = 0;
    int curr = 0;
    int last = 0;
    while (*s != '\0') {
        curr = romanCharToInt(*s);
        count += curr;
        if (curr > last) {
            count -= 2 * last;
        }
        last = curr;
        s += 1;
    }
    return count;
}