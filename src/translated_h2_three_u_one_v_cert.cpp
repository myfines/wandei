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
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static constexpr int N=46, CU=3, CV=1; static constexpr unsigned long long ES=832402470ULL, ER=247899900ULL; static constexpr int EW=304; static const u128 LOW=(u128)2075<<60; static u128 LIM=0,P3=1,INV=1; static std::array<unsigned char,N> PATH{};
static u128 p128(const char*s){u128 x=0;for(;*s;++s)x=10*x+(*s-'0');return x;} static std::string ds(u128 x){if(!x)return"0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}std::reverse(s.begin(),s.end());return s;}
static std::vector<std::pair<int,std::array<int,N>>> factors(){cpp_int p=1;std::vector<int>f(401);for(int i=0;i<=400;++i){f[i]=boost::multiprecision::msb(p);p*=3;}std::map<std::vector<int>,int>m;for(int sh=0;sh+N<=400;++sh){std::vector<int>w(N);for(int j=0;j<N;++j)w[j]=f[sh+j+1]-f[sh+j];m.emplace(w,sh);if(m.size()==47)break;}std::vector<std::pair<int,std::array<int,N>>>o;for(auto&kv:m){std::array<int,N>w{};for(int j=0;j<N;++j)w[j]=kv.first[j];o.push_back({kv.second,w});}std::sort(o.begin(),o.end(),[](auto&a,auto&b){return a.first<b.first;});return o;}
struct S{unsigned long long scripts=0,rows=0;int worst=0;u128 seed=0,end=0;}; static std::pair<u128,int> odd(u128 x){u128 y=3*x+1;int a=0;while(!(y&1)){y>>=1;++a;}return{y,a};}
static void leaf(int sh,int A,u128 d,int u,int v,S&st){if(u!=CU||v!=CV)return;++st.scripts;int b=A+1;if(b>=127)abort();u128 mod=(u128)1<<b,mask=mod-1,res=(INV*((((u128)1<<A)-d)&mask))&mask;if(!(res&1))abort();u128 q=res<LOW?(LOW-res+mod-1)/mod:0;for(;;++q){u128 seed=res+q*mod;if(seed>=LIM)break;++st.rows;u128 x=seed;bool fell=false;for(int k=1;k<=1500;++k){auto z=odd(x);x=z.first;if(k<=N&&z.second!=(int)PATH[k-1])abort();if(x<LOW){fell=true;if(k>st.worst){st.worst=k;st.seed=seed;st.end=x;}break;}}if(!fell){std::cerr<<"NO_DESCENT "<<sh<<" "<<ds(seed)<<"\n";abort();}}}
static void dfs(const std::array<int,N>&w,int sh,int j,int h,int u,int v,int A,u128 d,S&st){if(j==N){leaf(sh,A,d,u,v,st);return;}int r=w[j];for(int nh=0;nh<=2;++nh){int a=h+r-nh;if(a<1||a>4)continue;if(h==1&&r==2&&nh==0)continue;int nu=u+((h==0&&nh==1)?1:0),nv=v+((h==1&&nh==2)?1:0);if(nu>CU||nv>CV)continue;PATH[j]=(unsigned char)a;dfs(w,sh,j+1,nh,nu,nv,A+a,3*d+((u128)1<<A),st);}}
int main(int argc,char**argv){LIM=p128("6287967883654920544295");for(int i=0;i<N;++i)P3*=3;INV=1;for(int i=0;i<8;++i)INV*=(u128)2-P3*INV;S tot;int sel=0;for(auto&it:factors()){bool take=argc==1;for(int i=1;i<argc;++i)if(it.first==std::stoi(argv[i]))take=true;if(!take)continue;++sel;S st;dfs(it.second,it.first,0,0,0,0,0,0,st);std::cout<<"FACTOR "<<it.first<<" scripts "<<st.scripts<<" rows "<<st.rows<<" worst "<<st.worst<<" "<<ds(st.seed)<<" "<<ds(st.end)<<"\n"<<std::flush;tot.scripts+=st.scripts;tot.rows+=st.rows;if(st.worst>tot.worst){tot.worst=st.worst;tot.seed=st.seed;tot.end=st.end;}}
std::cout<<"TOTAL "<<sel<<" scripts "<<tot.scripts<<" rows "<<tot.rows<<" worst "<<tot.worst<<" "<<ds(tot.seed)<<" "<<ds(tot.end)<<"\n";if(argc==1){if(sel!=47||tot.scripts!=ES||tot.rows!=ER||tot.worst!=EW||ds(tot.seed)!="5727473727383584829487"||ds(tot.end)!="1271471526915619774637")abort();std::cout<<"CERTIFIED\n";}}