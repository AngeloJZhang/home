package codebreaker;
import java.util.Random;

public class cbreaker {
	
	public static void main(String args[]) {
	/*	gameNum = genNum();
		int[] count = compareNum(gameNum,inputNum);
		System.out.println("Place = " + count[0]);
		System.out.println("Match = " + count[1]);
	*/
	}
	public static int[] genNum() {
		Random genRan = new Random();
		int[] genNums = new int[4];
		for (int i =0 ; i < 4; i++) {
			genNums[i] = genRan.nextInt(10);
			System.out.println(genNums[i]);
		}
		return genNums;
	}
	/*public static int[] takeNums() {
		int[] input = new int[4];

	}*/
	public static int[] compareNum(int array1[], int array2[]) {
		int[] count = new int[2];
		count[0] = 0;
		count[1] = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if ((i == j)&(array1[i] == array2[j])){
					count[0]++ ;
				}
				else if( array1[i] == array2[j]) {
					count[1]++;
				}
			}
		}
		return count;
	}
	
	static int[] gameNum = null;
	static int[] inputNum = new int[] {2,4,6,8};
	int count = 0;

	
}
