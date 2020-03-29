import java.util.*;
class Test{
    public static void main(String[] args){
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter name");
        String name = myObj.nextLine();
        System.out.println("enter age");
        int age = myObj.nextInt();
        if(age<18){
            System.out.print("You need to be older than 18 to watch");
        }else{
            System.out.println("Welcome, "+name + "you're " + age );
        }
    }
}
