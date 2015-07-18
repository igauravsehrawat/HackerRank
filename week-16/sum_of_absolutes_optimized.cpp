// source
// https://www.hackerrank.com/contests/w16/challenges/sum-of-absolutes/editorial
// Even + Even = Even
// Even - Even = Even

// Even + Odd = Odd
// Even - Odd = Odd
// Odd - Even = Odd

// Odd + Odd = Even
// Odd - Odd = Even

#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;

#define mp  make_pair
#define pb push_back

int A[100001];

void solve()
{
    int N,Q,X,Y;
    A[0] = 0;
    cin>>N>>Q;
    for(int i=1;i<=N;i++)   cin>>A[i];
    // here is memoization part
    // saving the sum a[2] = a[2] + a[1]; a[3] = a[3] + a[2]
    for(int i=2;i<=N;i++)   A[i] = A[i] + A[i-1];
    for(int i=1;i<=Q;i++){
        cin>>X>>Y;
        int z = A[Y] - A[X - 1];
        // a[10] - a[0] here x = 1
        // a[10] - a[3] here x= 4
        if( z & 1 ) printf("Odd\n");
        else    printf("Even\n");
    }
}

int main()
{
    int T=1;
    for(int i=1;i<=T;i++){
        solve();
    }
    return 0;
}
