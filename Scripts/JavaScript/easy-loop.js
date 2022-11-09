function oneToRuleThemAll(array1, num1, string1) {
  // this function is given 3 arguments: an array of strings, a number, and a string
  // this challenge is going to be tough, but take it one step at a time
  // find the built in function that fits the situation and learn how to use it
  // you will most likely have to write your own mini function inside this function for part of it
  // we will have to write code to do the following:
  // filter the array based on the number of characters of num1
  // replace any instances of the first word in the new array with string1
  // combine the array into one string and extract the characters starting at the 2nd character and counting 8 characters out inclusively
  // return the last 3 characters in reverse order in all Upper Case
  // Example...
  // array1 = [“at”, “flag”, “words”, “round”, “object”, “run”, “will”, “how”, “to”, “set”, “then”, “flag”, “run”, “will”, “at”, “do”, “run”]
  // num1 = 3
  // string1 = “new”
  // newArray1 = [“run”, “how”, “set”, “run”, “run”]
  // newArray2 = [“new”, “how”, “set”, “new”, “new”]
  // newString1 = “newhowsetnewnew”
  // newString2 = “ewhowset”
  // finalString = “TES”

console.log(string1)
console.log(num1)
newArray1=[];
k=0;    
for( i=0;i<array1.length;i++)
{ 
if(array1[i].length==num1)
{ 
newArray1[k]=array1[i];
k=k+1;
}
 
}
console.log(newArray1)
 
//newarray1=[];
string2=newArray1[0]
newArray2=newArray1
for( i=0;i<newArray1.length;i++)
{ 
if(newArray1[i]==string2)
{ 
newArray2[i]=string1;
}
 
}
//console.log(newarray1)
 
newString1="";
newString2="";
finalString="";
for( i=0;i<newArray2.length;i++)
{     
newString1=newString1+newArray2[i];
}
 
newString2=newString1.substring(1,9)

//console.log(string4)
finalString=newString2[newString2.length-1]+newString2[newString2.length-2]+newString2[newString2.length-3]


finalString=finalString.toUpperCase()
console.log(finalString);

return finalString

}

module.exports = { oneToRuleThemAll }
