// Exact chunkable certificate for the translated 41-step low-height class.
//
// Build:
//   g++ -O3 -std=c++20 src/translated_lowheight_three_upcross_41_chunk_cert.cpp -o cert41low
//
// A complete partition used for the recorded certificate is:
//   ./cert41low 0 4
//   ./cert41low 4 8
//   ./cert41low 8 11
//   ./cert41low 11 22
//   ./cert41low 22 32
//   ./cert41low 32 42
//
// Local class:
// - start at h=0;
// - 41 odd-only transitions;
// - every state stays in {0,1};
// - at most three 0->1 upcrossings;
// - exclude h=1,r=2,a=3, the globally rare heavy direct repayment.
//
// Exact aggregate of the chunks above:
//   factors = 42
//   scripts = 5,596,528
//   concrete local seeds = 379,556,603
//   every seed falls below the verified frontier
//   worst drop = odd step 297
//   worst seed = 6114300038360557642401
//   worst endpoint = 635537898295088599553
//
// The local boundary interval is the sharp certified window
//   2075*2^60 <= x < 6287967883654920544295.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using u128 = unsigned __int128;

struct State { uint8_t h, up, A; u128 d; };

const int L = 41;
const u128 LOW = (u128)2075 << 60;

u128 parse128(const string& s) {
    u128 x=0;
    for (char c: s) x=10*x+(c-'0');
    return x;
}

string s128(u128 x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0'+x%10)); x/=10; }
    reverse(s.begin(),s.end());
    return s;
}

int ctz128(u128 y) {
    unsigned long long lo=(unsigned long long)y;
    return lo ? __builtin_ctzll(lo)
              : 64+__builtin_ctzll((unsigned long long)(y>>64));
}

u128 invodd(u128 a,int bits) {
    u128 x=1;
    for (int i=0;i<8;i++) x*=2-a*x;
    return x & ((((u128)1)<<bits)-1);
}

bool drop(u128 x,int& step,u128& endpoint) {
    for (step=1;step<=2000;step++) {
        u128 y=3*x+1;
        int a=ctz128(y);
        x=y>>a;
        if (x<LOW) { endpoint=x; return true; }
    }
    return false;
}

int main(int argc,char** argv) {
    int flo=argc>1?stoi(argv[1]):0;
    int fhi=argc>2?stoi(argv[2]):42;
    const u128 HIGH=parse128("6287967883654920544295");

    using boost::multiprecision::cpp_int;
    cpp_int p=1;
    vector<int> floors;
    for (int i=0;i<=500;i++) { floors.push_back(boost::multiprecision::msb(p)); p*=3; }
    vector<int> mech(500);
    for (int i=0;i<500;i++) mech[i]=floors[i+1]-floors[i];

    set<vector<int>> seen;
    vector<pair<vector<int>,int>> factors;
    for (int s=0;s+L<=500 && factors.size()<L+1;s++) {
        vector<int> w(mech.begin()+s,mech.begin()+s+L);
        if (seen.insert(w).second) factors.push_back({w,s});
    }
    assert(factors.size()==42);
    assert(0<=flo && flo<fhi && fhi<=42);

    u128 pow3=1;
    for (int i=0;i<L;i++) pow3*=3;

    unsigned long long total_scripts=0,total_rows=0;
    int worst=0,worst_shift=-1;
    u128 worst_seed=0,worst_endpoint=0;

    for (int fi=flo;fi<fhi;fi++) {
        const auto& word=factors[fi].first;
        int shift=factors[fi].second;
        vector<State> states{{0,0,0,0}};

        for (int r:word) {
            vector<State> next;
            next.reserve(states.size()*3);
            for (const auto& s:states) {
                // Stay at the same defect height: a=r.
                next.push_back({s.h,s.up,(uint8_t)(s.A+r),3*s.d+(((u128)1)<<s.A)});

                // Unit boundary departure 0->1: necessarily r=2,a=1.
                if (s.h==0 && r==2 && s.up<3)
                    next.push_back({1,(uint8_t)(s.up+1),(uint8_t)(s.A+1),3*s.d+(((u128)1)<<s.A)});

                // Low-height return 1->0 through r=1,a=2 only.
                // The alternative r=2,a=3 is excluded and globally bounded
                // by the sharp repayment-phase certificate.
                if (s.h==1 && r==1)
                    next.push_back({0,s.up,(uint8_t)(s.A+2),3*s.d+(((u128)1)<<s.A)});
            }
            states.swap(next);
        }

        total_scripts += states.size();
        unordered_map<int,u128> inv_cache;
        unsigned long long factor_rows=0;

        for (const auto& s:states) {
            int bits=s.A+1;
            u128 mod=((u128)1)<<bits, mask=mod-1;
            u128 inv;
            auto it=inv_cache.find(s.A);
            if (it==inv_cache.end()) {
                inv=invodd(pow3,bits);
                inv_cache[s.A]=inv;
            } else inv=it->second;

            u128 residue=(inv*(((((u128)1)<<s.A)-s.d)&mask))&mask;
            assert(residue&1);
            u128 q=residue<LOW ? (LOW-residue+mod-1)/mod : 0;

            for (;;q++) {
                u128 seed=residue+q*mod;
                if (seed>=HIGH) break;
                int step; u128 endpoint;
                if (!drop(seed,step,endpoint)) {
                    cerr << "FAIL factor=" << fi << " shift=" << shift
                         << " seed=" << s128(seed) << "\n";
                    return 2;
                }
                factor_rows++;
                if (step>worst) {
                    worst=step; worst_shift=shift;
                    worst_seed=seed; worst_endpoint=endpoint;
                }
            }
        }

        total_rows += factor_rows;
        cerr << "FACTOR " << fi << " shift=" << shift
             << " scripts=" << states.size()
             << " rows=" << factor_rows << "\n";
    }

    cout << "CERTIFIED range=" << flo << ":" << fhi
         << " scripts=" << total_scripts
         << " rows=" << total_rows
         << " worst=" << worst << "," << s128(worst_seed)
         << "," << s128(worst_endpoint)
         << ",shift=" << worst_shift << "\n";
    return 0;
}
