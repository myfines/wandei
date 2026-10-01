// Exact translated 46-step certificate with defect height at most two.
//
// First-candidate local class:
//   * start at h=0;
//   * all 46 subsequent defect states stay in {0,1,2};
//   * at most two 0->1 entries;
//   * at most one 1->2 entry;
//   * exclude the globally rare heavy direct return h=1,r=2,a=3.
//
// Every length-46 mechanical factor is enumerated.  Each exact valuation
// script determines one 2-adic local-seed cylinder, which is intersected with
//
//     2075*2^60 <= x < 2^73.
//
// Every concrete lift is checked against its valuation prefix and then
// continued under the exact odd-only Syracuse map until it drops below the
// verified frontier.
//
// Build:
//     g++ -O3 -std=c++17 src/translated_h2_one_entry_cert.cpp -o /tmp/h2cert
// Run all factors:
//     /tmp/h2cert
// Optional positional arguments select first-occurrence shifts of factors.

#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

static constexpr int STEPS = 46;
static constexpr int CAP_U = 2;
static constexpr int CAP_V = 1;
static const u128 LOW = (u128)2075 << 60;
static const u128 LOCAL_LIMIT = (u128)1 << 73;

static constexpr unsigned long long EXPECTED_SCRIPTS = 59'605'715ULL;
static constexpr unsigned long long EXPECTED_ROWS = 30'702'092ULL;
static constexpr int EXPECTED_WORST_STEP = 262;

static u128 POW3 = 1;
static u128 INV3 = 1;
static std::array<unsigned char, STEPS> PATH{};

