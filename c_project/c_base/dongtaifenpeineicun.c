#include <stdio.h>
#include <stdlib.h>
#define  N  (5)
#define  N1 (7)
#define  N2 (3)

int main()
{
    int *ip;
    int *large_ip;
    int *small_ip;
    if((ip = (int*)malloc(N * sizeof(int))) == NULL)
    {
        printf("memory allocated failed!\n");
        exit(1);
    }
    int i;
    for(i = 0; i < N; i++)
    {
        ip[i] = i;
        printf("ip[%d] = %d\t", i, ip[i]);
    }
    printf("\n");
    if((large_ip = (int* )realloc(ip, N1 * sizeof(int))) == NULL)
    {
        printf("memory allocated failed!\n");
        exit(1);
    }
    for(i = N; i < N1; i++)
        large_ip[i] = 9;
    for(i = 0; i < N1; i++)
        printf("large_ip[%d] = %d\t", i, large_ip[i]);
    printf("\n");
    if((small_ip = (int*)realloc(large_ip, N2 * sizeof(int))) == NULL)
    {
        printf("memory allocated failed!\n");
        exit(1);
    }
    for(i = 0; i < N2; i++)
        printf("small_ip[%d] = %d\t", i, small_ip[i]);
    printf("\n");
    free(small_ip);
    small_ip = NULL;
    system("pause");
    return 0;
}