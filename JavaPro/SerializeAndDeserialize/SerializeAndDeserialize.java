//leetcode 297. Serialize and Deserialize Binary Tree

import java.util.*;
public class Codec {
    
   ArrayList<String> al=new ArrayList<>();
   TreeNode newRoot;
    
  // Encodes a tree to a single string.
public ArrayList serialize(TreeNode root) {
    if (root==null){
        al.add("null");
        return al;
    } 
    
    al.add(""+root.val);
    serialize(root.left);
    serialize(root.right);
    //System.out.println(al);
    return al;
}

// Decodes your encoded data to tree.
public TreeNode deserialize(ArrayList<String> data) {
    if (data==null) return null;
    int[] t = {0};
    return helper(data, t);
}
    public TreeNode helper(ArrayList<String> arr, int[] t){
       // System.out.println(arr.get(t[0]));
         if(arr.get(t[0])=="null"){
        return null;
    }
 
    TreeNode root = new TreeNode(Integer.parseInt(arr.get(t[0])));
 
    t[0]=t[0]+1;
    root.left = helper(arr, t);
    t[0]=t[0]+1;
    root.right = helper(arr, t);
 
    return root;
    } 

}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));