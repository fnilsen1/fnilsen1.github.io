#include <bits/stdc++.h>
using namespace std;

// Dimensions of your puzzle
static const int R = 9;
static const int C = 7;

/*
  We'll store each state in the beam as:
   - board layout
   - number of moves so far
   - sequence of moves (in 0-based)
   - score (the higher the better)
*/
struct State {
    vector<vector<char>> board;
    int movesSoFar;
    vector<pair<int,int>> moveSeq;
    int score;
};

// -------------------------------------------------------------------
// 1) COLOR PRINTING UTILITIES
// -------------------------------------------------------------------

// We'll assign a different color code for each character:
// For example, B=Blue, G=Green, O=Yellow, P=Magenta, etc.
string colorCode(char c) {
    switch(c) {
        case 'B': return "\x1b[94m"; // bright blue
        case 'G': return "\x1b[92m"; // bright green
        case 'O': return "\x1b[93m"; // bright yellow
        case 'P': return "\x1b[95m"; // bright magenta
        default:  return "\x1b[0m";  // reset
    }
}

// Print the board in color to the terminal
void printBoardColor(const vector<vector<char>>& board) {
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            char val = board[r][c];
            if(val == 0) {
                // Empty cell, print spaces
                cout << "  ";
            } else {
                // Print in color
                cout << colorCode(val) << val << " " << "\x1b[0m";
            }
        }
        cout << "\n";
    }
    cout << "\n";
}

// -------------------------------------------------------------------
// 2) BASIC BOARD / MOVE UTILITIES
// -------------------------------------------------------------------

// Convert board to string for hashing
string boardToString(const vector<vector<char>>& b){
    ostringstream oss;
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            if(b[r][c] == 0) oss << '!';
            else oss << b[r][c];
        }
    }
    return oss.str();
}

// Check if board is empty
bool isCleared(const vector<vector<char>>& b){
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            if(b[r][c] != 0) return false;
        }
    }
    return true;
}

// Find connected group (4-dir) of board[row][col]
vector<pair<int,int>> getConnected(const vector<vector<char>>& board, int row, int col){
    char color = board[row][col];
    if(color == 0) return {};

    vector<pair<int,int>> group;
    group.reserve(R*C);

    static int dr[4] = {-1,1,0,0};
    static int dc[4] = {0,0,-1,1};

    vector<vector<bool>> visited(R, vector<bool>(C,false));
    stack<pair<int,int>> st;
    st.push({row,col});
    visited[row][col] = true;

    while(!st.empty()){
        auto [rr,cc] = st.top();
        st.pop();
        group.push_back({rr,cc});

        for(int i=0; i<4; i++){
            int nr = rr + dr[i];
            int nc = cc + dc[i];
            if(nr>=0 && nr<R && nc>=0 && nc<C){
                if(!visited[nr][nc] && board[nr][nc] == color){
                    visited[nr][nc] = true;
                    st.push({nr,nc});
                }
            }
        }
    }
    return group;
}

// Remove a group, apply gravity
void removeAndGravity(vector<vector<char>>& board, const vector<pair<int,int>>& group){
    // Remove
    for(auto &cell: group){
        board[cell.first][cell.second] = 0;
    }
    // Gravity
    for(int c=0; c<C; c++){
        int writeRow = R-1;
        for(int r=R-1; r>=0; r--){
            if(board[r][c] != 0){
                board[writeRow][c] = board[r][c];
                writeRow--;
            }
        }
        for(int r=writeRow; r>=0; r--){
            board[r][c] = 0;
        }
    }
}

// Count how many cells are non-empty
int countNonEmpty(const vector<vector<char>>& b){
    int cnt=0;
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            if(b[r][c] != 0) cnt++;
        }
    }
    return cnt;
}

// -------------------------------------------------------------------
// 3) BEAM SEARCH + ITERATIONS
// -------------------------------------------------------------------

// We'll define a comparator that sorts by descending 'score'
struct StateComparator {
    bool operator()(const State &a, const State &b) const {
        // We want highest score on top
        return a.score < b.score;
    }
};

