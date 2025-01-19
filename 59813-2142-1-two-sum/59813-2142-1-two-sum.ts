   //python solution
   
//    def twoSum(self, nums, target):
//         found = {}
    
//         for index, value in enumerate(nums):
//                 remain = target - nums[index]

//                 if remain in found:
                  
//                     return [index, found[remain]]

//                 else:
//                     found[value]= index
//                     # print(found)
                


//ts way

// function twoSum(nums: number[], target: number): number[] {
//     const hashMap = new Map();

   
//     for (let i = 0; i < nums.length; i++) {
//         hashMap.set(nums[i], i);
//     }


//     for (let i = 0; i < nums.length; i++) {
//         const complement = target - nums[i];

        
//         if (hashMap.has(complement) && hashMap.get(complement) !== i) {
//             return [i, hashMap.get(complement)];
//         }
//     }

//     return [];
// }

function twoSum(nums: number[], target: number): number[] {
    const hashMap = new Map<number, number>(); 

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

       
        if (hashMap.has(complement)) {
            return [hashMap.get(complement), i];
        }

        hashMap.set(nums[i], i);
    }

    
    return [];
}

