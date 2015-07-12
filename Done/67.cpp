#include<iostream>
#include<fstream>
using namespace std;
const int N=100;
int func(int x, int y, int arr[N][N]);
int arr[N][N];
int ans[N][N]={0};
int main()
{
	int i, j, k, l, m, n;

	ifstream f;
	f.open("inp1.txt");
	for(i=0;i<N;i++)
	{
		for(j=0;j<=i;j++)
		{
			f>>arr[i][j];
		}
	}
	long int max=0;
	for(i=0;i<N;i++)
	{
		m=func(N-1,i,arr);
		if(m > max)
			max=m;
	}
	cout<<max<<endl;
//	for(i=0;i<N;i++)
//	{
//		for(j=0;j<=i;j++)
//		{
//			cout<<ans[i][j]<<' ';
//		}
//		cout<<endl;
//	}
	f.close();
	return 0;
}
int func(int x, int y, int arr[N][N])
{

	if(ans[x][y]>0)
		return ans[x][y];
	if(y<0)
		return 0;
	if(x==0 && y==0)
	{
		ans[x][y]=arr[x][y];
		return ans[x][y];
	}
	if(y==0)
	{
		ans[x][y]=arr[x][y]+func(x-1,y, arr);
		return ans[x][y];
	}
	if(y>x)
	{
		ans[x][y]=0;
		return 0;
	}
	ans[x][y]=arr[x][y]+max(func(x-1,y,arr), func(x-1,y-1,arr));
	return ans[x][y];
}
