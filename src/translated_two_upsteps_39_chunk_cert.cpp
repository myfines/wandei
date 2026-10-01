// Exact chunkable certificate for the translated 39-step / <=2 total-upstep class.
//
// Build: g++ -O3 -std=c++20 src/translated_two_upsteps_39_chunk_cert.cpp -o cert39
// Suggested complete partition of the 40 factors:
//   ./cert39 0 8
//   ./cert39 8 16
//   ./cert39 16 24
//   ./cert39 24 32
//   ./cert39 32 40
//
// Local class:
// - start at h=0;
// - 39 odd-only transitions;
// - at most two total upward transitions h->h+1;
// - exclude h=1,r=2,h'=0 (the globally rare a=3 heavy direct repayment).
//
// The sharp boundary altitude certificate gives
//   LOW <= x < HIGH,
// with HIGH=6287967883654920544295.
//
// The exact aggregate of the five chunks is:
//   factors = 40
//   scripts = 992954
//   concrete rows = 594900016
//   worst drop = step 301
//   worst seed = 3922996901307644258171
//   worst endpoint = 2064323270781959543497
//   worst factor first shift = 26

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using u128 = unsigned __int128;

struct State {
    uint8_t h, up, A;
    u128 d;
    u128 code; // 3 bits per valuation; 3*39=117 < 128.
};

const int L = 39;
const u128 LOW = (u128)2075 << 60;

u128 parse128(const string& s) {
    u128 x = 0;
    for (char c : s) x = 10*x + (c-'0');
    return x;
}

string s128(u128 x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0' + x%10)); x/=10; }
    reverse(s.begin(), s.end());
    return s;
}

int ctz128(u128 y) {
    unsigned long long lo = (unsigned long long)y;
    if (lo) return __builtin_ctzll(lo);
    return 64 + __builtin_ctzll((unsigned long long)(y >> 64));
}

u128 inv_odd_mod_2b(u128 a, int bits) {
    u128 x = 1;
    for (int i=0; i<8; ++i) x *= 2 - a*x;
    return x & ((((u128)1) << bits) - 1);
}

pair<u128,int> odd_step(u128 x) {
    u128 y = 3*x + 1;
    int a = ctz128(y);
    return {y >> a, a};
}

bool drop_below_frontier(u128 x, int& step, u128& endpoint) {
    for (step=1; step<=2000; ++step) {
        auto [y,a] = odd_step(x);
        x = y;
        if (x < LOW) { endpoint=x; return true; }
    }
    return false;
}

int main(int argc, char** argv) {
    int flo = argc > 1 ? stoi(argv[1]) : 0;
    int fhi = argc > 2 ? stoi(argv[2]) : 40;
    const u128 HIGH = parse128("6287967883654920544295");

    using boost::multiprecision::cpp_int;
    cpp_int p = 1;
    vector<int> floors;
    for (int i=0; i<=500; ++i) {
        floors.push_back(boost::multiprecision::msb(p));
        p *= 3;
    }
    vector<int> mech(500);
    for (int i=0; i<500; ++i) mech[i]=floors[i+1]-floors[i];

    set<vector<int>> seen;
    vector<pair<vector<int>,int>> factors;
    for (int s=0; s+L<=500 && factors.size()<L+1; ++s) {
        vector<int> w(mech.begin()+s, mech.begin()+s+L);
        if (seen.insert(w).second) factors.push_back({w,s});
    }
    assert(factors.size()==40);
    assert(0<=flo && flo<fhi && fhi<=40);

    u128 pow3=1;
    for (int i=0; i<L; ++i) pow3*=3;

    unsigned long long total_scripts=0, total_rows=0;
    int global_worst=0, worst_shift=-1;
    u128 worst_seed=0, worst_endpoint=0;

    for (int fi=flo; fi<fhi; ++fi) {
        const auto& word=factors[fi].first;
        int shift=factors[fi].second;
        vector<State> states{{0,0,0,0,0}};

        for (int j=0; j<L; ++j) {
            int r=word[j];
            vector<State> next;
            next.reserve(states.size()*3);
            for (const auto& s: states) {
                int max_h_next=s.h+r-1;
                for (int hp=0; hp<=max_h_next; ++hp) {
                    int a=s.h+r-hp;
                    assert(a>=1 && a<=4);

                    // Exclude only the rare h=1,r=2,a=3 direct repayment.
                    if (s.h==1 && r==2 && hp==0) continue;

                    int up_next=s.up+(hp==s.h+1);
                    if (up_next>2) continue;
                    assert(hp<=2);

                    next.push_back(State{
                        (uint8_t)hp,
                        (uint8_t)up_next,
                        (uint8_t)(s.A+a),
                        3*s.d + (((u128)1)<<s.A),
                        s.code | (((u128)a) << (3*j))
                    });
                }
            }
            states.swap(next);
        }

        total_scripts += states.size();
        unordered_map<int,u128> inv_cache;
        unsigned long long factor_rows=0;

        for (const auto& s: states) {
            int bits=s.A+1;
            u128 modulus=((u128)1)<<bits;
            u128 mask=modulus-1;
            u128 inv;
            auto it=inv_cache.find(s.A);
            if (it==inv_cache.end()) {
                inv=inv_odd_mod_2b(pow3,bits);
                inv_cache.emplace(s.A,inv);
            } else inv=it->second;

            u128 residue=(inv*(((((u128)1)<<s.A)-s.d)&mask))&mask;
            assert(residue&1);

            // One representative proves that this entire residue cylinder
            // realizes the exact valuation prefix; lifts by 2^(A+1) share it.
            u128 vr=residue;
            for (int j=0; j<L; ++j) {
                auto [vy,a]=odd_step(vr);
                int expected=(int)((s.code>>(3*j))&7);
                assert(a==expected);
                vr=vy;
            }

            u128 q=residue<LOW ? (LOW-residue+modulus-1)/modulus : 0;
            for (;; ++q) {
                u128 seed=residue+q*modulus;
                if (seed>=HIGH) break;

                int step;
                u128 endpoint;
                if (!drop_below_frontier(seed,step,endpoint)) {
                    cerr << "FAIL factor=" << fi << " shift=" << shift
                         << " seed=" << s128(seed) << "\n";
                    return 2;
                }

                ++factor_rows;
                if (step>global_worst) {
                    global_worst=step;
                    worst_shift=shift;
                    worst_seed=seed;
                    worst_endpoint=endpoint;
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
         << " worst=" << global_worst << ","
         << s128(worst_seed) << "," << s128(worst_endpoint)
         << ",shift=" << worst_shift << "\n";
    return 0;
}
