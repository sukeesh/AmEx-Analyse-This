#include <bits/stdc++.h>

using namespace std;

int main(){
	string str[3];
	str[0] = "Supp";
	str[1] = "Elite";
	str[2] = "Credit";
	string new_str;
	cin >> new_str;
	for ( int i = 0 ; i < new_str.size() && i < 1000 ; i ++ ){
		if ( new_str[i] == '0' ){
			cout << str[0] << endl;
		}
		else if ( new_str[i] == '1' ){
			cout << str[1] << endl;
		}
		else{
			cout << str[2] << endl;
		}
	}
	return 0;
}