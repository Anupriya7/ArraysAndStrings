#include<bits/stdc++.h>
using namespace std;


bool checkifUniqueCharacters(string str,int n)
{
    sort(str.begin(),str.end());


    for(int i=0;i<n;i++)
    {
        if(str[i]==str[i+1])
            return false;
    }
    return true;
}

int main()
{
    string str="This is not unique";
    int n=str.length();
    if(checkifUniqueCharacters(str,n))
        cout<<"Unique"<<endl;
    else
        cout<<"false"<<endl;

}