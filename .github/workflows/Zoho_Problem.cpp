#include <iostream>
#include <queue>
using namespace std;

void solve(int a, int b){
    queue<int> q;
    q.push(a);
    q.push(b);
    int k =100;
    while(k--){
        int temp = q.front();
        q.pop();
        cout<<temp<<" ";
        q.push(temp*10 + a);
        q.push(temp*10 +b);
    }
    return;
}
int main()
{
   cout << "Hello World"; 
   int a,b;
   cin>>a>>b;
   solve(a,b);
   return 0;
}
