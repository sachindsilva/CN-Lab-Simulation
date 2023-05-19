#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void receiver(int *frame,int l2)
{
  int i,j,counter,l3;
  int msg[100];
  l3=l2-8;
  j=0;
  for(i=8;i<l3;i++)
  {
    if(frame[i]==0)
    {
      if(counter==5)
      {
        msg[j]=frame[i];
        j++;
        counter=0;
      }
      else
      {
        msg[j]=frame[i];
        j++;
        counter++;
      }
    }
    else
    {
      msg[j]=frame[i];
      j++;
      counter++;
    }
  }
  printf("Received Messages are\n");
  for(i=0;i<j;i++)
    printf("%d",msg[i]);
  printf("\n");
}


void sender()
{
  int data[100],frame[100],framelen,i,j=8,n;
  int count,zeroadded=0,zero;

  printf("Enter the number of bits\n");
  scanf("%d",&n);
  printf("Enter the data for bits\n");
  for(i=0;i<n;i++)
    scanf("%d",&data[i]);
  frame[0]=1;
  frame[1]=0;
  frame[2]=0;
  frame[3]=0;
  frame[4]=0;
  frame[5]=0;
  frame[6]=0;
  frame[7]=1;


  for(i=0;i<n;i++)
  {
    if(data[i]==0)
    {
      frame[j]=data[i];
      j++;
      zero=1;
      count=0;
    }
    else
    {
      if(count==5 && zero==1)
      {
        frame[j]=0;
        j++;
        zeroadded++;
        frame[j]=data[i];
        j++;
        count=0;
      }
      else
      {
        frame[j]=data[i];
        j++;
        count++;
      }
    }
  }

  frame[j++]=0;
  frame[j++]=1;
  frame[j++]=1;
  frame[j++]=1;
  frame[j++]=1;
  frame[j++]=1;
  frame[j++]=1;
  frame[j++]=0;

  framelen=n+16+zeroadded;

  printf("Length of frame sent : ",framelen);
  printf("frame sent are\n");
  for(i=0;i<framelen;i++)
    printf("%d",frame[i]);
  printf("\n");
  receiver(frame,framelen);



}


void main()
{
  sender();
}
