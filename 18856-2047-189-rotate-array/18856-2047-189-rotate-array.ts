/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    
    const abc =  new Array(nums.length) 
  
    for (let j = 0; j <(nums.length) ; j++ ){

        abc [(j+k)%(nums.length)] = nums[j]

    }

    for (let i= 0 ; i <(nums.length) ; i++){

        nums[i] = abc[i]


    }


}