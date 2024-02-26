%BPSK  transmission
clear all;
clc;

%Transmission end
modulation = 16;
symbols = 100;

symbol_padding = 4;

random_numbers = randi([0,1],[1,modulation*symbols]);
%random_numbers = ones(1,100);


%Select modulation scheme

%QAM-4

%We sliceoutu our bit squence into chunks of 16 to feed into our modulator
bit_chunks = reshape(random_numbers,sqrt(modulation),[]);

for a = 1:size(bit_chunks,2)

  dummy(a) = bin2dec(char(bit_chunks(:,a)'+'0'));
  modulated_signal(a) = qammod(dummy(a),modulation);
endfor



modulated_zero_padded = zeros(1,symbol_padding*length(modulated_signal));

modulated_zero_padded([1:symbol_padding:end])=modulated_signal;


root_raised_cosine = rcosfir(0.25,4,4,1,'sqrt');



output_real = conv(root_raised_cosine,real(modulated_zero_padded));

output_imag= conv(root_raised_cosine,imag(modulated_zero_padded));


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

