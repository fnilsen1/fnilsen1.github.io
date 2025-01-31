// clocklib

using namespace std;
#include <iostream>
#include <vector>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <array>
#include <iomanip>
#include <random>
#include "move_table.h"
void print_state();

int state[14] = {0};

void apply_moves(const string &moves)
{
    istringstream stream(moves);
    string move;

    while (stream >> move)
    {
        for (int i = 0; i < 14; i++)
        {
            state[i] += moves_map[move][i];
        }
    }
    for (int i = 0; i < 14; i++)
    {
        state[i] = (state[i] % 12 + 12) % 12;
    }
}

void print_state()
{
    cout << setw(2) << state[0] << setw(3) << state[1] << setw(3) << state[2] << setw(7) << state[9] << endl;
    cout << setw(2) << state[3] << setw(3) << state[4] << setw(3) << state[5] << setw(4) << state[10] << setw(3) << state[11] << setw(3) << state[12] << endl;
    cout << setw(2) << state[6] << setw(3) << state[7] << setw(3) << state[8] << setw(7) << state[13] << endl;
}

void generate_move_table()
{

    int front_table_singletic[15][14] = {
        {1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
        {0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        {1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
        {1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        {0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        {1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0}};

    int back_table_singletic[15][14] = {
        {0, 0, 1, 0, 0, 0, 1, 0, 1, -1, -1, -1, -1, -1},
        {1, 0, 0, 0, 0, 0, 1, 0, 1, -1, -1, -1, -1, -1},
        {1, 0, 1, 0, 0, 0, 1, 0, 0, -1, -1, -1, -1, -1},
        {1, 0, 1, 0, 0, 0, 0, 0, 1, -1, -1, -1, -1, -1},
        {0, 0, 0, 0, 0, 0, 1, 0, 1, 0, -1, -1, -1, -1},
        {0, 0, 1, 0, 0, 0, 1, 0, 0, -1, -1, -1, -1, -1},
        {0, 0, 1, 0, 0, 0, 0, 0, 1, -1, -1, -1, 0, -1},
        {1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, -1, -1, -1},
        {1, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, -1, -1},
        {1, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0},
        {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, -1, -1},
        {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, -1, 0, -1},
        {0, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0},
        {1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0},
        {1, 0, 1, 0, 0, 0, 1, 0, 1, -1, -1, -1, -1, -1}};

    vector<string> pin_states = {"UL", "UR", "DR", "DL", "U", "\\", "L", "R", "/", "D", "dl", "dr", "ur", "ul", "ALL"};

    unordered_map<string, array<int, 14>> front_moves_map;
    unordered_map<string, array<int, 14>> back_moves_map;
    string move_name;

    for (int i = 0; i < 15; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            move_name = pin_states[i] + ",B,-";
            array<int, 14> tmp_array = {};

            for (int k = 0; k < 14; k++)
            {
                tmp_array[k] = back_table_singletic[i][k] * -j;
            }

            move_name += to_string(j);
            back_moves_map[move_name] = tmp_array;
        }
    }

    for (const auto &[key, value] : back_moves_map)
    {
        cout << "    {\"" << key << "\", {";
        for (size_t i = 0; i < value.size(); ++i)
        {
            cout << value[i];
            if (i < value.size() - 1)
            {
                cout << ", ";
            }
        }
        cout << "}},\n";
    }

    std::cout << "};\n\n";
}

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

int main()
{

    // State array is defined at the top

    /*
    Pin position - Front/Back move (F/B)- how many tics
    string move = "UR,F,+5"
    If moves have 1 character then add '_' to match the format
    Examples: 'UR,F,+5' and 'U_,B,-3'
    */

    // Alg: "UR,F,+5 U,B,-3"

    // generate_move_table();
    string random_moves = generate_random_moves(100000000);
    auto start = chrono::high_resolution_clock::now();
    apply_moves(random_moves);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout << "Execution time: " << elapsed.count() << " seconds" << endl;
    print_state();
    return 0;
}
