// Exact chunked certificate for 29 mechanical boundary transitions.
// Build with g++ -O3 -std=c++20. Suggested chunks: 0:5,5:10,...,25:30.
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using u128=unsigned __int128;
const int L=29; const u128 LOW=(u128)2075<<60,HIGH=(u128)1<<73;
string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back(char('0'+x%10));x/=10;}reverse(s.begin(),s.end());return s;}
u128 inv2(u128 a,int b){u128 x=1;for(int i=0;i<8;i++)x*=2-a*x;return x&(((u128)1<<b)-1);}
bool drop(u128 x,int&k,u128&e){for(k=1;k<=2000;k++){u128 y=3*x+1;unsigned long long lo=(unsigned long long)y;int a=lo?__builtin_ctzll(lo):64+__builtin_ctzll((unsigned long long)(y>>64));x=y>>a;if(x<LOW){e=x;return true;}}return false;}
int main(int ac,char**av){int lo=ac>1?stoi(av[1]):0,hi=ac>2?stoi(av[2]):30;using boost::multiprecision::cpp_int;cpp_int p=1;vector<int>f;for(int i=0;i<=500;i++){f.push_back(boost::multiprecision::msb(p));p*=3;}vector<int>r(500);for(int i=0;i<500;i++)r[i]=f[i+1]-f[i];set<vector<int>>seen;vector<pair<vector<int>,int>>fac;for(int s=0;s+L<=500&&fac.size()<30;s++){vector<int>w(r.begin()+s,r.begin()+s+L);if(seen.insert(w).second)fac.push_back({w,s});}assert(fac.size()==30&&0<=lo&&lo<hi&&hi<=30);u128 p3=1;for(int i=0;i<L;i++)p3*=3;unsigned long long rows=0;int worst=0,wshift=-1;u128 wseed=0,wend=0;for(int i=lo;i<hi;i++){auto [w,sh]=fac[i];int A=0;u128 d=0;for(int a:w){d=3*d+((u128)1<<A);A+=a;}int bits=A+1;u128 mod=(u128)1<<bits,mask=mod-1;u128 res=(inv2(p3,bits)*((((u128)1<<A)-d)&mask))&mask;u128 q=res<LOW?(LOW-res+mod-1)/mod:0;for(;;q++){u128 seed=res+q*mod;if(seed>=HIGH)break;int k;u128 e;if(!drop(seed,k,e)){cerr<<"FAIL shift="<<sh<<" seed="<<s128(seed)<<"\n";return 2;}rows++;if(k>worst){worst=k;wshift=sh;wseed=seed;wend=e;}}}cout<<"range="<<lo<<":"<<hi<<" rows="<<rows<<" worst="<<worst<<","<<s128(wseed)<<","<<s128(wend)<<",shift="<<wshift<<"\n";}
