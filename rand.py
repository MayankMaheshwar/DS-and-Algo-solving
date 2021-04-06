public class LinkedList {
	
	int n;
	LinkedList next; 
	
	public LinkedList()
	{
		n=0;
		next=null;
		
	}
	
	public void add(int n)
	{
		this.n=n;
	}
	............
	
	public static void main(String []aa)
	{
		LinkedList first=null,temp=null;  /**Line A**/
		Scanner sc=new Scanner(System.in);
		for(int i=0;i<5;i++)
		{
			LinkedList li=new LinkedList();
			int n=sc.nextInt();
			if(first==null)
			{
			li.add(n);  /**Line B**/
			temp=li;
			first=temp;
			}
			else{
				temp.next=li;
				temp=li;   /**Line C**/
}