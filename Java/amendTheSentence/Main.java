import java.util.Scanner;

/**
* The Main program (amendTheSentence) implements an application that
* anwsers the codeSignal problem requiring the user to parse a given
* string with CapitalLettersForNewWords. The output for this example 
* should be "capital letters for new words". 
* 
* Soln relies on Java's string and character functions, especially 
* appending strings. Some tricky type conversion too on lines 54-55
*  between character and String types for the desired methods.
*
* @author  Abigail Brannan, 
* @version 1.0
* @since   2019-12-11 
*/
public class Main {

    /**
   * This is the main method which takes in the input and call amendTheSentence(input)
   * @param args Unused.
   * @return Nothing.
   */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String output = "";
		
		while(scanner.hasNextLine()) {
			String line = scanner.nextLine();

            output = amendTheSentence(line);
            System.out.println(output);
        }
    }

   /**
   * This method amends the sentence by parsing the output. 
   * @param String input Line to be parsed.
   * @return String output Sentence with words seperated by spaces and lowercase.
   */
    public static String amendTheSentence(String input) {
        String output = "";
        
        // if input is empty string, return empty string
        if (input == "")
            output = input;
        else {
            // make first letter lowercase and declare to output
            output = input.substring(0, 1).toLowerCase();

            for (int i = 1; i < input.length(); i++) {
                // if upperCase, add " " and lowerCase version of char to output
                if (Character.isUpperCase(input.charAt(i))) {
                    String temp = String.valueOf(input.charAt(i));
                    output = output + " " + temp.toLowerCase();
                } // if not upperCase, just add char to output
                else
                    output = output + input.charAt(i);
            }
        }

        return output;
    }
}