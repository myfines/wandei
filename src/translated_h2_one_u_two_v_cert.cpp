// Exact translated 46-step certificate for the last three-upstep case.
// Start at h=0; stay in {0,1,2}; require exactly one 0->1 entry U and
// exactly two 1->2 entries V; exclude the globally rare h=1,r=2 direct
// repayment to h=0.  All 47 length-46 mechanical factors are covered.

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

static constexpr int STEPS=46, CAP_U=1, CAP_V=2;
static const u128 LOW=(u128)2075<<60;
static constexpr unsigned long long EXPECTED_SCRIPTS=61'175'686ULL;
static constexpr unsigned long long EXPECTED_ROWS=17'737'070ULL;
static constexpr int EXPECTED_WORST_STEP=283;
static u128 LIMIT=0, POW3=1, INV3=1;
static std::array<unsigned char,STEPS> PATH{};

static u128 parse128(const char*s){u128 x=0;for(;*s;++s)x=10*x+unsigned(*s-'0');return x;}
static std::string dec128(u128 x){if(!x)return"0";std::string s;while(x){s.push_back(char('0'+x%10));x/=10;}std::reverse(s.begin(),s.end());return s;}

static std::vector<std::pair<int,std::array<int,STEPS>>> factors(){
 cpp_int p=1;std::vector<int>f(401);for(int i=0;i<=400;++i){f[i]=boost::multiprecision::msb(p);p*=3;}
 std::map<std::vector<int>,int> seen;for(int sh=0;sh+STEPS<=400;++sh){std::vector<int>w(STEPS);for(int j=0;j<STEPS;++j)w[j]=f[sh+j+1]-f[sh+j];seen.emplace(w,sh);if(seen.size()==47)break;}
 if(seen.size()!=47)std::abort();std::vector<std::pair<int,std::array<int,STEPS>>>out;
 for(auto&kv:seen){std::array<int,STEPS>w{};for(int j=0;j<STEPS;++j)w[j]=kv.first[j];out.push_back({kv.second,w});}
 std::sort(out.begin(),out.end(),[](auto&a,auto&b){return a.first<b.first;});return out;
}

struct Stats{unsigned long long scripts=0,rows=0;int worst=0;u128 seed=0,end=0;};
static std::pair<u128,int> odd(u128 x){u128 y=3*x+1;int a=0;while((y&1)==0){y>>=1;++a;}return{y,a};}

static void leaf(int sh,int A,u128 d,int cu,int cv,Stats&st){
 if(cu!=1||cv!=2)return;++st.scripts;int bits=A+1;if(bits>=127)std::abort();u128 mod=(u128)1<<bits,mask=mod-1;
 u128 rhs=(((u128)1<<A)-d)&mask,res=(INV3*rhs)&mask;if(!(res&1))std::abort();u128 q=0;if(res<LOW)q=(LOW-res+mod-1)/mod;
 for(;;++q){u128 seed=res+q*mod;if(seed>=LIMIT)break;++st.rows;u128 x=seed;bool fell=false;
  for(int s=1;s<=2000;++s){auto z=odd(x);x=z.first;if(s<=STEPS&&z.second!=(int)PATH[s-1])std::abort();if(x<LOW){fell=true;if(s>st.worst){st.worst=s;st.seed=seed;st.end=x;}break;}}
  if(!fell){std::cerr<<"NO DESCENT factor "<<sh<<" seed "<<dec128(seed)<<"\n";std::abort();}}
}

static void dfs(const std::array<int,STEPS>&w,int sh,int j,int h,int cu,int cv,int A,u128 d,Stats&st){
 if(j==STEPS){leaf(sh,A,d,cu,cv,st);return;}int r=w[j];for(int nh=0;nh<=2;++nh){int a=h+r-nh;if(a<1||a>4)continue;
  if(h==1&&r==2&&nh==0)continue;int nu=cu+((h==0&&nh==1)?1:0),nv=cv+((h==1&&nh==2)?1:0);if(nu>CAP_U||nv>CAP_V)continue;
  PATH[j]=(unsigned char)a;dfs(w,sh,j+1,nh,nu,nv,A+a,3*d+((u128)1<<A),st);}
}

int main(int argc,char**argv){
 LIMIT=parse128("6287967883654920544295");for(int i=0;i<STEPS;++i)POW3*=3;INV3=1;for(int i=0;i<8;++i)INV3*=(u128)2-POW3*INV3;
 auto fs=factors();Stats total;int selected=0;for(auto&it:fs){bool take=(argc==1);for(int i=1;i<argc;++i)if(it.first==std::stoi(argv[i]))take=true;if(!take)continue;++selected;Stats st;
  dfs(it.second,it.first,0,0,0,0,0,0,st);std::cout<<"FACTOR "<<it.first<<" scripts "<<st.scripts<<" rows "<<st.rows<<" worst "<<st.worst<<" "<<dec128(st.seed)<<" "<<dec128(st.end)<<"\n";
  total.scripts+=st.scripts;total.rows+=st.rows;if(st.worst>total.worst){total.worst=st.worst;total.seed=st.seed;total.end=st.end;}}
 std::cout<<"SELECTED_FACTORS "<<selected<<"\nTOTAL_SCRIPTS "<<total.scripts<<"\nTOTAL_ROWS "<<total.rows<<"\nWORST "<<total.worst<<" "<<dec128(total.seed)<<" "<<dec128(total.end)<<"\n";
 if(argc==1){if(selected!=47||total.scripts!=EXPECTED_SCRIPTS||total.rows!=EXPECTED_ROWS||total.worst!=EXPECTED_WORST_STEP||dec128(total.seed)!="4942811925495116845049"||dec128(total.end)!="1802150773986880577533")std::abort();std::cout<<"CERTIFIED\n";}
}
