import java.util.*;

class crc{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter the generator :");
        String gen=sc.nextLine();

        System.out.println("Enter the data :");
        String data=sc.nextLine();

        String code=data;

        while(code.length()<(data.length()+gen.length()-1))
            code=code+'0';
        code=data+div(code,gen);

        System.out.println("Transmitted code word is "+code);
        System.out.println("Please Enter the received code word :");

        String rec=sc.nextLine();

        if(Integer.parseInt(div(rec,gen))==0)
            System.out.println("Received code word contains no errors...");
        else 
            System.out.println("Received code word contains ERRORS!!");


    }

    static String div(String num1,String num2){
        int n=num2.length();

        String result=num1.substring(0,n);
        String rem="";

        for(int i=0;i<num2.length();i++)
        {
            if(result.charAt(i)==num2.charAt(i))
                rem+='0';
            else 
                rem+='1';
        }

        while(n<num1.length()){
            if(rem.charAt(0)=='0'){
                rem=rem.substring(1,rem.length());
                rem=rem+String.valueOf(num1.charAt(n));
                n++;
            }

            result=rem;
            rem="";

            for(int i=0;i<num2.length();i++)
            {
                if(result.charAt(i)==num2.charAt(i))
                    rem+='0';
                else
                    rem+='1';
            }

        }
        return rem.substring(1,rem.length());
    }

}