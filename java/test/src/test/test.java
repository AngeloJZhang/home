package test;
import java.lang.String;

public class test {
	public static void main( String args[]) {
	/*	int x,y,z;
		x =  2;
		y = x++;
		x = 2;
		z = ++x;
		System.out.println("x = " + x);
		System.out.println("y = " + y);
		System.out.println("z = " + z);
		x=2;
		System.out.println(squared(x++));
		x=2;
		System.out.println(squared(++x));
	*/
	/*	String holder = "1234";
		byte[] bholder;
		bholder = holder.getBytes();
		for(int i = 0; i < 4 ; i++) {
			System.out.println(bholder[i]);
		}
	*/
		String holder = "12k4";
		String test = "test";
		System.out.println(test);
		if (holder.length() == 4) {
			try {
				Integer.parseInt(holder);
				test = "hello";
			}
			catch (IllegalArgumentException e){
				System.out.println("wrong");
			}
		}
		System.out.print(test);
		
	}
	public static int squared(int holder) {
		return holder* holder;
	}
}
