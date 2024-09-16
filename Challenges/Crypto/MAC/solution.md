cat emoji

Intended solution path:
1. Reverse MT19937 internal state by selecting option 1 624 times
2. Observe that "MAC" is really just CRC
3. Understand CRC is really just modulo and CRT exists
4. Obtain ~10 (mac, key) pairs and CRT to get flag

Flag: `blahaj{cRc_m0RE_l1ke_Cr7}`