#include <stdio.h>
#include <string.h>

int main()
{
    char str1[20] = "Hello, World!";  // 문자열 초기화
    char str2[20];

    // 문자열 복사
    strcpy(str2, str1);
    printf("str2: %s\n", str2);  // 출력: str2: Hello, World!

    // 문자열 길이
    int length = strlen(str1);
    printf("str1의 길이: %d\n", length);  // 출력: str1의 길이: 13

    // 문자열 비교
    int result = strcmp(str1, str2);
    if (result == 0)
        printf("str1과 str2는 같은 문자열입니다.\n");
    else if (result < 0)
        printf("str1은 str2보다 사전적으로 앞에 있습니다.\n");
    else
        printf("str1은 str2보다 사전적으로 뒤에 있습니다.\n");

    // 문자열 연결
    strcat(str1, " Welcome!");
    printf("str1: %s\n", str1);  // 출력: str1: Hello, World! Welcome!

    return 0;
}


//문자열 입출력
#include <stdio.h>
#include <string.h>

int main()
{
    char str1[20] = "Hello, World!";
    char str2[20];

    printf("문자열을 입력하세요: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = '\0';  // 개행 문자 제거

    printf("str1: %s\n", str1);
    printf("str2: %s\n", str2);

    return 0;
}


//문자열 저장
#include <stdio.h>
#include <string.h>

#define MAX_STRINGS 3
#define MAX_LENGTH 20

int main()
{
    char strings[MAX_STRINGS][MAX_LENGTH];

    // 문자열 저장
    strcpy(strings[0], "Hello");
    strcpy(strings[1], "World");
    strcpy(strings[2], "C");

    // 문자열 출력
    for (int i = 0; i < MAX_STRINGS; i++)
    {
        printf("strings[%d]: %s\n", i, strings[i]);
    }

    return 0;
}
