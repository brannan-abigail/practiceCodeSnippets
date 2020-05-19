#include <iostream>
#include <vector>

using namespace std;

template <class T>
class Solution {
    public:
        void rotate(vector<vector>& matrix) 
        {   size_t n = matrix.size();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    swap(matrix[i][j], matrix[n - j - 1][n - i - 1]);
                }
            }

            for (int i = 0; i < n >> 1; i++ ) {
                for (int j = 0; j < n; j++) {
                    swap(matrix[i][j], matrix[n - i - 1][j]);
                }
            }
        }   
};

int main() { 
   try {
      Solution<int> soln;
      a = [[1, 2, 3],   [4, 5, 6],  [7, 8, 9]]
      soln = rotate(a);
      cout << soln << endl;

      return 0;
   } catch (exception const& ex) { 
      cerr << "Exception: " << ex.what() <<endl; 
      return -1;
   } 
} 