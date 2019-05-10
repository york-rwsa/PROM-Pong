`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   14:17:01 05/09/2019
// Design Name:   SevenSeg
// Module Name:   M:/prom-ise/PROM/SevenSeg_test.v
// Project Name:  PROM
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: SevenSeg
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////
`include "SevenSeg.v"
module SevenSeg_test;

	// Inputs
	reg [3:0] bcd;

	// Outputs
	wire [6:0] out;

	// Instantiate the Unit Under Test (UUT)
	SevenSeg uut (
		.bcd(bcd), 
		.out(out)
	);

	integer i;

	initial begin
		// Initialize Inputs
		bcd = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		for(i = 0; i < 16; i = i+1) //run loop for 0 to 15.
		begin
			bcd = i; 
			#10; //wait for 10 ns
		end   
	end
      
endmodule

