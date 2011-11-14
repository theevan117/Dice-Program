//
//     Evan W. Muller
//     theevan117@gmail.com
//
//


// import of scanner
import java.util.Scanner;

import java.util.HashMap;

import java.util.Random;

import java.util.ArrayList;

public class DiceProgram
{
	
	public static void main (String args[]) 
	{
			
		// Declaration of Scanner
		Scanner input = new Scanner(System.in);
		
		// Declaration of Random
		Random r = new Random();
		
		// Creation of Dice_History HashMap
		HashMap<Integer, ArrayList> diceHistory = new HashMap<Integer, ArrayList>();

		while(true){
		
			System.out.print("Which dice would you like to roll? ");
			 
			int diceChoice = input.nextInt();
			
			System.out.println("You chose d" + diceChoice);
			
			if(diceChoice <= 0){
				System.out.print("Invalid dice choice, goodbye!");
				break;
			}
			
			int diceValue = 1 + r.nextInt(diceChoice);
			
			System.out.println(diceValue);
			
			if(diceHistory.containsKey(diceChoice) == false){
				diceHistory.put(diceChoice, new ArrayList());
			}
			
			diceHistory.get(diceChoice).add(diceValue);
			
		}

	}
}

