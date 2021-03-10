// https://www.techiedelight.com/deletion-from-bst/
import java.util.*;
 class Node{
        int data;
        Node left;
        Node right;
        Node(int data){
            this.data=data;
            this.left=null;
            this.right=null;
            
        }
    }

public class BinarySearchTree{
    // Recursive function to insert a key into BST
	public static Node insertionInBSTRecursive(Node root, int key)
	{
		// if the root is null, create a new node and return it
		if (root == null) {
			return new Node(key);
		}
		// if given key is less than the root node, recur for left subtree
		if (key < root.data) {
			root.left = insertionInBSTRecursive(root.left, key);
		}
		// if given key is more than the root node, recur for right subtree
		else {
			root.right = insertionInBSTRecursive(root.right, key);
		}
		return root;
	}


    public static Node insertionInBST(Node root, int key){
        Node curr=root;
        Node  parent=null;
        //for empty root
        if(root==null){
            return new Node(key);
        }
        
        ////for getting the parent
        while(curr!=null){
            parent=curr;
            if(key<curr.data){
                curr=curr.left;
            }
            else{
                curr=curr.right;
            }
        }

        //for only one root element or when got the parent with 2 null childs both are this same case only
        if(key<parent.data){
            parent.left=new Node(key);
        }
        else{
            parent.right=new Node(key);
        }
        
        return root;
    }

    public static void treeTraversal(Node root){
        if(root==null) {return;}

        treeTraversal(root.left);
        System.out.print(root.data+" ");
        treeTraversal(root.right);
        
    }
	

public static void levelOrderTraversal(Node root){
    if(root== null){
        return ;
    }
    
    List<Node> q=new ArrayList<>();
    q.add(root);
    //int count=0; //note lines commented can also be used for the same result
    while(!q.isEmpty()){
        //count=q.size();
        //while(count>0){
        Node item=q.remove(0);
        System.out.print(item.data+" ");
        if(item.left!=null){
            q.add(item.left);
        }
        if(item.right!=null){
             q.add(item.right);
        }
        //count--;
        //}
        
    }
    System.out.println();
    
}

public static void leftViewOfTree(Node root){
    if (root == null){
        return; 
    }
    Queue<Node> q=new LinkedList<>();
    q.add(root);
    int count=0;
    int queueCount=0;
    while(!q.isEmpty()){
        count=q.size();
        queueCount=q.size();
        while(count>0){
            Node item=q.remove();
            if(count==queueCount){
                //as on first level both 1 , on second level when both 2 then only print
                // as we want first elemnt only to be printed on each level 
            System.out.print(item.data+" ");
            }
            if(item.left!=null){
                q.add(item.left);
            }
            if(item.right!=null){
                q.add(item.right);
            }
            count--;
        }
    }
       System.out.println();
}
// from queue import Queue
// def leftView(root):
//     if root is None:
//         return None
//     q=Queue()
//     q.put(root)
//     count=0
//     while !q.empty():
//         count=q.qsize()
//         countStart=q.qsize()
//         while count>0:
//             temp=q.get()
//             if count==countStart:
//                 print(temp.val)
//             if temp.left:
//                 q.put(temp.left)
//             if temp.right:
//                 q.put(temp.right)
//             count-=1    
                

public static void rightViewOfTree(Node root){
    if (root == null){
        return; 
    }
    Queue<Node> q=new LinkedList<>();
    q.add(root);
    int count=0;
    int queueCount=0;
    while(!q.isEmpty()){
        count=q.size();
        queueCount=q.size();
        while(count>0){
            Node item=q.remove();
            if(count==1){
            System.out.print(item.data+" ");
            }
            if(item.left!=null){
                q.add(item.left);
            }
            if(item.right!=null){
                q.add(item.right);
            }
            count--;
        }
    }
       System.out.println();
}

public static void mirrorTree(Node root){
    //just similar to Post order traversal except for printing we are swapping;
    if(root==null){
        return ;
    }
    mirrorTree(root.left);
    mirrorTree(root.right);
    Node temp=root.left;
    root.left=root.right;
    root.right=temp;
}


    public static int searchInBST(Node root, int key){
        if(root==null) return -1;
        
        
        if(key<root.data){
            return searchInBST(root.left,key);
        }
        if(key>root.data){
            return searchInBST(root.right,key);
        }
        //it means root.data will be equal to key
        return root.data;

    }

    public static void searchInBSTGivingParent(Node root, int key,Node parent){
        
        try{
                if(root==null && parent==null) {System.out.println("Empty BST");}
                if(root==null && parent!=null) {System.out.println("Not Found");}
                if(root.data==key && parent==null){System.out.println("Found at root with No parent");}
                if(root.data==key && parent!=null ){
                    System.out.println("Found with parent "+parent.data);
                }
            
            if(key<root.data){
                searchInBSTGivingParent(root.left,key,root);
            }
            if(key>root.data){
                searchInBSTGivingParent(root.right,key,root);

            }
        }
        catch(Exception e){
            System.out.println(e);

        }
    }

