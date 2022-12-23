#include <iostream>
#include<stack>
#include<string>
#include <sstream>

using namespace std;
stack<int> db;


void callTop() {
    if(db.empty()){
        cout<<-1<<endl;
        return;
    }
    cout << db.top() <<endl;
}

void callEmpty() {
    if(db.empty()){
        cout<<1<<endl;
        return;
    }
    cout<<0<<endl;
}

void callSize() {
    cout << db.size()<<endl;
}
 
void callPop() {
    if(db.empty()){
        cout<<-1<<endl;
        return;
    }
    cout << db.top()<<endl;
    db.pop();
}

void callPush(string command) {
    stringstream ss(command);
    string number;
    while(getline(ss,number,' ')){}
    db.push(stoi(number));
}

void findCommand(string command) {
    if (command.find("push") != string::npos) {
        callPush(command);
        return;
    }
    if (command == "pop") {
        callPop();
        return;
    }
    if (command == "size") {
        callSize();
        return;
    }
    if (command == "empty") {
        callEmpty();
        return;
    }
    if (command == "top") {
        callTop();
        return;
    }
}

void runCommands(int numbers) {
    while (numbers > 0) {
        char command[20];

        cin.getline(command,20);
        findCommand(command);
        numbers--;
    }
}

int main() {
    int commandNumbers;
    char buffer[1];

    cin >> commandNumbers;
    cin.getline(buffer,1);

    runCommands(commandNumbers);
}
