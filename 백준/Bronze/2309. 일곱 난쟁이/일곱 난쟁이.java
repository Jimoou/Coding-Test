import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {	

	static int solution(ArrayList<Integer> heights, int n1, int n2) {
	    int ret = 0;
	    for (int i = 0; i < heights.size(); i++)
	    {
	        if (i == n1 || i == n2)
	            continue;
	        ret += heights.get(i);
	    }
	    return ret;

	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> heights = new ArrayList<Integer>();
		
		for (int i = 0; i < 9; i++) {
			heights.add(sc.nextInt());
		}

	    int n1 = 0, n2 = 0;
	    for (int i = 0; i < 9; i++)
	    {
	        for (int j = i + 1; j < 9; j++)
	        {
	            if (100 == solution(heights, i, j))
	            {
	                n1 = i;
	                n2 = j;
	            }
	        }
	    }
	    

	    heights.remove(n2);
	    heights.remove(n1);

	    

	    Collections.sort(heights);
	    for (int i = 0; i < heights.size(); i++)
	    {
	    	System.out.println(heights.get(i));
	    }
	}
}