    public static int minimumAtRightSubTree(Node root){
        Node curr=root;
        while(curr.left != null){
            curr=curr.left;
        }
        return curr.data;
    }
    //note: Node root is the left root sent from where it is called
    public static Node maximumAtLeftSubTree(Node root){
        Node curr=root;
        while(curr.right!=null){
            curr=curr.right;
        }
        return curr;

    }

 
    // Function to delete node from a BST
	public static Node deleteNode(Node root, int key)
	{
		// base case: key not found in tree
		if (root == null) {
			return root;
		}

		// if given key is less than the root node, recur for left subtree
		if (key < root.data) {
			root.left = deleteNode(root.left, key);
		}
		
		// if given key is more than the root node, recur for right subtree
		else if (key > root.data) {
			root.right = deleteNode(root.right, key);
		}

		// key found
		else
		{
			// Case 1: node to be deleted has no children (it is a leaf node)
			if (root.left == null && root.right == null)
			{
				// update root to null
				return null;
			}

			// Case 2: node to be deleted has two children
			else if (root.left != null && root.right != null)
			{
				// find its in-order predecessor node
				Node predecessor = maximumAtLeftSubTree(root.left);

				// Copy the value of predecessor to current node
				root.data = predecessor.data;

				// recursively delete the predecessor. Note that the
				// predecessor will have at-most one child (left child)
				root.left = deleteNode(root.left, predecessor.data);
			}

			// Case 3: node to be deleted has only one child
			else
			{
				// find child node
				Node child = (root.left != null)? root.left: root.right;
				root = child;
			}
		}

		return root;
	}
    public static int sumAtDeepestLevel(Node root){
        Queue<Node> q=new LinkedList<>();
        q.add(root);
        int sumAtDeepestLevel=0;
        int count=0;
        while(!q.isEmpty()){
            count=q.size();
            sumAtDeepestLevel=0;
            while(count>0){
                Node x= q.remove();
                System.out.print(x.data+" ");   
                sumAtDeepestLevel+=x.data;
                if(x.left!=null){
                    q.add(x.left);
                }
                if(x.right!=null){
                    q.add(x.right);
                }
                count-=1;
            }
            System.out.println();
        }
        return sumAtDeepestLevel;
    }

   //note: print in order root, left and right
    public static void preOrderTraversalIterative(Node root){
        Stack<Node> s=new Stack<>();
        s.push(root);
        Node temp;
        while(!s.isEmpty()){
            temp=s.pop();
            System.out.print(temp.data+" ");
            //note pehle right push hua hai as pehle left print karna hai
             if(temp.right!=null){
                s.push(temp.right);  
            }
            if(temp.left!=null){
                s.push(temp.left);
            }
        }
        System.out.println();
    }
 // in t , jayega in order root, left , right bhale hi hai post i.e left, right ,root
      public static void postOrderTraversalIterative(Node root){
        Stack<Node> s=new Stack<>();
        Stack<Node> t=new Stack<>();
        s.push(root);
        Node temp;
        while(!s.isEmpty()){
             temp=s.pop();
             t.push(temp);
             if(temp.left!=null){
                s.push(temp.left);
            }
             if(temp.right!=null){
                s.push(temp.right);  
            }
        }
        while(!t.isEmpty()){
            temp=t.pop();
            System.out.print(temp.data+" ");
        }
        System.out.println();
    }

    public static void inOrderTraversalIterative(Node root){
        Stack<Node> s=new Stack<>();
        Node temp=root;
        while(!s.isEmpty() || temp!=null){
             if(temp!=null){
                s.push(temp);
                temp=temp.left;
            }
            else{
                temp=s.pop();
                System.out.print(temp.data+" ");
                temp=temp.right;  
            }
            
            
        }
    
        System.out.println();
    }
 

   
    public static void main(String args[] ){

    int[] list=new int[]{10,23,5,12,15,3,4};
    Node groot=null;
    for(int i=0;i<list.length;i++){
        //groot=insertionInBST(groot,list[i]);
        groot=insertionInBSTRecursive(groot,list[i]);
    }
    
    //System.out.println(searchInBST(groot,123));
    //searchInBSTGivingParent(groot,23,null);
    //System.out.println(minimumAtRightSubTree(groot));
     //deleteNode(groot,12);
     //treeTraversal(groot);\
	 //levelOrderTraversal(groot);
     //mirrorTree(groot);
     //treeTraversal(groot);
     //leftViewOfTree(groot);
     //rightViewOfTree(groot);
     //System.out.println("Sum at deepest level : "+sumAtDeepestLevel(groot));
     preOrderTraversalIterative(groot);
     postOrderTraversalIterative(groot);
     inOrderTraversalIterative(groot);
     
    }
}

/* Tree [10,23,5,12,15,3,4]
        10
        /\
       5  23
       /  /
       3  12
        \  \
         4  15       
 
*/

// to run
//javac BinarySearchTree.java
// java -cp . BinarySearchTree

// or
// set this in CLASSPATH
// JAVA_HOME = C:\Program Files\Java\jdk1.8.0_201
// CLASSPATH = %JAVA_HOME%\lib.;
