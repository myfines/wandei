#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using u128=unsigned __int128;
const u128 LOW=(u128)2075<<60, LIM=(u128)1<<73;
string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
u128 inv2(u128 a,int bits){u128 x=1;for(int i=0;i<8;i++)x=x*(2-a*x);return x&(((u128)1<<bits)-1);}
bool below(u128 seed,int&kk,u128&out){u128 x=seed,MAXV=~(u128)0;for(int k=1;k<=2000;k++){if(x>(MAXV-1)/3)return false;u128 y=3*x+1; unsigned long long lo=(unsigned long long)y;int a=lo?__builtin_ctzll(lo):64+__builtin_ctzll((unsigned long long)(y>>64));x=y>>a;if(x<LOW){kk=k;out=x;return true;}}return false;}
struct R{bool ok; unsigned long long rows; int wk,ws;u128 seed,x;};
R check(int N,const vector<int>&m){set<vector<int>>seen;vector<pair<vector<int>,int>>fac;for(int sh=0;sh+N<=(int)m.size()&&fac.size()<(size_t)N+1;sh++){vector<int>w(m.begin()+sh,m.begin()+sh+N);if(seen.insert(w).second)fac.push_back({w,sh});}if(fac.size()!=N+1){cerr<<"factorcount fail "<<N<<" "<<fac.size()<<"\n";exit(2);}u128 p3=1;for(int i=0;i<N;i++)p3*=3;unsigned long long rows=0;int wk=0,ws=-1;u128 wseed=0,wx=0;
for(auto &[w,sh]:fac){int A=0;u128 d=0;for(int a:w){d=3*d+((u128)1<<A);A+=a;}int bits=A+1;u128 mod=(u128)1<<bits,mask=mod-1;u128 inv=inv2(p3,bits);u128 res=(inv*((((u128)1<<A)-d)&mask))&mask;u128 q=0;if(res<LOW)q=(LOW-res+mod-1)/mod;for(;;q++){u128 seed=res+q*mod;if(seed>=LIM)break;int k;u128 x;if(!below(seed,k,x)){cout<<"FAIL N="<<N<<" shift="<<sh<<" A="<<A<<" seed="<<s128(seed)<<" rows_before="<<rows<<"\n";return {false,rows,wk,sh,seed,0};}if(k>wk){wk=k;ws=sh;wseed=seed;wx=x;}rows++;}}
cout<<"OK N="<<N<<" factors="<<fac.size()<<" rows="<<rows<<" worst="<<wk<<","<<s128(wseed)<<","<<s128(wx)<<",shift="<<ws<<"\n";return {true,rows,wk,ws,wseed,wx};}
int main(){
    using boost::multiprecision::cpp_int;
    cpp_int p=1; vector<int>fl;
    for(int i=0;i<=500;i++){fl.push_back(boost::multiprecision::msb(p));p*=3;}
    vector<int>m(500);for(int i=0;i<500;i++)m[i]=fl[i+1]-fl[i];
    R r=check(31,m);
    assert(r.ok);
    assert(r.rows==184782336ULL);
    assert(r.wk==330);
    assert(r.ws==36);
    assert(r.seed==(u128)8355649853805505174ULL*1000 + 523ULL);
    assert(r.x==(u128)1072053775599191922ULL*1000 + 857ULL);
}
