#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char res[100];

void sender()
{
    int i,n,len;
    int frame[100],l[100];

    printf("Enter the number of frames :");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("Enter the frame %d : ",i+1);
        scanf("%s",&frame);

        len=strlen(frame);
        printf("The Length of frame %d sent = %d\n",i+1,len);

        sprintf(l,"%d",len);
        strcat(l,frame);
        strcat(res,l);
    }
}

void receiver()
{
    int i,j,len;    

    printf("Received frames are\n");
    for(i=0;i<strlen(res);i++)
    {
        len=res[i]-'0';
        for(j=i+1;j<=(i+len);j++)
            printf("%c",res[j]); i=i+len;
        printf("\t");
    }
}

void main()
{
    sender();
    receiver();
}