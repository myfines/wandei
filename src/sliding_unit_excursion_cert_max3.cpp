#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using u128=unsigned __int128;
static const int STEPS=46, MAXU=3;
static const u128 LOW=(u128)2075<<60;
static const u128 LIM=(u128)1<<73;

string s128(u128 x){ if(!x)return "0"; string s; while(x){s.push_back('0'+x%10);x/=10;} reverse(s.begin(),s.end());return s; }
u128 p128(const string& s){u128 x=0; for(char c:s)x=x*10+(c-'0'); return x;}

u128 inv_odd_pow2(u128 a,int bits){
    u128 x=1;
    // Newton doubles correct bits; native wrap mod 2^128 is fine.
    for(int i=0;i<8;i++) x = x*(2-a*x);
    if(bits<128) x &= (((u128)1<<bits)-1);
    return x;
}

unsigned long long leaves=0,cands=0,rows=0;
int worstk=0,worstshift=-1; u128 worstseed=0,worstx=0;
bool overflowed=false;
array<u128,80> invs{}; array<bool,80> invok{};
u128 P3=1;

bool first_below(u128 seed,int &kk,u128 &out){
    u128 x=seed;
    const u128 MAXV=~(u128)0;
    for(int k=1;k<=1000;k++){
        if(x>(MAXV-1)/3){ overflowed=true; return false; }
        u128 y=3*x+1;
        int a=0;
        unsigned long long lo=(unsigned long long)y;
        if(lo) a=__builtin_ctzll(lo);
        else { unsigned long long hi=(unsigned long long)(y>>64); a=64+__builtin_ctzll(hi); }
        x=y>>a;
        if(x<LOW){kk=k;out=x;return true;}
    }
    return false;
}

void leaf(int shift,int h,int u,int A,u128 d){
    if(u==0)return;
    leaves++;
    int bits=A+1;
    u128 mod=(u128)1<<bits, mask=mod-1;
    if(!invok[bits]){invs[bits]=inv_odd_pow2(P3,bits);invok[bits]=true;}
    u128 diff=(((u128)1<<A)-d)&mask;
    u128 res=(invs[bits]*diff)&mask;
    if(!(res&1)){ cerr<<"even residue\n"; exit(2); }
    u128 q=0;
    if(res<LOW) q=(LOW-res+mod-1)/mod;
    bool any=false;
    for(;;q++){
        u128 seed=res+q*mod;
        if(seed>=LIM)break;
        if(!any){cands++;any=true;}
        rows++;
        int k;u128 out;
        if(!first_below(seed,k,out)){
            cerr<<"FAIL shift="<<shift<<" seed="<<s128(seed)<<" h="<<h<<" u="<<u<<" A="<<A<<" overflow="<<overflowed<<"\n";
            exit(3);
        }
        if(k>worstk){worstk=k;worstseed=seed;worstx=out;worstshift=shift;}
    }
}

void dfs(const array<int,46>& w,int shift,int pos,int h,int u,int A,u128 d){
    if(pos==STEPS){leaf(shift,h,u,A,d);return;}
    int r=w[pos]; u128 nd=3*d+((u128)1<<A);
    dfs(w,shift,pos+1,h,u,A+r,nd);
    if(h==0 && r==2 && u<MAXU) dfs(w,shift,pos+1,1,u+1,A+1,nd);
    if(h==1) dfs(w,shift,pos+1,0,u,A+r+1,nd);
}

int main(){
    for(int i=0;i<46;i++)P3*=3;
    using boost::multiprecision::cpp_int;
    cpp_int p=1; vector<int> fl;
    for(int i=0;i<=1000;i++){ fl.push_back(boost::multiprecision::msb(p)); p*=3; }
    vector<int> mech(1000); for(int i=0;i<1000;i++) mech[i]=fl[i+1]-fl[i];
    vector<pair<array<int,46>,int>> fac;
    set<array<int,46>> seen;
    for(int sh=0; sh+46<=1000 && fac.size()<47; ++sh){
        array<int,46>w{}; for(int j=0;j<46;j++)w[j]=mech[sh+j];
        if(seen.insert(w).second) fac.push_back({w,sh});
    }
    if(fac.size()!=47){cerr<<"factor count "<<fac.size()<<"\n";return 1;}
    auto t0=chrono::steady_clock::now();
    for(size_t i=0;i<fac.size();i++){
        dfs(fac[i].first,fac[i].second,0,0,0,0,0);
        if(i%5==0){
            double sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
            cerr<<"progress "<<i<<" leaves="<<leaves<<" rows="<<rows<<" worst="<<worstk<<" sec="<<sec<<"\n";
        }
    }
    assert(leaves==104035682ULL);
    assert(cands==47290188ULL);
    assert(rows==47866652ULL);
    assert(worstk==276);
    assert(worstseed==p128("8171827952796853273339"));
    assert(worstx==p128("697521228196614030223"));
    assert(worstshift==31);
    assert(!overflowed);
    cout<<"factors="<<fac.size()<<"\n";
    cout<<"leaves="<<leaves<<"\n";
    cout<<"candidate_classes="<<cands<<"\n";
    cout<<"rows="<<rows<<"\n";
    cout<<"worst="<<worstk<<","<<s128(worstseed)<<","<<s128(worstx)<<","<<worstshift<<"\n";
    cout<<"overflow="<<overflowed<<"\n";
    return 0;
}
