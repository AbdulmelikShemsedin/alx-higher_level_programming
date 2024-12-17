#!/usr/bin/node
/* script that prints messege depending of the num of args
*/
const args = process.argv;

if (args.length == 2){
    console.log("No argument", args);
} else if (args.length == 3){
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
