#include <iostream>
#include <vector>
#include <utility>

using namespace std ;
vector <long long> boxes_seq ;

int main() {

long long boxes ,chocolates=0 ,number_of_ways=0,min=999909999; 
 //input logic
cin >> boxes ; 
while(boxes --){

	 cin >> chocolates ;
	 boxes_seq.push_back(chocolates) ;
	 if (chocolates < min){ //minima logic
	 	min = chocolates ;
	 }
 
 

 }
 //problem logic
 //don't let the opponent to left the boxes alone 
 //play safe by taking out only 1 
 vector<long long>::iterator it ;
	 for(it = boxes_seq.begin(); it< boxes_seq.end(); it++){

	 	//cout << *it << endl;
	 	if (*it> min){
	 		number_of_ways++ ;
	 	//	cout << number_of_ways << endl; 
	 	}

	 }

cout << number_of_ways << endl ; 
	return 0 ; 
}