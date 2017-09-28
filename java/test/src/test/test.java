package test;

public class test {
	public static void main( String args[]) {
		int x,y,z;
		x =  2;
		y = x++;
		x = 2;
		z = ++x;
		System.out.println("x = " + x);
		System.out.println("y = " + y);
		System.out.println("z = " + z);
		System.out.println(squared(x++));
		System.out.println(squared(++x));
	}
	public static int squared(int holder) {
		return holder* holder;
	}
}
