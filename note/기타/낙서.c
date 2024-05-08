#include <stdio.h>
#include <fcntl.h>

main()
{
    char c;
    int fd;
    char filename[20];

    printf("Enter the name of the file:");
    gets(filename);
    fd = open(filename, O_RDONLY);

    lseek(fd, 501L, 0);

    while (read(fd, &c, 1) != 0)
        write(1, &c, 1);

    close(fd);
}