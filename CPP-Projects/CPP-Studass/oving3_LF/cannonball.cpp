#include "cannonball.h"
#include "cannonball_viz.h"
#include "utilities.h"

// BEGIN: 2a
double acclY()
{
	return -gravity; // definert som en konstant i cannonball.h
}
// END: 2a

// BEGIN: 2b
double velY(double initVelocityY, double time)
{
	return initVelocityY + acclY() * time;
}
// END: 2b

// BEGIN: 2c
double posX(double initPositionX, double initVelocityX, double time)
{
	return initPositionX + initVelocityX * time;
}

double posY(double initPositionY, double initVelocityY, double time)
{
	return initPositionY + initVelocityY * time + 0.5 * pow(time, 2.0) * acclY();
}
// END: 2c

// BEGIN: 2d
void printTime(double time)
{
	int hours = static_cast<int>(time) / 3600;  // "time" konverteres til heltall for at "/" skal utføre heltallsdivisjon.
	int minutes = (static_cast<int>(time) - 3600 * hours) / 60;
	double seconds = time - hours * 3600 - minutes * 60;
	cout << hours << " hours, " << minutes << " minutes and " << seconds << " seconds\n";
}
// END: 2d

// BEGIN: 2e
double flightTime(double initVelocityY)
{
	return (-2.0 * initVelocityY) / acclY();
}
// END: 2e

// BEGIN: 3b
bool testDeviation(double compareOperand, double toOperand, double maxError, string name)
{
	if (abs(compareOperand - toOperand) <= maxError) {
		cout << name << " is valid.\n";
		return true;
	} else {
		cout << name << " is invalid. Expected: " << toOperand << ", got " << compareOperand
			 << ".\n";
		return false;
	}
}
// END: 3b

// BEGIN: 4a
double getUserInputTheta()
{
	cout << "Please enter an angle in degrees for the cannon: ";
	double theta;
	cin >> theta;
	while (theta < 0.1)
	{
		cout << "The angle you chose was too small, please select a larger one.\n";
		cin >> theta;
	}
	return theta;
}

double getUserInputInitVelocity()
{
	cout << "Please enter the initial velocity of the cannonball: ";
	double initVelocity;
	cin >> initVelocity;
	while (initVelocity < 0.1)
	{
		cout << "The velocity you chose was too small, please select a larger one.\n";
		cin >> (initVelocity);
	}
	return initVelocity;
}

double degToRad(double deg)
{
	return (deg / 180) * pi; // pi definert som en konstant i cannonball.h
}

double getVelocityX(double theta, double initVelocity)
{
	return cos(degToRad(theta)) * initVelocity;
}

double getVelocityY(double theta, double initVelocity)
{
	return sin(degToRad(theta)) * initVelocity;
}

vector<double> getVelocityVector(double theta, double initVelocity)
{
	vector<double> velocityVector;

	velocityVector.push_back(getVelocityX(theta, initVelocity));
	velocityVector.push_back(getVelocityY(theta, initVelocity));
	return velocityVector;

	// Alternativt:
	// return {
	// 	getVelocityX(theta, initVelocity),
	// 	getVelocityY(theta, initVelocity)
	// };
}
// END: 4a

// BEGIN: 4b
double getDistanceTraveled(double velocityX, double velocityY)
{
	double fTime = flightTime(velocityY);
	double distanceTraveled = posX(0, velocityX, fTime);
	return distanceTraveled;
	// kort: return posX(0, velocityX, flightTime(velocityY))
}
// END: 4b

// BEGIN: 4c
double targetPractice(double distanceToTarget, double velocityX, double velocityY)
{
	double error = distanceToTarget - getDistanceTraveled(velocityX, velocityY);
	return abs(error);
}
// END: 4c

// BEGIN: 5b

void playTargetPractice()
{
	cout << "*******Playing target practice!*******\n"
			"The goal of this game is to hit the target, you will be presented\n"
			"with a target at some random distance (between 100 and 1000m)\n"
			"from you. In order to hit a target you must specify an angle and\n"
			"an initial velocity for the cannonball.\n\n";
	constexpr int minTarget = 100;
	constexpr int maxTarget = 1000;
	constexpr int timeSteps = 50;
	constexpr int maxTries = 10;
	double distanceToTarget = randomWithLimits(minTarget, maxTarget);
	double maxError = 5.0;
	bool win = false;

	cout << "Target is placed at " << distanceToTarget << " m range\nGood luck!\n\n";

	cout << fixed << setprecision(2);
	for (int round = 0; round < maxTries; ++round)
	{
		cout << "Round " << round + 1 << ":\n\n";
		double angle, initVelocity, initVelocityX, initVelocityY;
		angle = getUserInputTheta();
		initVelocity = getUserInputInitVelocity();
		initVelocityX = getVelocityX(angle, initVelocity);
		initVelocityY = getVelocityY(angle, initVelocity);
		
		double error = targetPractice(distanceToTarget, initVelocityX, initVelocityY);
		double distanceTraveled = getDistanceTraveled(initVelocityX, initVelocityY);

		
		cout << "Flight time was: ";
		printTime(flightTime(initVelocityY));
		cout << "Your shot went: " << distanceTraveled 
			 << " m\nDistance from target: " << error
			 << " m\n";

		cannonBallViz(distanceToTarget, maxTarget, initVelocityX, initVelocityY, timeSteps);
		if (error < maxError)
		{
			win = true;
			break;
		}

		if (distanceTraveled > distanceToTarget)
		{
			cout << "You overshot the target.\n\n";
		}
		else
		{
			cout << "You didn't reach the target.\n\n";
		}
	}

	if (win)
	{
		cout << "Congratulations you won!\n";
	}
	else
	{
		cout << "Too bad, you lost.\n";
	}
}

// END: 5b