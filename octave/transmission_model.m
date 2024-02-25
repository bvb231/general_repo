%BPSK  transmission
clear all;
clc;

%Transmission end

symbol_padding = 4;

random_numbers = randi([0,1],[1,100]);
%random_numbers = ones(1,100);

rand_num_zero_padded = zeros(1,symbol_padding*length(random_numbers));

rand_num_zero_padded([1:symbol_padding:end])=random_numbers;


root_raised_cosine = rcosfir(0.25,4,4,1,'sqrt');


output = conv(root_raised_cosine,rand_num_zero_padded);


%plot(output)


%%Channel Model








%Receiver end`
rx_input = conv(root_raised_cosine,output);


rx_input_ds = downsample(rx_input,symbol_padding);
%plot(rx_input)
%plot(rx_input_ds)

rx_input_ds = rx_input_ds([9:end]);

rounded_input = round(rx_input_ds);



%Perfect match!
plot(random_numbers)
hold on;
plot(rounded_input)

