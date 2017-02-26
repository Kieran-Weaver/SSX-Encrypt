#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "pcg_variants.h"
#include "entropy.h"                    // Wrapper around /dev/random

uint64_t f(uint64_t s, uint64_t s2)
{
    // Read command-line options

    int rounds = 25;
    bool nondeterministic_seed = false;
    pcg64_random_t rng;
    pcg64_srandom_r(&rng, s, s2);
    for (int round = 1; round <= rounds; ++round) {

        for (int i = 0; i < 6; ++i) {
            pcg64_random_r(&rng);
        }
        pcg64_advance_r(&rng, -6);
        for (int i = 0; i < 6; ++i) {
            pcg64_random_r(&rng);
        }
    }

    return pcg64_random_r(&rng);
}
void stream_cipher(uint64_t * retval, uint64_t iv, uint64_t length_, uint64_t * key_blocks, uint64_t *plaintext_blocks){
    for (int i=0;i<length_;i++){
        retval[i] = plaintext_blocks[i] ^ f(iv,key_blocks[i]);
    }
}
int main(){
    uint64_t *vals = (uint64_t *)(malloc(5*sizeof(uint64_t)));
    uint64_t *vals2 = (uint64_t *)(malloc(5*sizeof(uint64_t)));
    uint64_t ptext[] = {0x00bab10c,0xbeefdead,0x13374201,0xBAAAAAAD};
    uint64_t ktext[] = {0xbeefdead,0x42011337,0xbeefdedd,0x12345678};
    stream_cipher(vals,0xdeadbeef,4,ptext,ktext);
    stream_cipher(vals2,0xdeadbeef,4,ptext,vals);
    printf("%lx \n",vals2[0]);
    printf("%lx \n",vals2[1]);
    printf("%lx \n",vals2[2]);
    printf("%lx \n",vals2[3]);
    return 0;
}
