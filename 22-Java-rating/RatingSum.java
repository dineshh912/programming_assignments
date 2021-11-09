import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;

public class RatingSum{
    public static void main(String args[]) throws FileNotFoundException{
        File inputFile = new File("input.txt"); // Intialize and open input.txt file
        Scanner sc = new Scanner(inputFile); // Scanner object helps to read from input file
        int n = sc.nextInt(); // Reading integer
        ArrayList<Integer> rating = new ArrayList<Integer>(n); // Store rating 
        ArrayList<Integer> value = new ArrayList<Integer>(n); // Store rating 

        for(int i=0; i<n; i++){
            rating.add(sc.nextInt()); // Read from input.txt and add into rating array
            value.add(1); // each value in the array list as 1
        }

        sc.close(); // Exiting scanner object after complet reading

        for(int i=0; i<n; i++){
            for(int j=i; j>=0; j--){
                if(j-1 > 0){ // Check index is greater than 0
                    if(rating.get(j) > rating.get(j-1)) // compare j and j-1 rating
                        value.set(j, Math.max(value.get(j), value.get(j-1)+1)); //check value of j and j-1
                }
                if(j+1 < n){ //  check next index is valid value
                    if(rating.get(j) > rating.get(j+1)) // compare j and j+1 rating
                    value.set(j, Math.max(value.get(j), value.get(j+1)+1)); //check value of j and j+1
                }
            }
        }
        int sumValue = 0; // store final sum value
        for(int i=0; i<n; i++){ // loop through value array List
            sumValue+= value.get(i); // Add all the values and store it in variable
        }

        System.out.println("Result value sum : "+ sumValue); //Print output
    }
}