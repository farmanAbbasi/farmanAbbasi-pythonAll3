class Node{
    int data;
    Node next;
    Node(int data){
        this.data=data;
        this.next=null;
    }
    
public static Node insertNode(Node start, int data){
    if(start==null){
        start= new Node(data);
        return start;
    }
    Node curr = start;
    while(curr.next!=null){
        curr=curr.next;
    }
    curr.next=new Node(data);
    return start;
} 
public static Node insertAtAnyPosition(Node start, int data, int position){
    
    if(position==1){
        start=insertNodeAtBeginning(start,data);
        return start;
    }
    Node neww=new Node(data);
    Node curr=start;
    int counter=0;
    while(curr.next!=null){
        counter+=1;
         if(counter==position-1){
            break;
        }
        curr=curr.next;
        
       
    }
    Node temp=curr.next;
    curr.next=neww;
    neww.next=temp;
    return start;

}
public static Node insertNodeAtBeginning(Node start, int data){
    Node curr;
    curr =new Node(data);
    curr.next=start;
    start=curr;
    return start;
}
public static Node deleteNodeAtEnd(Node start){
    if(start==null){
        System.out.println("Nothing to delete");
       
    }
    Node curr=start;
    Node parent=start;
    int counter=0;
    while(curr.next!=null){
        parent=curr;
        curr=curr.next;
        counter+=1;
    }
    parent.next=null;
    if(counter==0){
        start=null;//means ek hi bacha tha toh ab sab khatam
    }
    return start;
    
    
}
public static Node deleteNodeAtBeginning(Node start){
    if(start==null){
        System.out.println("Nothing to delete");
    }
    start=start.next;
    return start;
    
}
public static Node deleteNodeAtAnyPosition(Node start,int position){
     if(position==1){
        start=deleteNodeAtBeginning(start);
        return start;
     }
     
     Node curr=start;
     Node parent=start;
     int counter=0;
     while(curr.next!=null){
        counter+=1;
        parent=curr;
        curr=curr.next;
        if(counter==position-1){
            break;
        }
         
     }
     parent.next=curr.next;
     if(counter==0){
         start=parent;//this thing is done, agar ek hi elemnt tha toh ab satrt bhi wahi ho jo parent hai
     }
     return start;
     
    
     
}
public static void printHelper(Node start){
    if(start==null){
        System.out.println("Nothing to print");
    }
    while(start!=null){
        System.out.print(start.data+" ");
        start=start.next;
    }
    System.out.println();
    
}
    
}

public class LinkedList
{
	public static void main(String[] args) {
		Node start=null;
		start=Node.insertNode(start,1);
		start=Node.insertNode(start,2);
		start=Node.insertNode(start,3);
		start=Node.insertNode(start,4);
		start=Node.insertNodeAtBeginning(start,5);
		start=Node.insertNodeAtBeginning(start,6);
		start=Node.insertNode(start,7);
		start=Node.insertAtAnyPosition(start,3000,7);
		Node.printHelper(start);//6 5 1 2 3 4 3000 7 
		
		start=Node.deleteNodeAtEnd(start);
		Node.printHelper(start);//6 5 1 2 3 4 3000

		start=Node.deleteNodeAtBeginning(start);
		Node.printHelper(start);//5 1 2 3 4 3000
		
		start=Node.deleteNodeAtAnyPosition(start,5);
		Node.printHelper(start);//5 1 2 3 3000
		
	}
}
