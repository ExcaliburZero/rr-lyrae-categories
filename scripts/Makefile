GRAPHTYPE=eps
GRAPHPATH=../graphs/
DATAPATH=~/Documents/ogle/

make_scatter = python scatter.py "RR$(1) Periods ($(2) OGLE $(3))" "Number" "Period (days)" $(GRAPHPATH)ogle$(5)_$(4)_RR$(1)_scatter.$(GRAPHTYPE) < $(DATAPATH)ogle$(5)/$(4)/RR$(1)-periods.dat

make_function = python function.py "RR$(1) Period Probability ($(2) OGLE $(3))" "Period (days)" "Probability" $(GRAPHPATH)ogle$(5)_$(4)_RR$(1)_probability.$(GRAPHTYPE) < $(DATAPATH)ogle$(5)/$(4)/RR$(1)-stats.dat

make_compare = python functions-overlay.py "RR Lyrae Categories Period Probability ($(1) OGLE $(2))" "Period (days)" "Probability" $(GRAPHPATH)ogle$(4)_$(3)_overall_probability.$(GRAPHTYPE) < $(DATAPATH)ogle$(4)/$(3)/overall.dat

help:
	@echo "all"
	@echo "scatter"
	@echo "function"
	@echo "overall"

all: scatter function overall

scatter:
	$(call make_scatter,ab,SMC,III,smc,3)
	$(call make_scatter,c,SMC,III,smc,3)
	$(call make_scatter,d,SMC,III,smc,3)
	$(call make_scatter,e,SMC,III,smc,3)

	$(call make_scatter,ab,LMC,III,lmc,3)
	$(call make_scatter,c,LMC,III,lmc,3)
	$(call make_scatter,d,LMC,III,lmc,3)
	$(call make_scatter,e,LMC,III,lmc,3)

	$(call make_scatter,ab,SMC,IV,smc,4)
	$(call make_scatter,c,SMC,IV,smc,4)
	$(call make_scatter,d,SMC,IV,smc,4)

	$(call make_scatter,ab,LMC,IV,lmc,4)
	$(call make_scatter,c,LMC,IV,lmc,4)
	$(call make_scatter,d,LMC,IV,lmc,4)

function:
	$(call make_function,ab,SMC,III,smc,3)
	$(call make_function,c,SMC,III,smc,3)
	$(call make_function,d,SMC,III,smc,3)
	$(call make_function,e,SMC,III,smc,3)

	$(call make_function,ab,LMC,III,lmc,3)
	$(call make_function,c,LMC,III,lmc,3)
	$(call make_function,d,LMC,III,lmc,3)
	$(call make_function,e,LMC,III,lmc,3)

	$(call make_function,ab,SMC,IV,smc,4)
	$(call make_function,c,SMC,IV,smc,4)
	$(call make_function,d,SMC,IV,smc,4)

	$(call make_function,ab,LMC,IV,lmc,4)
	$(call make_function,c,LMC,IV,lmc,4)
	$(call make_function,d,LMC,IV,lmc,4)

overall:
	$(call make_compare,SMC,III,smc,3)
	$(call make_compare,LMC,III,lmc,3)
	$(call make_compare,SMC,IV,smc,4)
	$(call make_compare,LMC,IV,lmc,4)
