

fn = 'music_orig.wav';
[x,fs] = audioread(fn);
display(size(x));

plot(x);
xlabel('Samples');
ylabel('J/Hz');
title('Audio Signal');
