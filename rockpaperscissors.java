//rock paper scissor game
import java.io.*;
import java.util.*;
class rockpaperscissors
{
    public static void main(String [] args)
    {
        Scanner sc=new Scanner(System.in);
        int score=0,score1=0;
        int pts;
        System.out.println("enter points to play");
        pts=sc.nextInt();
        System.out.println("Rock:r  Paper:p  Scissor:s");
        char ar[]={'r','p','s'};
        while(score!=pts && score1!=pts)
        {
            char c=sc.next().charAt(0);
            if(c!='r' && c!='s' && c!='p')
            {
                System.out.println("wrong input exiting");
                System.exit(0);
            }
            int guess=(int)(Math.random()*((3-1)+1)+1);
            char g=ar[guess-1];
            System.out.println("player:"+c+" computer:"+g);
            if(c==g)
            {
                System.out.println("Player score:"+score+" computer score:"+score1);
                continue;
            }
            if(c=='r' && g=='p')
            score1++;
            if(g=='r' && c=='p')
            score++;
            if(c=='p' && g=='s')
            score1++;
            if(g=='p' && c=='s')
            score++;
            if(c=='r' && g=='s')
            score++;
            if(g=='r' && c=='s')
            score1++;
            System.out.println("Player score:"+score+" computer score:"+score1);
        }
        if(score==pts)
        System.out.println("Player winner!!");
        else if(score1==pts)
        System.out.println("Computer winner!!");
    }
}