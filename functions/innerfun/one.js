
const duplicates = [9, 4, 9, 1, 4, 6, 7, 2, 1, 6];

const a =duplicates.indexOf(4)
console.log(a);

// dupliactes
// sort 


const removeDupliactes = duplicates.filter((currentvalue,accumaltevalue)=>duplicates.indexOf(currentvalue)==accumaltevalue)
console.log(removeDupliactes);

// const a= removeEventListener.sort((a,b)=>a-b);
// const b = duplicates.sort((a, b) => a-b);

// console.log(b); // Output: [1, 1, 2, 4, 4, 6, 6, 7, 9, 9]
