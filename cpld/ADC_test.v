`timescale 1us / 100ns
`include "ADC.v"

module ADC_test;

	// Inputs
	reg Reset;
	reg CLK;
	reg gtRef;

	// Outputs
	wire [6:0] ADCout;
	wire DACout;
	wire ADCsampled;

	// Instantiate the Unit Under Test (UUT)
	ADC uut (
		.ADCout(ADCout), 
		.DACout(DACout), 
		.ADCsampled(ADCsampled), 
		.Reset(Reset), 
		.CLK(CLK), 
		.gtRef(gtRef)
	);

	always #1 CLK = ~CLK;

	initial begin
		// Initialize Inputs
		Reset = 0;
		CLK = 0;
		gtRef = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		Reset = 1'b1;
		#100;
		Reset = 1'b0;
		
		#256;
		gtRef = 1;
		#512;
		gtRef = 0;
		#1100;
		gtRef = 1;
		#256;
		gtRef = 0;
	end
      
endmodule

