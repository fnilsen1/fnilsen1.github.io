#pragma once
#include <iostream>
#include <vector>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <array>
#include <iomanip>
#include <random>
#include "move_table.h"
#include "tests.h"
using namespace std;

void apply_moves(const string &moves);
void print_state();
void generate_move_table();