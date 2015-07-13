#include <iostream>
#include <cmath>

using namespace std; 

void louise(long long *n){

int power = 0 ;
long long power_num=2;

	while(power_num<=*n){
		power_num = pow(power_num,power);
		power = power +1 ;

	}
	if(*n==power_num){
			n = n/2 ;
		}
	else{
		*n = *n - pow(2,power-1);
		
	}
	
	if(*n==1){
		cout << "Louise" << endl;
		return ;
	}
	else{
		richard(n);
		}

}


void richard(long long *n){

	
int power = 0 ;
long long power_num=2;
	while(power_num<=*n){
		power_num = pow(power_num,power);
		power = power +1 ;

	}
	if(*n==power_num){
			*n = *n/2 ;
		}
	else{
		*n = *n - pow(2,power-1);
		
	}
	
	if(*n==1){
		cout << "Richard" << endl;
		return ;
	}
	else{
		louise(n);
		}	

}

int main()

{

int testcases ;
long long *n ,input;

cin >> testcases ;
while(testcases--){

	cin >> input;
	n = &input ;
	louise(n);


}
	return 0;

}