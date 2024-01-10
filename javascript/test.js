
process.stdin.resume();
  
// We are using this single function to handle multiple signals
function handle(signal) {
    console.log("SIGINT");
    process.exit(1);
}
 
process.on('SIGINT', handle);
