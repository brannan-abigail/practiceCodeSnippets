import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String output = "";
		
		while(scanner.hasNextLine()) {
			String line = scanner.nextLine();
        
            if (isNumeric(line))
                output = testCases(Integer.parseInt(line));
            System.out.println(output);
        }
    }

    public static String amendTheSentence(String input) {
        String output = "codesignam is awesome";
        return output;
    }

    public static String testCases(int testCase) {
        String output = "";

        switch (testCase) {
            case 1:
                System.out.println("Hit test Case 1");
                output = amendTheSentence("CodesignamIsAwesome");
                break;
        }

        return output;
    }

    public static boolean isNumeric(final String str) {
        // null or empty
        if (str == null || str.length() == 0) {
            return false;
        }
        return str.chars().allMatch(Character::isDigit);
    }
}