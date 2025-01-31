#include "utilities.h"

int incrementByValueNumTimes(int startValue, int increment, int numTimes)
{
	for (int i = 0; i < numTimes; i++)
		startValue += increment;

	return startValue;
}

// BEGIN: 1d
void incrementByValueNumTimesRef(int& startValue, int increment, int numTimes)
{
	for (int i = 0; i < numTimes; i++)
		startValue += increment;
}
// END: 1d

// BEGIN: 1e
void swapNumbers(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}
// END: 1e

// BEGIN: 2b
void printStudent(const Student& student) {
// Parameter kan tas inn som const-referanse fordi funksjonen ikke skal endre på den.
	cout<< "Name: " <<student.name << ", age: " << student.age <<", studyprogram: " 
	<< student.studyProgram <<'\n'; 
}
// END: 2b

// BEGIN: 2c
bool isInProgram(const Student& student, const string& program) {
// Parametere kan tas inn som const-referanser fordi funksjonen ikke skal endre på dem.
	return student.studyProgram == program;
}
// END: 2c

// BEGIN: 3a
string randomizeString(int n, char upper, char lower)
{
	string str;
	random_device rd;
	default_random_engine generator(rd());
	uniform_int_distribution<int> distribution((int)lower, (int)upper);
	for (int i = 0; i < n; ++i){
		str += distribution(generator);
	}
	return str;
}
// END: 3a

// BEGIN: 3c
string readInputToString(unsigned int n, char upper, char lower)
{
	string str;
	// Variabelen ch er introdusert i for-lokkens scope. Generelt er et mindre scope bedre,
	// saa lenge det er mulig.
	// I hver iterasjon, sjekk at n ikke er lik 0, og les tegnet til ch

	// Grensene konverteres også til store bokstaver for avgrensingen
	lower = toupper(lower);
	upper = toupper(upper);
	
	for (char ch; str.size() < n && cin >> ch; ) {
		// hopp over tegn som ikke er alfanumerisk
		if (isalnum(ch)) {
			ch = toupper(ch); // endre til stor bokstav
			if (lower <= ch && ch <= upper) {
				str += ch;
			}
		}
	}

	// forkast overflowing input paa samme linje
	cin.clear();
	cin.ignore(255, '\n');

	return str;
}
// END: 3c

// BEGIN: 3d
int countChar(string str, char ch)
{
	int n = 0;
	for (char c : str) {
		if (c == ch) {
			++n;
		}
	}

	return n;

	// Alternativ med STL-algoritme:
	// return count(str.begin(), str.end(), ch);
}
// END: 3d

