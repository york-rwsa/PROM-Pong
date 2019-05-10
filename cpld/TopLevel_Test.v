`timescale 1ns / 1ps

module TopLevel_Test;

	// Inputs
	reg gtRef;
	reg CLK;
	reg Reset;

	// Outputs
	wire [6:0] ADCout;
	wire DACoutDriver;

	// seven seg
	reg [3:0] bcd;
	wire [6:0] out;
	integer i;

	// Instantiate the Unit Under Test (UUT)
	PROM_TopLevel uut (
		.ADCout(ADCout), 
		.DACout(DACoutDriver), 
		.gtRef(gtRef), 
		.CLK(CLK), 
		.Reset(Reset),
		.bcd (bcd),
		.segOut (out)
	);


	always #1000 CLK = ~CLK;

	initial begin
		// Initialize Inputs
		gtRef = 0;
		CLK = 0;
		Reset = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		Reset = 1'b1;
		#10
		Reset = 1'b0;
		
		for(i = 0; i < 16; i = i+1) //run loop for 0 to 15.
		begin
			bcd = i; 
			#10; //wait for 10 ns
		end   
	end
      
endmodule

