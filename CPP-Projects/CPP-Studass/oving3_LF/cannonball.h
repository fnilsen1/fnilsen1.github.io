#pragma once
#include "std_lib_facilities.h"

constexpr double pi = 3.14159265;
constexpr double gravity = 9.81;

// Del 1:

// BEGIN: 1a
double acclY();
// END: 1a

// BEGIN: 1b
double velY(double initVelocityY, double time);
// END: 1b

// BEGIN: 1c
double posX(double initPositionX, double initVelocityX, double time);
double posY(double initPositionY, double initVelocityY, double time);
// END: 1c

// BEGIN: 1d
void printTime(double time);
// END: 1d

// BEGIN: 1e
double flightTime(double initVelocityY);
// END: 1e

bool testDeviation(double compareOperand, double toOperand, double maxError, string name);

// Del 2:

// BEGIN: 4a
double getUserInputTheta();

double getUserInputInitVelocity();

double degToRad(double deg);

double getVelocityX(double theta, double initVelocity);
double getVelocityY(double theta, double initVelocity);
vector<double> getVelocityVector(double theta, double initVelocity);
// END: 4a

// BEGIN: 4b
double getDistanceTraveled(double velocityX, double velocityY);
// END: 4b

// BEGIN: 4c
double targetPractice(double distanceToTarget, double velocityX, double velocityY);
// END: 4c

// Del 3:
// BEGIN: 5b
void playTargetPractice();
// END: 5b
