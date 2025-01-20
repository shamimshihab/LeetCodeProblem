/**
 Do not return anything, modify nums in-place instead.
 */



//better code 



function moveZeroes(nums: number[]): void {


    let zerod :number  =  0

    for (let i = 0 ; i < nums.length ; i ++ ){

        if(nums[i]!== 0 ){

            let tempA =  nums[i]
            
            // nums[i] = 0

             nums[i] = nums[zerod]


            nums[zerod] = tempA 
         

            zerod ++


        }



    }







    
};

 //not a good solution
// function moveZeroes(nums: number[]): void {

//     let num  = 0

//     const filtere = nums.filter((n)=> {
        
        
//         return n!==0
        
//         }
        
        
        
//         )

//     console.log(filtere)


//     let zeroneeded =  nums.length - filtere.length

//     for (let i=0 ; i < zeroneeded ; i ++ ){

//         filtere.push(0)


//     }

//      for (let i=0 ; i < nums.length ; i ++ ){

//         nums[i] =  filtere[i]


//     }




    
// };