// This function runs ONE iteration of beam search
pair<int, vector<pair<int,int>>> beamSearchIteration(
    const vector<vector<char>>& initialBoard,
    int beamWidth,
    int maxExpansions,
    mt19937 &rng
) {
    // We measure how many pieces we've removed by (initNonEmpty - currentNonEmpty).
    int initNonEmpty = countNonEmpty(initialBoard);

    priority_queue<State, vector<State>, StateComparator> frontier;
    unordered_set<string> visited;

    State start;
    start.board = initialBoard;
    start.movesSoFar = 0;
    start.moveSeq.clear();
    start.score = 0; // 0 removed so far
    frontier.push(start);
    visited.insert(boardToString(initialBoard));

    int expansions = 0;

    // We'll track the best partial solution:
    int bestLeftover = initNonEmpty; 
    vector<pair<int,int>> bestSeq;

    while(!frontier.empty() && expansions < maxExpansions) {
        // Collect up to beamWidth states from the frontier
        vector<State> batch;
        for(int i=0; i<beamWidth; i++){
            if(frontier.empty()) break;
            batch.push_back(frontier.top());
            frontier.pop();
        }

        // Expand them
        for(auto &st : batch){
            expansions++;

            // Check if cleared
            if(isCleared(st.board)){
                // fully cleared => leftover=0
                return make_pair(0, st.moveSeq);
            }

            // If not cleared, see how many left
            int leftover = countNonEmpty(st.board);
            if(leftover < bestLeftover){
                bestLeftover = leftover;
                bestSeq = st.moveSeq;
            }

            // Gather distinct groups
            vector<vector<bool>> used(R, vector<bool>(C,false));
            vector<pair<int,int>> groupLeaders;
            for(int r=0; r<R; r++){
                for(int c=0; c<C; c++){
                    if(st.board[r][c] == 0) continue;
                    if(!used[r][c]){
                        auto grp = getConnected(st.board, r, c);
                        for(auto &g: grp){
                            used[g.first][g.second] = true;
                        }
                        groupLeaders.push_back({r,c});
                    }
                }
            }

            // Shuffle them for random tie-breaking
            shuffle(groupLeaders.begin(), groupLeaders.end(), rng);

            // Expand each group
            for(auto &gl : groupLeaders){
                // Copy board
                auto newBoard = st.board;
                auto group = getConnected(newBoard, gl.first, gl.second);

                // If your puzzle requires group>=2:
                // if(group.size()<2) continue;

                removeAndGravity(newBoard, group);

                string key = boardToString(newBoard);
                if(visited.count(key)) continue;
                visited.insert(key);

                State nxt;
                nxt.board = move(newBoard);
                nxt.movesSoFar = st.movesSoFar + 1;
                nxt.moveSeq = st.moveSeq;
                nxt.moveSeq.push_back({gl.first, gl.second});

                int removed = initNonEmpty - countNonEmpty(nxt.board);
                nxt.score = removed;

                frontier.push(nxt);
            }

            if(expansions >= maxExpansions) break;
        }
    }

    // If we exit the loop without clearing, we return best partial
    return make_pair(bestLeftover, bestSeq);
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ---------------------------
    // 1) DEFINE YOUR BOARD
    // ---------------------------
    vector<vector<char>> board = {
       {'P','G','B','P','B','P','O'},
       {'B','P','O','O','G','G','B'},
       {'G','O','O','O','G','O','P'},
       {'P','G','G','O','G','G','O'},
       {'B','B','G','O','G','B','B'},
       {'P','G','O','B','B','O','G'},
       {'O','P','O','O','O','B','P'},
       {'G','G','B','P','G','P','B'},
       {'P','O','G','B','O','P','B'}
    };

    // ---------------------------
    // 2) PARAMETERS TO TWEAK
    // ---------------------------
    int beamWidth = 300;       // #states to expand each "layer"
    int maxExpansions = 20000; // limit expansions per iteration
    int iterations = 5;        // number of repeated runs
                               // (each run has random tie-breaking)

    // For randomization
    random_device rd;
    mt19937 rng(rd());

    // We'll track the best solution across all iterations
    int bestLeftoverGlobal = R * C; // something large
    vector<pair<int,int>> bestSeqGlobal;

    int initialNonEmpty = countNonEmpty(board);

    // Run multiple times with random tie-breaking
    for(int i=1; i<=iterations; i++){
        auto result = beamSearchIteration(board, beamWidth, maxExpansions, rng);
        int leftover = result.first;
        auto seq = result.second;

        cout << "Iteration " << i 
             << ": leftover=" << leftover
             << " after " << seq.size() << " moves.\n";

        if(leftover < bestLeftoverGlobal){
            bestLeftoverGlobal = leftover;
            bestSeqGlobal = seq;
        }
        // If we fully cleared it, leftover=0 => done
        if(leftover == 0){
            cout << "Found a full clear in iteration " << i << "!\n";
            break;
        }
    }

    // Final result:
    cout << "\nBest leftover across all iterations: " << bestLeftoverGlobal
         << " after " << bestSeqGlobal.size() << " moves.\n";
    if(bestLeftoverGlobal == 0){
        cout << "We cleared the board!\n";
    } else {
        cout << "Not fully cleared, but removed "
             << (initialNonEmpty - bestLeftoverGlobal) << " pieces.\n";
    }

    // -------------------------------------------------------------------
    // 3) PRINT THE BOARD AFTER EVERY MOVE (IN COLOR!)
    //    We'll replay the best solution step by step.
    // -------------------------------------------------------------------

    cout << "\nReplaying the best solution:\n";

    // Make a copy of the initial board
    auto replayBoard = board;

    // Print the initial board
    cout << "Initial board:\n";
    printBoardColor(replayBoard);

    // Apply each move, printing the updated board
    for(int i = 0; i < (int)bestSeqGlobal.size(); i++){
        auto [r, c] = bestSeqGlobal[i];

        // 1-based for display
        cout << "Move #" << (i+1)
             << " => click (" << (r+1) << ", " << (c+1) << ")\n";

        // Remove group
        auto group = getConnected(replayBoard, r, c);
        removeAndGravity(replayBoard, group);

        // Print updated board
        printBoardColor(replayBoard);
    }

    return 0;
}
