cpp_code = """
#include<iostream>
using namespace std;
int main(){
    cout<<"Awesome..."<<endl;
    return 0;
}
"""

print(cpp_code)

java_code = """
class MyApp{
    public static void main(String[] args){
        System.out.println("This is Awesome...");
    }
}
"""

file1 = open("/Users/ishant/Downloads/myapp.cpp", "w")
file2 = open("/Users/ishant/Downloads/MyApp.java", "w")
file1.write(cpp_code)
file2.write(java_code)
print("Source Code Created")