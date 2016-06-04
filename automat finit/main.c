#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *get_starech(int stare)
{
    if(stare == 0)
        return "E";
    else if(stare == 1)
        return "A";
    else if(stare == 2)
        return "AN";
    else if(stare == 3)
        return "ANA";
}
int stare(int st, char el)
{
    switch(st)
    {
    case 0:
        if(el=='a')
            return 1;
        else if(el=='n')
            return 0;
    break;
    case 1:
        if(el=='n')
            return 2;
        else if(el=='a')
            return 1;
    break;
    case 2:
        if(el=='a')
            return 3;
        else if(el=='n')
            return 0;
    break;
    case 3:
        if(el=='a')
            return 1;
        else if(el=='n')
            return 0;
    }
}
int main()
{
    int i, st, p, cifra, k=0;
    char sir[100];
    printf("Introduceti sirul: ");
    scanf("%s",sir);
    st = 0;
    printf("%s ",get_starech(st));
    for(i=0;i<strlen(sir);i++)
    {
        //cifra = sir[i]-48;
        p = stare(st, sir[i]);
        printf("%c-> %s ",sir[i],get_starech(p));
        st = p;
        if(st==3)
            k++;
    }


    printf("\nCuvantul ana apare de: %d ori\n", k);
    return 0;
}
