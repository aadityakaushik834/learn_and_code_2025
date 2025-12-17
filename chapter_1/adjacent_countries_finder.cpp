#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, string> countryMap = {
        {"IN", "Pakistan, China, Nepal, Bhutan, Bangladesh, Myanmar"},
        {"US", "Canada, Mexico"},
        {"NZ", "None"},
        {"FR", "Belgium, Luxembourg, Germany, Switzerland, Italy, Spain"},
        {"CA", "United States"}
    };

    string code;
    cout << "Enter Country Code: ";
    cin >> code;

    if (countryMap.find(code) != countryMap.end()) {
        cout << "Adjacent Countries: " << countryMap[code] << endl;
    } else {
        cout << "Unknown country code!" << endl;
    }
    return 0;
}
