#define _CRT_SECURE_NO_WARNINGS    // fopen 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>     // fopen, fputs, fclose 함수가 선언된 헤더 파일

int main()
{
    char name[256];
    char id[20];
    char str[30];
    
    FILE *fp = fopen("hello.txt", "w");    // hello.txt 파일을 쓰기/읽기 모드(w+)로 열기.
    
    //출력
    printf("이름을 입력하세요: ");
    fgets(name, sizeof(name), stdin); //gets는 한줄단위고 scanf 는 공백을 읽을 수 없음 fgets는 한줄 띄우기까지
    
    fputs(name, fp);   // 파일에 문자열 저장
    printf("학번을 입력하세요: ");
    scanf("%s", id);
    fputs(id, fp);
    fclose(fp);

    FILE *f = fopen("hello.txt", "r");
    // 입력
    fgets(str, sizeof(name), fp);
    printf("My name is %s", str);
    fgets(str, sizeof(id), fp);
    printf("MY ID is %s ", str);
    fclose(fp);    // 파일 포인터 닫기

    fclose(fp);
    return 0;
}