static std::string decimal_u128(u128 x) {
    if (x == 0) return "0";
    std::string out;
    while (x) {
        out.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

static std::vector<std::pair<int, std::array<int, STEPS>>> all_factors() {
    cpp_int p = 1;
    std::vector<int> floors(401);
    for (int i = 0; i <= 400; ++i) {
        floors[i] = boost::multiprecision::msb(p);
        p *= 3;
    }

    std::map<std::vector<int>, int> seen;
    for (int shift = 0; shift + STEPS <= 400; ++shift) {
        std::vector<int> word(STEPS);
        for (int j = 0; j < STEPS; ++j)
            word[j] = floors[shift + j + 1] - floors[shift + j];
        seen.emplace(word, shift);
        if (seen.size() == STEPS + 1) break;
    }
    if (seen.size() != STEPS + 1) std::abort();

    std::vector<std::pair<int, std::array<int, STEPS>>> out;
    for (const auto& kv : seen) {
        std::array<int, STEPS> word{};
        for (int j = 0; j < STEPS; ++j) word[j] = kv.first[j];
        out.push_back({kv.second, word});
    }
    std::sort(out.begin(), out.end(), [](const auto& a, const auto& b) {
        return a.first < b.first;
    });
    return out;
}

struct Stats {
    unsigned long long scripts = 0;
    unsigned long long rows = 0;
    int worst_step = 0;
    u128 worst_seed = 0;
    u128 worst_endpoint = 0;
};

static std::pair<u128, int> odd_step(u128 x) {
    u128 y = 3 * x + 1;
    int a = 0;
    while ((y & 1) == 0) {
        y >>= 1;
        ++a;
    }
    return {y, a};
}

static void check_leaf(int shift, int A, u128 affine_d, Stats& st) {
    ++st.scripts;

    const int bits = A + 1;
    if (bits >= 127) std::abort();
    const u128 modulus = (u128)1 << bits;
    const u128 mask = modulus - 1;
    const u128 rhs = (((u128)1 << A) - affine_d) & mask;
    const u128 residue = (INV3 * rhs) & mask;
    if ((residue & 1) == 0) std::abort();

    u128 q = 0;
    if (residue < LOW) q = (LOW - residue + modulus - 1) / modulus;

    for (;; ++q) {
        const u128 seed = residue + q * modulus;
        if (seed >= LOCAL_LIMIT) break;
        ++st.rows;

        u128 x = seed;
        bool fell = false;
        int fall_step = 0;
        u128 endpoint = 0;

        for (int step = 1; step <= 2000; ++step) {
            auto [next, a] = odd_step(x);
            x = next;
            if (step <= STEPS && a != int(PATH[step - 1])) {
                std::cerr << "prefix verification failure at factor shift "
                          << shift << ", step " << step << "\n";
                std::abort();
            }
            if (x < LOW) {
                fell = true;
                fall_step = step;
                endpoint = x;
                break;
            }
        }

        if (!fell) {
            std::cerr << "NO DESCENT for seed " << decimal_u128(seed)
                      << " at factor shift " << shift << "\n";
            std::abort();
        }

        if (fall_step > st.worst_step) {
            st.worst_step = fall_step;
            st.worst_seed = seed;
            st.worst_endpoint = endpoint;
        }
    }
}

static void dfs(const std::array<int, STEPS>& mechanical,
                int shift,
                int j,
                int h,
                int count_u,
                int count_v,
                int A,
                u128 affine_d,
                Stats& st) {
    if (j == STEPS) {
        check_leaf(shift, A, affine_d, st);
        return;
    }

    const int r = mechanical[j];

    for (int next_h = 0; next_h <= 2; ++next_h) {
        const int a = h + r - next_h;
        if (a < 1 || a > 4) continue;

        // Globally rare odd-height r=2 direct repayment, treated separately
        // by sharp_repayment_phase_cert.py.
        if (h == 1 && r == 2 && a == 3) continue;

        const int next_u = count_u + ((h == 0 && next_h == 1) ? 1 : 0);
        const int next_v = count_v + ((h == 1 && next_h == 2) ? 1 : 0);
        if (next_u > CAP_U || next_v > CAP_V) continue;

        PATH[j] = (unsigned char)a;
        dfs(mechanical,
            shift,
            j + 1,
            next_h,
            next_u,
            next_v,
            A + a,
            3 * affine_d + ((u128)1 << A),
            st);
    }
}

int main(int argc, char** argv) {
    for (int i = 0; i < STEPS; ++i) POW3 *= 3;

    // Newton iteration gives the inverse of the odd number 3^46 modulo 2^128.
    // Unsigned overflow is reduction modulo 2^128; masking later yields the
    // inverse modulo every 2^(A+1) used by this certificate.
    INV3 = 1;
    for (int i = 0; i < 8; ++i) INV3 *= (u128)2 - POW3 * INV3;

    const auto factors = all_factors();
    Stats total;
    int selected_count = 0;

    for (const auto& item : factors) {
        const int shift = item.first;
        const auto& word = item.second;

        bool selected = (argc == 1);
        for (int i = 1; i < argc; ++i)
            if (shift == std::stoi(argv[i])) selected = true;
        if (!selected) continue;
        ++selected_count;

        Stats st;
        dfs(word, shift, 0, 0, 0, 0, 0, 0, st);

        std::cout << "FACTOR " << shift
                  << " scripts " << st.scripts
                  << " rows " << st.rows
                  << " worst " << st.worst_step
                  << " " << decimal_u128(st.worst_seed)
                  << " " << decimal_u128(st.worst_endpoint) << "\n";

        total.scripts += st.scripts;
        total.rows += st.rows;
        if (st.worst_step > total.worst_step) {
            total.worst_step = st.worst_step;
            total.worst_seed = st.worst_seed;
            total.worst_endpoint = st.worst_endpoint;
        }
    }

    std::cout << "SELECTED_FACTORS " << selected_count << "\n";
    std::cout << "TOTAL_SCRIPTS " << total.scripts << "\n";
    std::cout << "TOTAL_ROWS " << total.rows << "\n";
    std::cout << "WORST " << total.worst_step
              << " " << decimal_u128(total.worst_seed)
              << " " << decimal_u128(total.worst_endpoint) << "\n";

    if (argc == 1) {
        if (selected_count != 47 ||
            total.scripts != EXPECTED_SCRIPTS ||
            total.rows != EXPECTED_ROWS ||
            total.worst_step != EXPECTED_WORST_STEP ||
            decimal_u128(total.worst_seed) != "3345476547508506755675" ||
            decimal_u128(total.worst_endpoint) != "2003311712042859815183") {
            std::abort();
        }
        std::cout << "CERTIFIED\n";
    }
}
