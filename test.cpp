// #include <iostream>
// using namespace std;

// int main() {
//     int arr[] = {0, 0, 0, 0};
//     int target[] = {200, 100, 40, 10};
//     int count = 0;

//     while (arr[0] != target[0] || arr[1] != target[1] || arr[2] != target[2] || arr[3] != target[3]) {
//         arr[0]++;

//         if (arr[0] > 200) {
//             arr[0] = 0;
//             arr[1]++;
//         }

//         if (arr[1] > 100) {
//             arr[1] = 0;
//             arr[2]++;
//         }

//         if (arr[2] > 40) {
//             arr[2] = 0;
//             arr[3]++;
//         }

//         if ((arr[0] + arr[1]*2 + arr[2]*5 + arr[3]*20) == 100) {
//             count++;
//         }

//         for (int i = 0; i < 4; i++) {
//             cout << arr[i] << " ";
//         }
//         cout << endl;
//     }

//     cout << count << endl;

//     return 0;
// }

// #include <iostream>
// #include <vector>

// using namespace std;

// int main() {
//     vector<int> arr = {0, 0, 0, 0, 0};
//     vector<int> target = {200, 100, 40, 10, 2};
//     int count = 0;
    
//     while (arr != target) {
//         arr[0]++;
        
//         if (arr[0] > 200) {
//             arr[0] = 0;
//             arr[1]++;
//         }
        
//         if (arr[1] > 100) {
//             arr[1] = 0;
//             arr[2]++;
//         }
        
//         if (arr[2] > 40) {
//             arr[2] = 0;
//             arr[3]++;
//         }

//         if (arr[3] > 10) {
//             arr[3] = 0;
//             arr[4]++;
//         }
        
//         if ((arr[0] + arr[1]*2 + arr[2]*5 + arr[3]*20 + arr[4]*100) == 200) {
//             count++;
//         }
        
//         for (int i = 0; i < arr.size(); i++) {
//             cout << arr[i] << " ";
//         }
//         cout << endl;
//     }
    
//     cout << count << endl;
    
//     return 0;
// }

#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> arr = {0, 0, 0, 0, 0};
    vector<int> target = {200, 100, 40, 10, 2};
    int count = 0;

    while (arr != target) {
        arr[0]++;

        if (arr[0] > 200) {
            arr[0] = 0;
            arr[1]++;
        }

        if (arr[1] > 100) {
            arr[1] = 0;
            arr[2]++;
        }

        if (arr[2] > 40) {
            arr[2] = 0;
            arr[3]++;
        }

        if (arr[3] > 10) {
            arr[3] = 0;
            arr[4]++;
        }

        if ((arr[0] + arr[1]*2 + arr[2]*5 + arr[3]*20 + arr[4]*100) == 200) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}