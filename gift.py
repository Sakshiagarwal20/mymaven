interface Candy {
	public static String tasteOfCandy = "Sweet";
	public String typeOfMilk = "Skimmed";
	
}


class Candies implements Candy {
	public long priceOfCandy = 0;
	public long quantity=0;
	public String nameOfCandy = "";
	public String typeOfCandy = "";
	public   static long netWeightCandies;
	
	public Candies()
	{
		
	}
	public Candies(String nameOfCandy,String typeOfCandy,long priceOfCandy, long quantity ) {
		super();
		this.nameOfCandy=nameOfCandy;
		System.out.println("name of Candy is: " + this.nameOfCandy);
		this.typeOfCandy=typeOfCandy;
                System.out.println("type of Candy is: " + this.typeOfCandy);
		this.priceOfCandy = priceOfCandy;
		System.out.println("Price of a Candy is: " + this.priceOfCandy);
		
		this.quantity=quantity;
		System.out.println("quantity of the Candy is: " + this.quantity);
		netWeightCandies+=quantity;
	}


	public long getPrice()
	{
      return priceOfCandy; 

	}
	
	public static long weightOfCand() {
		
		
		 return  netWeightCandies;
		}
	public String toString()
	{
		return "Candyname="+ this.nameOfCandy+" "+"Price=" +this.priceOfCandy;
	}
static void weight(){
System.out.println("net weight="+ netWeightCandies);
}

}
	



public class NewYearGift {

public NewYearGift() {
		
	}

	public static void main(String[] args) {
		
	ArrayList<Candies> arrayList=new ArrayList<Candies>();
	Candies candyobj1=new Candies();
		

		arrayList.add(new  Candies("Dairymilk","Milk",80,50));
		arrayList.add(new  Candies("Temptations","Darkchoclate",75,40));
		arrayList.add(new  Candies("5Star","Creamy", 30,50));
		arrayList.add(new  Candies("Snickers","Nuts",40,50));

		Comparator<Candies> CandyCom=new Comparator<Candies>()
		{
			public int compare(Candies can1,Candies can2)	{	
			if(can1.getPrice()>can2.getPrice())
			
				 return 1;
				 else
				 return -1;
			}
			
		};

		Collections.sort(arrayList,CandyCom);
		for(Candies candyItem:arrayList)
		{

			System.out.println(candyItem);
		}


		System.out.println("Weight of the total Candies in Gift is:"+weightOfCand());
        

		
		
		
		//Create lot of Instances for Candies here to access all
	
}
}
