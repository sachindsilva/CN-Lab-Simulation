import java.io.*;
import java.net.*;

class udpclient{
    public static void main(String[] args)throws Exception{
        DatagramSocket cs=new DatagramSocket();

        BufferedReader inputstream=new BufferedReader(new InputStreamReader(System.in));

        InetAddress IPAddress=InetAddress.getByName("localhost");
        byte[] receiveData=new byte[1024];

        byte[] sendData=new byte[1024];
        System.out.println("Enter your message here :(TYPE END to stop) :");

        while(true){
            String message=inputstream.readLine();

            if(message.equals("END"))
            {
                cs.close();
                System.exit(0);
            }
            else 
            {
                sendData=message.getBytes();

                DatagramPacket sendPacket=new DatagramPacket(sendData,sendData.length,IPAddress,7999);

                cs.send(sendPacket);

                DatagramPacket receivePacket=new DatagramPacket(receiveData,receiveData.length);

                cs.receive(receivePacket);

                String modifiedmsg=new String(receivePacket.getData());

                System.out.println("From server : "+modifiedmsg);
            }
        }


    }   
}