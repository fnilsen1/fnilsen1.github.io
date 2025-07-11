// clocklib
#include "utils.h"
#include "tests.h"

int main()
{

    //IMPORTANT: POINTER SHOULD BE PARAMETER IN FUNCTIONS
    //For parallelization

    // State array is defined at the top

    /*
    Pin position - Front/Back move (F/B)- how many tics
    string move = "UR,F,+5"
    If moves have 1 character then add '_' to match the format
    Examples: 'UR,F,+5' and 'U_,B,-3'
    */

    // Alg: "UR,F,+5 U,B,-3"

    // generate_move_table();
    // time_random_moves(1000000);
    apply_moves("U,F,-1");
    print_state();


    return 0;
}
