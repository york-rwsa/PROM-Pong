`timescale 100ps / 10ps
`define MSBI 7

module DAC(
    input [7:0] DACin,
    input CLK,
    input Reset,
    output reg DACout
    );

reg [`MSBI + 2:0] DeltaAdder;
reg [`MSBI + 2:0] SigmaAdder;
reg [`MSBI + 2:0] SigmaLatch;
reg [`MSBI + 2:0] DeltaB;

always @(SigmaLatch) DeltaB = { SigmaLatch[`MSBI + 2], SigmaLatch[`MSBI + 2] } << (`MSBI + 1);
always @(DACin or DeltaB) DeltaAdder = DACin + DeltaB;
always @(DeltaAdder or SigmaLatch) SigmaAdder = DeltaAdder + SigmaLatch;

always @(posedge CLK or posedge Reset)
begin
	if (Reset)
	begin
		SigmaLatch <= #1 1'b1 << (`MSBI + 1);
		DACout <= #1 1'b0;
	end
	else
	begin
		SigmaLatch <= #1 SigmaAdder;
		DACout <= #1 SigmaLatch[`MSBI + 2];
	end
end

endmodule
