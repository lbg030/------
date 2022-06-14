#include <stdio.h>

int main(void)

{

    int a = 1, b = 2, c = 3;

    printf("%3d%3d%3d\n", a, b, c);

    {

        int b = 4;

        int c = 5;

        printf("%3d%3d%3d\n", a, b, c);

        a = b;

        {

            int c = 6; // 새로운 변수 c 위에서 선언한 c와 다름

            c = b; // c 를 6으로 선언 하였었지만 b값으로 다시 바뀜     6 -> 4

            printf("%3d%3d%3d\n", a, b, c); // 여기서 4 4 4 
        }

        printf("%3d%3d%3d\n", a, b, c); // c가 4로 선언된건 다른 c이므로 영향을 받지 않음 int c = 5 를 따름   4 4 5

        {

            printf("%3d%3d%3d\n", a, b, c); // 4 4 5
        }

        printf("%3d%3d%3d\n", a, b, c); // 4 4 5
    }

    printf("%3d%3d%3d\n", a, b, c); // 여기가 헷갈리실 텐데 a=b에 의해 값이 따로 지정되었었기 때문에 4를 따르는 거고 나머지 b,c는 주소값으로 할당이 아닌 재선언으로 되었기 때문에 값 변화가 없습니다

    return 0;
}