import java.util.Scanner;

public class CompoundInterest1 {
	private static Scanner sc;
	public static void main(String[] args) 
	{
		double PAmount, ROI, TimePeriod;
		sc = new Scanner(System.in);
		
		System.out.print(" Please Enter the Principal Amount : ");
		PAmount = sc.nextDouble();
		
		System.out.print(" Please Enter the Rate Of Interest : ");
		ROI = sc.nextDouble();
		
		System.out.print(" Please Enter the Time Period in Years : ");
		TimePeriod = sc.nextDouble();
		
		calCompoundInterest(PAmount, ROI, TimePeriod);
		
	}
	
	public static void calCompoundInterest(double PAmount, double ROI, double TimePeriod)
	{
		double FutureCI, CI;
		FutureCI = PAmount * (Math.pow(( 1 + ROI/100), TimePeriod));
		CI = FutureCI - PAmount;
		
		System.out.println("\n The Future Compound Interest for Principal Amount " + PAmount + " is = " + FutureCI);
		System.out.println(" The Compound Interest for Principal Amount " + PAmount + " is = " + CI);
	}

}

