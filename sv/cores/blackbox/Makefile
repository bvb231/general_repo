blackbox :=  counter/testbench \


.PHONY: $(blackbox)

.PHONY: all
all: $(blackbox)

$(blackbox):
	@cd $@ && $(MAKE)

.PHONY: clean
clean:
	$(foreach TEST, $(blackbox), $(MAKE) -C $(TEST) clean;)

regression:
	$(foreach TEST, $(blackbox), $(MAKE) -C $(TEST) regression;)
