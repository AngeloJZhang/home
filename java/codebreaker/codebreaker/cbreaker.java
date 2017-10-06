package codebreaker;
import java.io.*;
import java.util.Random;

public class cbreaker {
	
	public static void main(String args[]) throws IOException {
		BufferedReader readline = new BufferedReader(new InputStreamReader(System.in)); 
		int[] inputNums, count, gameNums = null;
		while(true) {
			System.out.println("\n\n\n\n\n\n\n\n\nWelcome to Code Breaker!");
			System.out.println("\nThis is a four digit code breaker game.\nThe objective is to find the correct 4 digits within the turn limit!\nGood luck!");
			gameNums = genNum();
			System.out.println(readNum(gameNums));
			for(int i =0; i<8; i++) {
				inputNums = takeNums();
				count = compareNum(gameNums,inputNums);
				if (count[0] != 4) {
					System.out.println("You have " + count[0] + " number/s in the correct position.");
					System.out.println("You have " + count[1] + " number/s in an incorrect position.");
					System.out.println("You have " + (7-i) + " turn/s left.\n");
				}
				else {
					System.out.println("Congratulations! You Win!");
					break;
				}
			}
			System.out.println("The number was : " + readNum(gameNums) );
			gameNums = null;
			System.out.print("Press enter to play again : ");
			readline.readLine();
		
			
		}
	}
	public static String readNum(int[] genNums) {
		//reads out an array of ints
		String holder = "";
		for (int i = 0; i < genNums.length ; i++) {
			holder = holder + genNums[i];
		}
		return holder;
	}
	public static int[] genNum() {
		//generate random numbers
		Random genRan = new Random();
		int[] genNums = new int[4];
		System.out.println("\nGenerating Nums...");
		for (int i =0 ; i < 4; i++) {
			genNums[i] = genRan.nextInt(10);
			//System.out.println(genNums[i]);
		}
		System.out.println("Generation Finished.\n");
		return genNums;
	}
	public static int[] takeNums() throws IOException{
		//take nums and check for valid
		String holder = "";
		boolean valid = false;
		while(!valid) {
		System.out.print("\nEnter your 4-digit guess # : ");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		holder = br.readLine();
		if (holder.length() == 4) {
			try {
				Integer.parseInt(holder);
				valid = true;
			}
			catch (IllegalArgumentException e){
				System.out.println("\nPlease enter a valid 4-digit number.");
			}
		}
		else {
			System.out.println("\nPlease enter a 4-digit number.");
			}
		}
		//System.out.println(holder);
		return string2Array(holder);
	}
	
	public static int[] string2Array(String digits) {
		//go string to int array;
		int[] input = new int[digits.length()];
		for (int i = 0 ; i < digits.length() ; i++) {
			input[i] = (int) digits.charAt(i) - 48;
			//System.out.println(input[i]);
		}
		return input;
	}
	public static int[] compareNum(int array1[], int array2[]) {
		//get the matches and placement numbers index 0 place match index 1 = incorrect place match
		int[][] count = new int[2][4];
		int[] values = new int[2];
		count[0] = new int[4];
		count[1] = new int[4];
		int holder = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if ((i == j) && (array1[j] == array2[i])){
					count[0][j] = 1;
					holder++;
				}
				else if( array1[j] == array2[i]) {
					count[1][j] = 1;
					holder++;
				}	
				count[1][j] = count[1][j] ^ count[0][j];
			}
		}
		if (holder >= 1) {
			System.out.println("There are duplicate number/s");
		}
		values[0]= arraySum(count[0]);
		values[1]= arraySum(count[1]);
		count = null;
		return values;
	}
	public static int arraySum(int[] holder) {
		int sum = 0;
		for(int i = 0; i < holder.length; i++) {
			sum += holder[i];
		}
		return sum;
	}
}
