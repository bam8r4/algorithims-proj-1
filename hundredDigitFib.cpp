//This program will find the the first fibonacci number to be under 100 digits long. 
#include <iostream>
using namespace std;

//This function is used to sanitize my arrays of any previous values. 
void arraySetter(int arr[])
{
    for(int i = 0; i < 100; i++)
    {
        arr[i] = 0;
    }
}

int main()
{
    
    bool isDone = true;
    
    //This is the true array that we will output at the end.
    int arr1[100];
    
    //These two arrays just shuffle fibonacci number around so we can continue the sequence.
    int arr2[100];
    int arrTemp[100];
    
    //Calling above funtion to sanitize all array I plan to use. 
    arraySetter(arr1);
    arraySetter(arr2);
    arraySetter(arrTemp);
    
    //I am setting the the first value of the second array to one so a fib sequence can occur. 
    arr2[99] = 1;
    
   while(isDone)
    {
        if(arr2[0] != 0)
        {
            isDone = false;
            cout<<"Ending program the array has reached more than 100 digits.\n\n";
            break;
        }
        
        //This loop is creating a sum of both arrays without a carry value. 
        for (int i = 99; i > -1; i--)
        {
            arrTemp[i]=(arr2[i]+arr1[i]);
        }
        
        //This loop goes through and performs any carry operations that need to be done. 
        for (int i = 99; i > -1; i--)
        {
            if(arrTemp[i]>9)
            {
                arrTemp[i-1] = arrTemp[i-1]+1;
                arrTemp[i] = arrTemp[i] % 10;
            } 
        }
        
        //Reassigning Array 1 to Array 2.
        for(int j=0; j<100; j++)
        {
            arr1[j]=arr2[j];
           
        }
        
        //Reassigning Array 2 to our Temp Array
        for(int j=0; j<100; j++)
        {
            arr2[j]=arrTemp[j];
        }
        
    }
    
    cout<<"The greatest value with 99 digits in the Fibonacci sequence is: " << endl;
    
     for(int i = 1; i < 100; i++)
    {
        cout << arr1[i];
    }

    return 0;
}








