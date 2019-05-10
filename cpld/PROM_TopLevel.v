`timescale 1ns / 1ps
`include "ADC.v"
`include "SevenSeg.v"

`define MSBI 7

module PROM_TopLevel(
    output [`MSBI - 1:0] ADCout,
    output DACout,
    input gtRef,
    input CLK,
    input Reset,
	 input [3:0] bcd,
	 output [6:0] segOut
    );

ADC adcObj (
	.ADCout (ADCout),
	.DACout (DACout),
	.gtRef (gtRef),
	.CLK (CLK),
	.Reset (Reset)
	);

SevenSeg seg (
	.bcd (bcd),
	.out (segOut)
	);

//reg [`MSBI:0] counter;
//reg [`MSBI:0] counter2;
//
//always @ (posedge CLK or posedge Reset)
//begin
//	if 		(Reset)			 counter <= #1 0;
//	else if 	(counter2 == 0) counter <= #1 counter + 1;
//end
//
//always @ (posedge CLK or posedge Reset)
//begin
//	if (Reset)	counter2 <= #1 0;
//	else 			counter2 <= #1 counter2 + 1;
//end
//
//DAC dacObj (
//	.DACout (DACout),
//	.DACin (counter),
//	.CLK (CLK),
//	.Reset (Reset)
//);


endmodule
