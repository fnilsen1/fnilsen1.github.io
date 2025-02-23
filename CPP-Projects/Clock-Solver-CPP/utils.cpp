#include "utils.h"

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
