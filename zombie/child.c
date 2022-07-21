#include <stdio.h>
#include <unistd.h> 

int main(int argc, char const *argv[])
{
	setbuf(stdout, NULL);

	char *line = NULL;
    size_t len = 0;
    ssize_t read = 0;
    read = getline(&line, &len, stdin);	
    for(;;){
		printf("%s", line);
		sleep(2);	
	}
	return 0;
}