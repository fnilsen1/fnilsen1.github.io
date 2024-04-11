#include <iostream>
using namespace std;

int maxOfTwo(int a, int b){
    if(a>b){
        cout << "A is greater than B" << endl;
        return a;
}

    else{
        cout << "B is greater than or equal to A" << endl;
        return b;
    }
}

int fibonacci(int n){
    int a = 0;
    int b = 1;
    cout << "Fibonacci numbers:" << endl;
    for(int x = 1; x < n+1; x++){
        cout << x << " " << b << endl;

        int temp = b;
        b += a;
        a = temp;
    
    
    }
    cout << "----" << endl;
    return b;
}

int squareNumberSum(int n){
    int totalSum = 0;
    for(int i = 1; i < n+1; i++){
        totalSum += i*i;
        cout << i*i << endl;
    }
    cout << totalSum << endl;
    return totalSum;
}

int triangleNumbersBelow(int n){
    int acc = 1;
    int num = 2;
    cout << "Triangle numbers below " << n << ":" << endl;
    while(acc < n){
        cout << acc << endl;
        acc += num;
        num += 1;
    }
    cout << endl;
}

int isPrime(int n){
    for(int j = 2; j<n; j++){
        if(n%j == 0){
            return false;
        }
    
    }
    return true;
}

int naivePrimeNumberSearch(int n){
    for(int number = 2; number < n; number++){
        if(isPrime(number)){
            cout << number << " is a prime" << endl;
        }
    
    }
}

void inputAndPrintNameAndAge(){
    string name;
    cout << "Skriv inn et navn: ";
    cin >> name;
    int age;
    cout << "Skriv inn alderen til " << name << ": ";
    cin >> age;
    cout << name << " er " << age << " aar gammel.";

}

int main() {
// cout << "Oppgave a)" << endl;
// cout << maxOfTwo(5, 6) << endl;

// cout    << "Oppgave c)" << endl;
// cout << fibonacci(5) << endl;

// cout << "Oppgave d)" << endl;
// cout << squareNumberSum(5) << endl;

// cout << "Oppgave e)" << endl;
// triangleNumbersBelow(10);

// cout << "Oppgave f) og g)" << endl;
// naivePrimeNumberSearch(14);

inputAndPrintNameAndAge();

return 0;
}