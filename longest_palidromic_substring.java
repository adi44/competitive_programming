//longest palindromic substring.
public class longest_palidromic_substring
{
	static int start = 0;
	static int maxLen = -1;

	static public String LongestPalindrome(String s)
	{
		if(s.length()<2)
			return s;
		for(int i=0;i<s.length(); i++)
		{
			findP(s,i,i);
			//to check all odd palidromic substrings
			findP(s,i,i+1);
			//to check all even palindromic substrngs.

		}
		return s.substring(start, start+maxLen);

	}
	static public void findP(String s, int j, int k)
	{
		while((j>=0)&&(k<=s.length()-1)&&(s.charAt(j)==s.charAt(k))){
			j--;
			k++;
		}
		int len= k-j-1;
		if(len>maxLen)
		{
			maxLen=Math.max(maxLen,len);
			start=j+1;//start value would be increment of lower value
		}
	}
	public static void main(String[] args)
	{
		System.out.println(LongestPalindrome("bbcde"));
	}
}
/*Alogrithm 
here, if you want to find a palindromic string we will use a techniqye called expanding from center. in this technique we will expend the palindrome from center and try to look if it matches. and we will find a length. if it
does not matches, we will find the length and check it if it is maximum from the mac length if it is maximum from the max length, then it will be assigned to max length. 