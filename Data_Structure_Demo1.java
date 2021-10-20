
public class Data_Structure_Demo1{

    public static void main(String[] args){
        int[] arr = {1,2,3,4};
        //String[] stringArr = {"a","b"};
       // printLoop(arr);

        //printForEachLoop(arr,stringArr);

        printNestedLoops(arr);
    }

    public static void printArray(int[] numbers){
       
       //requires O(1) runtime complexity, as it is dependent on just 1 varible numbers[0]
        System.out.println(numbers[0]);
        //still requires O(1) runtime complexity, as it is dependent on just 1 varible numbers[0] and numbers[1] and it will run im constant time,
        // does not matter how many prints we have, the input is dependent on 1 constant variable
        System.out.println(numbers[1]);
    }

    //requires O(n) time as now the runtime depends on the number of iterations the loop runs or the length of the num array or basically
    //the cost of this algo grows linearly and is in direct corelation with the size of the input 
	//so O(n)	runtime complexity

    public static void printLoop(int[] num){
        for(int i=0; i< num.length; i++){
            System.out.println(num[i]);
        }

    }


// now the complexity depends on two input arrays int and string
    public static void printForEachLoop(int[] num,String[] name){
       
       //both the loops run in O(n) time but we dont have the same input we have n for int and m for string array
       //so the complexity of the method will be O(n+m)
       //which can again be simplified to O(n) because the runtime increases linearly, this n is to show linear relation not just the first input array
        for(int numbers : num){ //O(n)
            System.out.println(numbers);
        }

        for(String names : name){ //O(m)
            System.out.println(names);
        }

    }

  // nested loops complexity
    public static void printNestedLoops(int[] number){
        //so our total complexity is O(n*n) not O(n+n) as for each outer n we have their own n length array
        
        for(int one : number){ //O(n)
            
            for(int two : number){ //O(n)
                //{1,2,3,4}= input array
                System.out.print(one + two);
                // 2345345645675678 = output
            }

            //for 4 inputs we have 16 outputs, the outer loop ran 4 times and the inner loop ran 16 times, 4 times for every "one" value
            //since we are using the same array numbers as input to our algorithm
            // the runtime complexity of our algorithm increases quadratically with the number of input
            //so O(n^2) "O of n squared"
    
        }
       
    }  
}