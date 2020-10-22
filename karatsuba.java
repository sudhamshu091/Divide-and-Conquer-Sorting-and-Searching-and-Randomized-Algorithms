public class karatsuba {
  public static void main(String args[]) {
    System.out.println(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627));
  }

  public static int karatsuba(int X, int Y) {
    String x = Integer.toString(X);
    String y = Integer.toString(Y);
    int result = 0;


    for (int i = 0; i < y.length(); i++) {
      int carry = 0;
      String temp = "";


      for (int j = x.length() - 1; j >= 0; j--) {
        int num = Character.getNumericValue(y.charAt(i)) * Character.getNumericValue(x.charAt(j)) + carry;
        if (num > 9 && j > 0) {
          temp = Integer.toString(num % 10) + temp;
          carry = num / 10;
        }
        else {
          temp = Integer.toString(num) + temp;
          carry = 0;
        }
      }
      result *= 10;

      result += Integer.parseInt(temp);
    }
    return result;
  }
}
