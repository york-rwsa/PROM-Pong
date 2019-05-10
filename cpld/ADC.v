`timescale 1ns / 1ps

`include "DAC.v"

module ADC(
    output reg [`MSBI - 1:0] ADCout,
    output DACout,
	 output reg ADCsampled,
    input Reset,
    input CLK,
	 input gtRef
    );


reg [`MSBI:0] Reference;
reg [`MSBI:0] Mask;

reg [`MSBI:0] DACcounter;
reg DACsampled;

reg Shift;

// dac requires one full cycle to realise output
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	DACcounter <= #1 0;
	else 			DACcounter <= #1 DACcounter + 1;
end

// once dac counter overflows DAC output has stabalised 
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	DACsampled <= #1 0;
	else 			DACsampled <= #1 (DACcounter == 0);
end

// add clock cycle delay to shift 
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	Shift <= #1 0;
	else 			Shift <= #1 DACsampled;
end

// ADCsample reg
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	ADCsampled <= #1 0;
	// if DACcounter & the mask reg has gone through each state, ie Mask[0] == 1
	else 			ADCsampled <= #1 (DACcounter & Mask[0]);
end

// mask shifter
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	Mask <= #1 0;
	else
	if (Shift)
	begin
	   // |var is reduction or
		// means each element of var OR'd together
		// ie var = 01010, |var = 1,
		//    var = 00000, |var = 0
		// this if makes sure only 1 bit is set
		if (Mask[1] | ~(|Mask)) Mask <= #1 1;
		else Mask <= #1 { Mask[0], Mask[`MSBI:1] }; // shift right
	end
end

// reference reg
// input to dac
always @ (posedge CLK or posedge Reset)
begin
	if (Reset) Reference <= #1 0;
	else if (Shift)
		Reference <= #1 	{ Mask[0], Mask[`MSBI:1] } | (
									Reference &
									~{ (`MSBI + 1) { Mask[0] } } &
									~(Mask & ~{ (`MSBI + 1) { gtRef } })
								);
end

// output reg
always @ (posedge CLK or posedge Reset)
begin
	if (Reset)	ADCout <= #1 0;
	else if (ADCsampled) ADCout <= #1 Reference[`MSBI:1];
end

DAC dacObj (
	.DACout (DACout),
	.DACin (Reference),
	.CLK (CLK),
	.Reset (Reset)
);

endmodule
