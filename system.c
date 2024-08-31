#include <stdio.h>
#include <string.h>

typedef struct {
    char name[100];
    char data[1000];
} File;

File files[10];
int file_count = 0;

void create_file(const char *name, const char *data) {
    strcpy(files[file_count].name, name);
    strcpy(files[file_count].data, data);
    file_count++;
}

void read_file(const char *name) {
    for (int i = 0; i < file_count; i++) {
        if (strcmp(files[i].name, name) == 0) {
            printf("File Data: %s\n", files[i].data);
            return;
        }
    }
    printf("File not found\n");
}

typedef struct {
    int pid;
    char name[100];
} Process;

Process processes[10];
int process_count = 0;

void create_process(const char *name) {
    processes[process_count].pid = process_count;
    strcpy(processes[process_count].name, name);
    process_count++;
}

void list_processes() {
    for (int i = 0; i < process_count; i++) {
        printf("Process ID: %d, Name: %s\n", processes[i].pid, processes[i].name);
    }
}

void shell() {
    char command[100];
    while (1) {
        printf("shell> ");
        scanf("%s", command);
        if (strcmp(command, "exit") == 0) {
            break;
        } else if (strcmp(command, "ls") == 0) {
            list_processes();
        } else {
            printf("Unknown command\n");
        }
    }
}

void kernel_main() {
    printf("Kernel Initialized\n");
    // Initialize memory management
    // Initialize process management
}

int main() {
    kernel_main();
    // init_memory();
    // init_processes();
    // init_keyboard();
    // init_display();
    shell();
    return 0;
}
