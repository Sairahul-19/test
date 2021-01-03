# class Stack
# {
#   int s[10] =new int[10];
#   int top;
#   Stack()
#   {
#     top=-1;
#   }  
#   void push(int n)
#   {
#     if (top==9)  
#         System.out.println('Overflow error");
#     else
#        s[++top]= n;
       
#   }
  
#   void pop()
#   {
#     if (top==-1)
#         System.out.println('Underflow error");
#     else
#         System.out.println(s[top--]);
#   }
  
#   void display()
#   {
#     if (top==-1)
#         System.out.println("Stack is empty and there is nothing to be printed");
#     for (int i=top;i>=0;i--)
#        System.out.println(s[i]);
#   }
  
#   boolean is_empty()
#   {
#     if top == -1
#        return True;
#   }
  
#   int length()
#   {
#      return top+1;
#   }   
  
#   int top_pos()
#   {
#      return top;
     
#   }
# }  
# public class YourClassNameHere {
#     public static void main(String[] args) {
#   Stack s= new Stack();
  
#     }
# }
