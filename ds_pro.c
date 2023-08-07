#include<stdio.h> 
#include<stdlib.h>                              
#include<conio.h>
#include<string.h>
#include<time.h>
char user_input[20];
int main()
{   system("cls");
    printf("WELCOME TO RANDOM-BOX\n");
    printf("COLLECTION OF RANDOM TOOLS......\n");
    printf("AVAILABLE RANDOM TOOLS ARE :\n1. CHROME \n2. NOTEPAD \n3. YOUTUBE \n4. CHATGPT \n5. BARD \n ");
    while(1)
    {
        printf("user ==> ");
        gets(user_input);
        if(strcmp(user_input,"exit")==0)
        {
            system("cls");
            printf("bot ==> ok byy\n");
            break;
        }
        else if(strcmp(user_input,"hi")==0)
        {
            printf("bot ==> hi sir\n");
        }
        else if(strcmp(user_input,"open chrome")==0)
        {
            printf("ok sir , opening chrome browser \n");
            system("start chrome");
        }
        else if(strcmp(user_input,"open notepad")==0)
        {
            printf("ok sir , opening notpad editor \n");
            system("start notepad");
        }
        else if(strcmp(user_input,"open cmd")==0)
        {
            printf("ok sir , opening cmd terminal \n");
            system("start cmd");
        }
        else if(strcmp(user_input,"time")==0)
        {
            time_t s, val =1 ;
            struct tm* current_time;
            s = time(NULL);
            current_time = localtime(&s);
            printf("bot ==> %02d:%02d:%02d\n",current_time->tm_hour,current_time->tm_min,current_time->tm_sec);
        }
        else if(strcmp(user_input,"open youtube")==0)
        {
            printf("ok sir , opening youtube \n");   
            system("start http://youtube.com");   
        }
        else if(strcmp(user_input,"open chatgpt")==0)
        {
            printf("ok sir , opening chatgpt \n");   
            system("start https://chat.openai.com/");   
        }
        else if(strcmp(user_input,"open bard")==0)
        {
            printf("ok sir , opening bard \n");   
            system("start https://bard.google.com/");   
        }
    }
    return 0;
}