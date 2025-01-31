#include "std_lib_facilities.h"
#include "test.h"

void testCallByValue()
{
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	int result = incrementByValueNumTimes(v0, increment, iterations);
	cout << "v0: " << v0 << " increment: " << increment
		 << " iterations: " << iterations << " result: " << result << '\n';
}

void testCallByReference()
{
	// BEGIN: 1d

	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	incrementByValueNumTimesRef(v0, increment, iterations);
	cout << "v0: " << v0 << " increment: " << increment
		 << " iterations: " << iterations << '\n';
	
	// END: 1d
}


void testString(){
	// 3b OG 3e
	// BEGIN: 3e
	static constexpr int numGrades = 8;
	string grades{randomizeString(numGrades, 'F', 'A')};
	cout << "Random grades: " << grades << '\n';

	// e)
	vector<int> gradeCount(6);
	int score = 0;
	for (int i = 0; i < 6; ++i) {
		gradeCount[i] = countChar(grades, 'A' + i);
		score += (6 - i) * gradeCount[i];
	}

	double gpa = score / double{numGrades}; // gpa = grade point average
	cout << "Grade point average = " << fixed << setprecision(1) << gpa << '\n';
	// END: 3e
}
