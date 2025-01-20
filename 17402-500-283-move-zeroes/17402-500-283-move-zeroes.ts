/**
 Do not return anything, modify nums in-place instead.
 */


 //not a good solution
function moveZeroes(nums: number[]): void {

    let num  = 0

    const filtere = nums.filter((n)=> {
        
        
        return n!==0
        
        }
        
        
        
        )

    console.log(filtere)


    let zeroneeded =  nums.length - filtere.length

    for (let i=0 ; i < zeroneeded ; i ++ ){

        filtere.push(0)


    }

     for (let i=0 ; i < nums.length ; i ++ ){

        nums[i] =  filtere[i]


    }




    
};