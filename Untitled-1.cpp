#include<iostream>
using namespace std;
float Sn(float a,float r,int n){
    float Sn=a;
    int pow=0;
    while(n>pow){
        for(int i=0;i<pow;i++){
            Sn+=a*r;
        }
        pow+=1;            
        }
    return Sn;
}

int main(){
    float a=10,r=10,n=2;

    //test
    cout << Sn(a,r,n) << Sn(a,r,1)/3;

    while(true){
        for(int i=1;i<10;i++){
            float S1 = Sn(a,r,i+1);
            float S2 = Sn(a,r,i);
            if(S1/3<=S2 && S2<=S1*3){
                cout << r << endl;
            }

        }
        //a+=0.1;
        r+=0.1;

    }
    system("pause");
    return 0;
}
