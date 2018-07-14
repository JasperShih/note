#include <stdio.h>
#include <stdarg.h>

void boo(int num, ...)
{
    va_list args;
    va_start(args, num);
    
    printf("%d", num); // 1
    num = va_arg(args, int);
    printf("%d", num); // 2
    num = va_arg(args, int);
    printf("%d", num); // 3
    
    //num = va_arg(args, int);
    //printf("%d", num); maybe crash
    
    va_end(args);
}

int main()
{
    boo(1, 2, 3);
    return 0;
}
