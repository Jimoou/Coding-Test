#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* overwrite_string, int s) {
	size_t my_string_length = strlen(my_string);
	size_t overwrite_length = strlen(overwrite_string);
	char* answer = (char*)malloc((my_string_length + 1) * sizeof(char));
	strcpy(answer, my_string);
	strncpy(answer + s, overwrite_string, overwrite_length);

	return answer;
}