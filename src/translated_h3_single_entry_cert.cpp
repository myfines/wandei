// Exact translated 46-step certificate through defect height three.
//
// Local class:
//   * start at h=0;
//   * all states stay in {0,1,2,3};
//   * each upward entry 0->1, 1->2, 2->3 occurs at most once;
//   * exclude positive odd-height r=2 direct repayments to h=0.
//
// The excluded direct repayments are globally covered by
// sharp_repayment_phase_cert.py (at most five in the full first candidate).
//
// Build:
//   g++ -O3 -std=c++17 src/translated_h3_single_entry_cert.cpp -o /tmp/h3cert
// Run:
//   /tmp/h3cert

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
static const u128 LOW = (u128)2075 << 60;
static const u128 LOCAL_LIMIT = (u128)1 << 73;

static constexpr unsigned long long EXPECTED_SCRIPTS = 67'075'614ULL;
static constexpr unsigned long long EXPECTED_ROWS = 35'382'699ULL;
static constexpr int EXPECTED_WORST_STEP = 259;

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
            if (step <= STEPS && a != int(PATH[step - 1])) std::abort();
            if (x < LOW) {
                fell = true;
                fall_step = step;
                endpoint = x;
                break;
            }
        }
        if (!fell) {
            std::cerr << "NO DESCENT: " << decimal_u128(seed) << "\n";
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
                int count_t,
                int A,
                u128 affine_d,
                Stats& st) {
    if (j == STEPS) {
        check_leaf(shift, A, affine_d, st);
        return;
    }

    const int r = mechanical[j];
    for (int next_h = 0; next_h <= 3; ++next_h) {
        const int a = h + r - next_h;
        if (a < 1 || a > 5) continue;

        // Direct repayment of a positive odd defect at r=2 is one of the
        // globally rare sharp-phase events; exclude it from this clean class.
        if ((h == 1 || h == 3) && r == 2 && next_h == 0) continue;

        const int next_u = count_u + ((h == 0 && next_h == 1) ? 1 : 0);
        const int next_v = count_v + ((h == 1 && next_h == 2) ? 1 : 0);
        const int next_t = count_t + ((h == 2 && next_h == 3) ? 1 : 0);
        if (next_u > 1 || next_v > 1 || next_t > 1) continue;

        PATH[j] = (unsigned char)a;
        dfs(mechanical,
            shift,
            j + 1,
            next_h,
            next_u,
            next_v,
            next_t,
            A + a,
            3 * affine_d + ((u128)1 << A),
            st);
    }
}

int main(int argc, char** argv) {
    for (int i = 0; i < STEPS; ++i) POW3 *= 3;
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
        dfs(word, shift, 0, 0, 0, 0, 0, 0, 0, st);
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
            decimal_u128(total.worst_seed) != "4780127247684938901371" ||
            decimal_u128(total.worst_endpoint) != "848117883565327063261") {
            std::abort();
        }
        std::cout << "CERTIFIED\n";
    }
}
