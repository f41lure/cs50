{"filter":false,"title":"vigenere7.c","tooltip":"/vigenere7.c","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":61,"column":1},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"efe77852e3edd68390e0b4139b033056b23bc8e8","undoManager":{"mark":52,"position":52,"stack":[[{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":[" "],"id":1}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["t"],"id":2}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["o"],"id":3}],[{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["l"],"id":4}],[{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["o"],"id":5}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["w"],"id":6}],[{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["e"],"id":7}],[{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":["r"],"id":8}],[{"start":{"row":33,"column":15},"end":{"row":33,"column":17},"action":"insert","lines":["()"],"id":9}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["s"],"id":10}],[{"start":{"row":33,"column":17},"end":{"row":33,"column":19},"action":"insert","lines":["[]"],"id":11}],[{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":["i"],"id":12}],[{"start":{"row":18,"column":5},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["t"],"id":14}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["o"],"id":15}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["l"],"id":16}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["o"],"id":17}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["w"],"id":18}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["e"],"id":19}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["r"],"id":20}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":17},"action":"insert","lines":["()"],"id":21}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["k"],"id":22}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["e"],"id":23}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["y"],"id":24}],[{"start":{"row":19,"column":19},"end":{"row":19,"column":21},"action":"insert","lines":["[]"],"id":25}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["k"],"id":26}],[{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":[";"],"id":27}],[{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"remove","lines":[" "],"id":28}],[{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":[";"],"id":29}],[{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"remove","lines":["6"],"id":30}],[{"start":{"row":70,"column":34},"end":{"row":70,"column":35},"action":"remove","lines":[" "],"id":31}],[{"start":{"row":70,"column":33},"end":{"row":70,"column":34},"action":"remove","lines":["-"],"id":32}],[{"start":{"row":70,"column":32},"end":{"row":70,"column":33},"action":"remove","lines":[" "],"id":33}],[{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":["6"],"id":34}],[{"start":{"row":50,"column":34},"end":{"row":50,"column":35},"action":"remove","lines":[" "],"id":35}],[{"start":{"row":50,"column":33},"end":{"row":50,"column":34},"action":"remove","lines":["-"],"id":36}],[{"start":{"row":50,"column":32},"end":{"row":50,"column":33},"action":"remove","lines":[" "],"id":37}],[{"start":{"row":37,"column":0},"end":{"row":80,"column":9},"action":"remove","lines":["        if (isupper(s[j]) && isupper(key[j])) ","        {","            int a = (int) key[j] - 65;","            int b = ((int) s[i]);","            int c = (a + b - 65) % 26 + 65;","            printf(\"%c\", (char) c);","            j++;","        }","","        // encode uppercase letters & check case of key value","        else if (isupper(s[i]) && islower(key[j])) ","        {","            int a = (int) key[j] - 65;","            int b = ((int) s[i]);","            int c = (a + b - 65) % 26 + 65;","            printf(\"%c\", (char) c);","            j++;","        }","","        // encode lowercase letters & check case of key value","        else if (islower(s[i]) && islower(key[j])) ","        {","            int a = (int) key[j] - 97;","            int b = ((int) s[i]);","            int c = (a + b - 97) % 26 + 97;","            printf(\"%c\", (char) c);","            j++;","        }","","        // encode lowercase letters & check case of key value","        else if (islower(s[i]) && isupper(key[j])) ","        {","            int a = (int) key[j] - 97;","            int b = ((int) s[i]);","            int c = (a + b - 97) % 26 + 97;","            printf(\"%c\", (char) c);","            j++;","        }","        ","        else if (isalpha(s[i]) == false)        // Program will still increase key even if a space is present","        {","            printf(\"%c\", s[i]);","            ","        }"],"id":38}],[{"start":{"row":36,"column":2},"end":{"row":36,"column":4},"action":"insert","lines":["  "],"id":39}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"insert","lines":["    "],"id":40}],[{"start":{"row":36,"column":8},"end":{"row":56,"column":9},"action":"insert","lines":["        if (isupper(s[i]))","        {","            int a = (int) key[j] - 65;","            int b = ((int) s[i]);","            int c = (a + b - 65) % 26 + 65;","            printf(\"%c\", (char) c);","            j++;","        }","        else if (islower(s[i]))","        {","            int a = (int) key[j] - 97;","            int b = ((int) s[i]);","            int c = (a + b - 97) % 26 + 97;","            printf(\"%c\", (char) c);","            j++;","        }","        else if (isalpha(s[i]) == false)        // Program will still increase key even if a space is present","        {","            printf(\"%c\", s[i]);","            ","        }"],"id":41}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"remove","lines":[" "],"id":42}],[{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"remove","lines":[" "],"id":43}],[{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"remove","lines":[" "],"id":44}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":12},"action":"remove","lines":["    "],"id":45}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"remove","lines":["    "],"id":46}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":[" "],"id":48}],[{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":[" "],"id":49}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"remove","lines":["5"],"id":50}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["6"],"id":51}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["9"],"id":52}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["7"],"id":53}]]},"timestamp":1502989356366}