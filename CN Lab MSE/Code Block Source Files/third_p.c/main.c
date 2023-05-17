#include<stdio.h>

struct node
{

    int dist[20];
    int from[20];

}rt[20];

int main()
{

    int dmat[20][20];
    int i,j,k,n,count=1;
    printf("Enter the number of nodes\n");
    scanf("%d",&n);
    printf("Enter the cost matrix\n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        {
            scanf("%d",&dmat[i][j]);
            dmat[i][i]=0;
            rt[i].dist[j]=dmat[i][j];
            rt[i].from[j]=j;
        }

        do
        {
            for(i=1;i<=n;i++)
                for(j=1;j<=n;j++)
                    for(k=1;k<=n;k++)
                        if(rt[i].dist[j]>dmat[i][k]+rt[k].dist[j])
                        {
                            rt[i].dist[j]=rt[i].dist[k]+rt[k].dist[j];
                            rt[i].from[j]=k;
                        }
                        count++;

        }while(count<n);

        for(i=1;i<=n;i++)
        {
            printf("\nDistance table for router %c is \n",i+64);
            for(j=1;j<=n;j++)
                printf("\t Node %d via %d, Distance : %d\n",j,rt[i].from[j],rt[i].dist[j]);
        }
        return 0;
}
