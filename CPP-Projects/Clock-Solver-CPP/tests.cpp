#include "tests.h"

using namespace std;

string generate_random_moves(int n)
{
    vector<string> pin_states = {"UL", "UR", "DR", "DL", "U", "\\", "L", "R", "/", "D", "dl", "dr", "ur", "ul", "ALL"};
    vector<string> random_tic_vector = {"0", "+1", "+2", "+3", "+4", "+5", "+6", "-1", "-2", "-3", "-4", "-5"};
    vector<string> fb = {"F", "B"};

    string moves;
    random_device rd;
    default_random_engine generator(rd());
    uniform_int_distribution<int> random_pin_state(0, 13);
    uniform_int_distribution<int> random_tic(0, 11);
    uniform_int_distribution<int> front_or_back(0, 1);

    for (int i = 0; i < n; i++)
    {
        moves += pin_states.at(random_pin_state(generator)) + "," + fb.at(front_or_back(generator)) + "," + random_tic_vector.at(random_tic(generator)) + " ";
    }

    return moves;
}

void time_random_moves(int n){
    string random_moves = generate_random_moves(n);
    auto start = chrono::high_resolution_clock::now();
    apply_moves(random_moves);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout << "Execution time: " << elapsed.count() << " seconds" << endl;
    print_state();
}
