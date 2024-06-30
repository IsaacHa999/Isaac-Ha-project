/*
C++의 `std::string` 클래스는 문자열을 쉽고 효율적으로 다루기 위해 다양한 함수를 제공합니다. 여기 일반적으로 자주 사용되는 몇 가지 함수들의 목록과 간단한 설명을 제공합니다:

### 생성 및 할당
- **`string()`**: 빈 문자열을 생성합니다.   ex) string str;
- **`string(const string& str)`**: 복사 생성자, 다른 `std::string` 객체로부터 문자열을 복사합니다.  ex) string strCopy(str);
- **`string(const string& str, size_t pos, size_t len = npos)`**: 부분 문자열을 사용하여 문자열을 생성합니다.  ex) string subStr(str, 7, 5); // "world"
- **`string(const char* s)`**: C 스타일 문자열로부터 `std::string` 객체를 생성합니다.   ex) string fromCString = "C-style string";
- **`string(size_t n, char c)`**: 문자 `c`를 `n`번 반복하여 문자열을 생성합니다.        ex) string repeatedChars(10, '*');
- **`operator=`**: 문자열을 할당합니다. ex) str = "Hello, world!";

### 크기 및 용량
- **`size()` 또는 `length()`**: 문자열의 길이(문자 수)를 반환합니다.    ex) cout << "String length: " << str.length() << endl;
- **`empty()`**: 문자열이 비어 있는지 확인합니다. 비어 있으면 `true`를 반환합니다.
- **`resize(size_t n)`**: 문자열의 크기를 `n`으로 조절합니다.
- **`capacity()`**: 문자열이 할당한 메모리의 크기를 반환합니다.
- **`clear()`**: 문자열의 내용을 지웁니다.

### 요소 접근
- **`operator[]`**: 주어진 위치의 문자에 접근합니다.
- **`at(size_t pos)`**: 주어진 위치의 문자에 접근하며, 범위를 벗어날 경우 `std::out_of_range` 예외를 던집니다.
- **`front()`**: 문자열의 첫 번째 문자를 반환합니다.    ex) cout << "First character: " << str.front() << endl;
- **`back()`**: 문자열의 마지막 문자를 반환합니다.  ex) cout << "Last character: " << str.back() << endl;

### 수정
- **`append(const string& str)`**: 문자열의 끝에 다른 문자열을 추가합니다.
- **`insert(size_t pos, const string& str)`**: 주어진 위치에 문자열을 삽입합니다.
- **`replace(size_t pos, size_t len, const string& str)`**: 문자열의 일부를 다른 문자열로 대체합니다.
- **`erase(size_t pos = 0, size_t len = npos)`**: 문자열의 일부를 제거합니다.
- **`push_back(char c)`**: 문자열의 끝에 문자를 추가합니다.     ex) str.push_back('!');
- **`pop_back()`**: 문자열의 마지막 문자를 제거합니다.  ex) str.pop_back();

### 검색 및 비교
- **`find(const string& str, size_t pos = 0)`**: 주어진 위치에서부터 문자열을 검색하고, 발견된 첫 위치의 인덱스를 반환합니다.   ex) size_t found = str.find("Universe");
- **`rfind(const string& str, size_t pos = npos)`**: 문자열을 역순으로 검색합니다.
- **`compare(const string& str)`**: 두 문자열을 비교하고 결과를 정수로 반환합니다.  ex) int result = str.compare(anotherStr); // 0 if equal, <0 if str is smaller, >0 if str is larger

### 부분 문자열 및 변환
- **`substr(size_t pos = 0, size_t len = npos)`**: 문자열의 부분을 추출하여 새 문자열을 생성합니다.
- **`c_str()`**: 문자열의 C 스타일 표현(널 종료 문자열)을 반환합니다.       ex) const char *cStr = str.c_str();
- **`data()`**: 문자열 데이터에 대한 포인터를 반환합니다.           ex) const char *data = str.data();

이 함수들을 사용하여 문자열의 생성, 수정, 검색, 비교 등 다양한 작업을 수행할 수 있습니다. C++에서 문자열을 다루는 데 이러한 함수들이 매우 유용합니다.
*/

#include <iostream>
#include <string>

using namespace std;

#include <iostream>
#include <string>

using namespace std;

int main()
{
    // 생성 및 할당
    string str = "Hello, world!";
    string strCopy(str);
    cout << "Copied string: " << strCopy << endl;
    string subStr(str, 7, 5); // "world"
    cout << "Substring: " << subStr << endl;
    string repeatedChars(10, '*');
    cout << "repeatedChars: " << repeatedChars << endl;
    string fromCString = "C-style string";
    cout << "From C-style string: " << fromCString << endl;

    // 크기 및 용량
    cout << "String length: " << str.length() << endl;
    cout << "Is string empty? " << (str.empty() ? "Yes" : "No") << endl;
    str.resize(5);
    cout << "Resized string: " << str << endl;
    cout << "Capacity of string: " << str.capacity() << endl;
    str.clear();

    // 요소 접근
    str = "Hello, world!";
    cout << "First character: " << str.front() << endl;
    cout << "Last character: " << str.back() << endl;

    // 수정
    str.append(" How are you?");
    cout << "After append: " << str << endl;
    str.insert(13, " dear");
    cout << "After insert: " << str << endl;
    str.replace(7, 5, "Universe");
    cout << "After replace: " << str << endl;
    str.erase(13, 5);
    cout << "After erase: " << str << endl;
    str.push_back('!');
    cout << "After push_back: " << str << endl;
    str.pop_back();
    cout << "After pop_back: " << str << endl;

    // 검색 및 비교
    size_t found = str.find("Universe");
    if (found != string::npos)
        cout << "'Universe' found at position: " << found << endl;
    string anotherStr = "Hello, Universe! How are you?";
    int result = str.compare(anotherStr); // 0 if equal, <0 if str is smaller, >0 if str is larger
    cout << "Comparison result: " << result << endl;

    // 부분 문자열 및 변환
    string newSubStr = str.substr(7, 8); // "Universe"
    cout << "Substring: " << newSubStr << endl;
    const char *cStr = str.c_str();
    cout << "C-style string: " << cStr << endl;

    return 0;
}
