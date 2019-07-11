
#include<stdio.h>
int num=0;
void fun(int n)
{
	if(n<2)
		return ;
	else if(n==2)
		{
			num++;
			fun(n-2);
		}	
	else
		{
			num++;
			fun(n-2);
		}
}


int main()
{	
	int n=50;    
	fun(n);
	printf("%d\n",num);
	return 0;

}