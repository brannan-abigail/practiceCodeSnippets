#include <iostream>
#include <vector>

using namespace std;
int main() {
    cout<<"Hello World\n";
    
    std::vector<std::vector<int>> a;
    
    a = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};
     
     cout << a.size();

    return 0;
}