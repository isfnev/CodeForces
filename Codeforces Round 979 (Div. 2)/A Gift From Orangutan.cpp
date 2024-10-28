#include <iostream>
using namespace std ;

int main()
{
	int t;
	cin >> t;

	while(t--)
	{
		int n;
		cin >> n;
		int a[n];

		int max_value = 1;
		int min_value = 1000;

		for(int& i:a)
		{
			cin >> i;
			if (max_value < i)
				max_value = i;
			if (min_value > i)
				min_value = i;
		}
		cout << (max_value - min_value)*(n-1)<<'\n';
	}

	return 0 ;
}