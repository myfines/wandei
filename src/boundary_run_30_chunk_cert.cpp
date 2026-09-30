// Exact chunked certificate for 30 mechanical boundary transitions.
// Build: g++ -O3 -std=c++20 boundary_run_30_chunk_cert.cpp -o cert
// Run four disjoint chunks: ./cert 0 8 ; ./cert 8 16 ; ./cert 16 24 ; ./cert 24 31
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using u128 = unsigned __int128;
const int L=30;
const u128 LOW=(u128)2075<<60, HIGH=(u128)1<<73;
string out128(u128 x){string s;if(!x)return"0";while(x){s.push_back(char('0'+x%10));x/=10;}reverse(s.begin(),s.end());return s;}
u128 invpow2(u128 a,int bits){u128 x=1;for(int i=0;i<8;i++)x*=2-a*x;return x&(((u128)1<<bits)-1);}
bool drops(u128 x,int& step,u128& end){for(int k=1;k<=2000;k++){u128 y=3*x+1;unsigned long long lo=(unsigned long long)y;int a=lo?__builtin_ctzll(lo):64+__builtin_ctzll((unsigned long long)(y>>64));x=y>>a;if(x<LOW){step=k;end=x;return true;}}return false;}
int main(int argc,char**argv){
 int first=argc>1?stoi(argv[1]):0,last=argc>2?stoi(argv[2]):31;
 using boost::multiprecision::cpp_int;
 cpp_int p=1;vector<int> f;
 for(int i=0;i<=500;i++){f.push_back(boost::multiprecision::msb(p));p*=3;}
 vector<int> r(500);for(int i=0;i<500;i++)r[i]=f[i+1]-f[i];
 set<vector<int>> seen;vector<pair<vector<int>,int>> factors;
 for(int s=0;s+L<=500&&factors.size()<31;s++){vector<int>w(r.begin()+s,r.begin()+s+L);if(seen.insert(w).second)factors.push_back({w,s});}
 assert(factors.size()==31&&0<=first&&first<last&&last<=31);
 u128 p3=1;for(int i=0;i<L;i++)p3*=3;
 unsigned long long rows=0;int worst=0,wshift=-1;u128 wseed=0,wend=0;
 for(int i=first;i<last;i++){
  auto [w,shift]=factors[i];int A=0;u128 d=0;
  for(int a:w){d=3*d+((u128)1<<A);A+=a;}
  int bits=A+1;u128 mod=(u128)1<<bits,mask=mod-1;
  u128 residue=(invpow2(p3,bits)*((((u128)1<<A)-d)&mask))&mask;
  u128 q=residue<LOW?(LOW-residue+mod-1)/mod:0;
  for(;;q++){
   u128 seed=residue+q*mod;if(seed>=HIGH)break;
   int k;u128 end;if(!drops(seed,k,end)){cerr<<"FAIL shift="<<shift<<" seed="<<out128(seed)<<"\n";return 2;}
   rows++;if(k>worst){worst=k;wshift=shift;wseed=seed;wend=end;}
  }
 }
 cout<<"range="<<first<<":"<<last<<" rows="<<rows<<" worst="<<worst<<","<<out128(wseed)<<","<<out128(wend)<<",shift="<<wshift<<"\n";
}
