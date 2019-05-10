`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:34:46 05/07/2019
// Design Name:   DAC
// Module Name:   M:/prom-ise/PROM/DAC_test.v
// Project Name:  PROM
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: DAC
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////
`timescale 1 us / 100 ns


module DAC_test;

	// Inputs
	reg [7:0] DACin;
	reg CLK;
	reg Reset;

	// Outputs
	wire DACout;

	// Instantiate the Unit Under Test (UUT)
	DAC uut (
		.DACin(DACin), 
		.CLK(CLK), 
		.Reset(Reset), 
		.DACout(DACout)
	);

	always #1000 CLK = ~CLK;

	initial begin
		// Initialize Inputs
		DACin = 0;
		CLK = 0;
		Reset = 0;
		
		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		Reset = 1'b1;
		#100
		Reset = 1'b0;
		
		DACin = 8'b10010101;
	end
      
endmodule

