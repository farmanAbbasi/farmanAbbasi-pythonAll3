import java.util.ArrayList;
import java.util.List;

public class Main {
    
public static void printPermutations(String prefix, String str) {
  if (str.length() == 0) {
      //this prefix is one ans.
    System.out.println(prefix);
  } else {
    for (int i = 0; i < str.length(); i++) {
        //everytime a new newStr and newPrefic is created using whatever is passed
      String newStr = str.substring(0, i) + str.substring(i + 1);
      String newPrefix = prefix + str.charAt(i);
      printPermutations(newPrefix, newStr);
    }
  }
}

public static void main(String[] args) {
  // A sample string
  String s = "abc";
  printPermutations("", s);
}
}

