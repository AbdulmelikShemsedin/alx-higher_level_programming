#!/usr/bin/node
/* a script that prints argument passed to it
 */
const args = process.argv;

if (args[2] === NULL) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
