rev $1 | awk 'BEGIN{FS=""}{for(i=1;i<=NF;i=i+1){if($i=="A")Sc=Sc"T";else if($i=="C")Sc=Sc"G";else if($i=="G")Sc=Sc"C";else if($i=="T")Sc=Sc"A"};print Sc}'